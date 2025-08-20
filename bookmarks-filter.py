import json
import os

# Cambiá según tu navegador y sistema operativo
BOOKMARKS_PATH = os.path.expanduser(
    r"~\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks"
)

SEARCH_TEXT = "chatgpt"  # Texto a buscar en título o URL
EXPORT_FILE = "favoritos_filtrados.txt"


def extract_bookmarks(bookmark_node, results):
    """Recorre recursivamente los favoritos."""
    if bookmark_node.get("type") == "url":
        name = bookmark_node.get("name", "")
        url = bookmark_node.get("url", "")
        if SEARCH_TEXT.lower() in name.lower() or SEARCH_TEXT.lower() in url.lower():
            results.append((name, url))
    elif bookmark_node.get("type") == "folder":
        for child in bookmark_node.get("children", []):
            extract_bookmarks(child, results)


def main():
    # Leer archivo JSON de favoritos
    with open(BOOKMARKS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    roots = data.get("roots", {})
    for key in ["bookmark_bar", "other", "synced"]:
        if key in roots:
            extract_bookmarks(roots[key], results)

    # Mostrar resultados
    for name, url in results:
        print(f"{name}: {url}")

    # Exportar a archivo
    if results:
        with open(EXPORT_FILE, "w", encoding="utf-8") as f:
            for name, url in results:
                f.write(f"{name}: {url}\n")
        print(f"\n✅ Exportado a {EXPORT_FILE}")
    else:
        print("\n❌ No se encontraron coincidencias.")


if __name__ == "__main__":
    main()
