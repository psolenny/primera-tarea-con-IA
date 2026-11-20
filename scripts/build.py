# Genera las páginas del sitio. Uso: python3 scripts/build.py
import pathlib, shutil
import paginas as P
from rutas import RUTAS, F
from deck import DECK, SLIDES

# El sitio se escribe en la raíz del repo (la carpeta que contiene scripts/).
# Los archivos de assets/ (site.css, deck.css, deck.js y logos) no se generan: vienen del sitio de la charla.
OUT = pathlib.Path(__file__).resolve().parent.parent
for d in ("assets", "kit", "rutas/descargas"): (OUT / d).mkdir(parents=True, exist_ok=True)
(OUT / "assets/taller.css").write_text(P.TALLER_CSS, encoding="utf-8")

w = lambda rel, txt: (OUT / rel).write_text(txt, encoding="utf-8")
w("index.html", P.index())
w("presentacion.html", DECK)
w("rutas/index.html", P.rutas_index())
for i, r in enumerate(RUTAS):
    w(f"rutas/{r['slug']}.html", P.ruta(r, i))
    w(f"rutas/descargas/{r['archivo']}", r["fuente"] + "\n")
    w(f"rutas/descargas/{r['b_archivo']}", r["b_fuente"] + "\n")
for n, f in (("index", P.kit_index), ("metodo", P.kit_metodo), ("claro", P.kit_claro), ("datos", P.kit_datos),
             ("recuperacion", P.kit_recuperacion), ("plataformas", P.kit_plataformas), ("hoja", P.kit_hoja)):
    w(f"kit/{n}.html", f())
print(len(SLIDES), "láminas generadas")
