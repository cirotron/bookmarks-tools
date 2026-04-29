import json
import os
import shutil

# Cambiá según tu navegador y sistema operativo
BOOKMARKS_PATH = os.path.expanduser(
    r"~\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks"
)
EXPORT_FILE = "favoritos_filtrados.txt"


def extract_and_filter(bookmark_node, search_text, results, parents):
    """Recorre recursivamente los favoritos."""
    if bookmark_node.get("type") == "url":
        name = bookmark_node.get("name", "")
        url = bookmark_node.get("url", "")
        if search_text.lower() in name.lower() or search_text.lower() in url.lower():
            results.append((name, url, parents, bookmark_node))
    elif bookmark_node.get("type") == "folder":
        for child in bookmark_node.get("children", []):
            extract_and_filter(child, search_text, results, parents + [bookmark_node])


def main():
    search_text = input("🔎 Texto a buscar en favoritos: ").strip()

    # Leer archivo JSON de favoritos
    with open(BOOKMARKS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    roots = data.get("roots", {})
    for key in ["bookmark_bar", "other", "synced"]:
        if key in roots:
            extract_and_filter(roots[key], search_text, results, [])

    if not results:
        print("❌ No se encontraron coincidencias.")
        return

    # Mostrar resultados
    print("\nResultados encontrados:")
    for i, (name, url, _, _) in enumerate(results, start=1):
        print(f"{i}. {name}: {url}")

    # Exportar a archivo
    with open(EXPORT_FILE, "w", encoding="utf-8") as f:
        for name, url, _, _ in results:
            f.write(f"{name}: {url}\n")
    print(f"\n✅ Exportado a {EXPORT_FILE}")

    # Preguntar si eliminar
    choice = input("\n¿Querés eliminar estos favoritos del navegador? (s/n): ").strip().lower()
    if choice != "s":
        print("❎ No se eliminó nada.")
        return

    # Hacer backup
    backup_path = BOOKMARKS_PATH + ".bak"
    shutil.copy2(BOOKMARKS_PATH, backup_path)
    print(f"📂 Backup creado en {backup_path}")

    # Eliminar coincidencias
    for _, _, parents, node in results:
        for parent in parents:
            if "children" in parent and node in parent["children"]:
                parent["children"].remove(node)

    # Guardar cambios
    with open(BOOKMARKS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("🗑️ Favoritos eliminados correctamente.")


if __name__ == "__main__":
    main()