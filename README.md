# bookmarks-tools

Scripts en Python para trabajar con favoritos en navegadores basados en Chromium (Brave, Chrome, Edge, Opera, Vivaldi).

## Descripción

`bookmarks-filter.py` permite buscar favoritos por texto, previsualizar los resultados, exportarlos a un archivo y opcionalmente eliminarlos del navegador, todo desde la terminal.

---

## Requisitos

- Python 3.x
- Un navegador basado en Chromium (Brave, Chrome, Edge, Opera, Vivaldi)
- El navegador debe estar **cerrado** al momento de ejecutar el script

---

## Configuración

Antes de usar el script, verificá que la variable `BOOKMARKS_PATH` apunte al archivo de favoritos de tu navegador.

Abrí `bookmarks-filter.py` y modificá esta línea:

```python
BOOKMARKS_PATH = os.path.expanduser(r"~\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks")
```

### Rutas por navegador

#### Windows

| Navegador | Ruta |
|-----------|------|
| **Brave** | `~\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks` |
| **Chrome** | `~\AppData\Local\Google\Chrome\User Data\Default\Bookmarks` |
| **Edge** | `~\AppData\Local\Microsoft\Edge\User Data\Default\Bookmarks` |
| **Opera** | `~\AppData\Roaming\Opera Software\Opera Stable\Bookmarks` |
| **Opera GX** | `~\AppData\Roaming\Opera Software\Opera GX Stable\Bookmarks` |
| **Vivaldi** | `~\AppData\Local\Vivaldi\User Data\Default\Bookmarks` |

#### macOS

| Navegador | Ruta |
|-----------|------|
| **Brave** | `~/Library/Application Support/BraveSoftware/Brave-Browser/Default/Bookmarks` |
| **Chrome** | `~/Library/Application Support/Google/Chrome/Default/Bookmarks` |
| **Edge** | `~/Library/Application Support/Microsoft Edge/Default/Bookmarks` |
| **Opera** | `~/Library/Application Support/com.operasoftware.Opera/Bookmarks` |
| **Vivaldi** | `~/Library/Application Support/Vivaldi/Default/Bookmarks` |

#### Linux

| Navegador | Ruta |
|-----------|------|
| **Brave** | `~/.config/BraveSoftware/Brave-Browser/Default/Bookmarks` |
| **Chrome** | `~/.config/google-chrome/Default/Bookmarks` |
| **Chromium** | `~/.config/chromium/Default/Bookmarks` |
| **Edge** | `~/.config/microsoft-edge/Default/Bookmarks` |
| **Opera** | `~/.config/opera/Bookmarks` |
| **Vivaldi** | `~/.config/vivaldi/Default/Bookmarks` |

> **Nota:** Si usás múltiples perfiles en el navegador, reemplazá `Default` por el nombre del perfil correspondiente (ej: `Profile 1`).

---

## Uso

> ⚠️ **Cerrá el navegador antes de ejecutar el script.** De lo contrario, los cambios pueden perderse o corromperse al reabrir el navegador.

Ejecutá el script desde la terminal:

```bash
python bookmarks-filter.py
```

### Flujo paso a paso

1. **Búsqueda** — El script pide el texto a buscar (se aplica sobre el nombre y la URL del favorito).
2. **Resultados** — Muestra en pantalla todos los favoritos que coinciden.
3. **Exportación** — Guarda los resultados en `favoritos_filtrados.txt` en el directorio actual.
4. **Eliminación (opcional)** — Pregunta si querés eliminar esos favoritos del navegador.
   - Si respondés **`s`**: hace un backup automático (`Bookmarks.bak`) y borra las coincidencias del archivo original.
   - Si respondés **`n`**: no modifica nada.

---

## Archivos generados

| Archivo | Descripción |
|---------|-------------|
| `favoritos_filtrados.txt` | Lista de favoritos encontrados en la última búsqueda |
| `Bookmarks.bak` | Copia de seguridad del archivo original, creada antes de eliminar |

---

## Licencia

MIT — ver [LICENSE](LICENSE).
