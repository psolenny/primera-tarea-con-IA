# Tu primera tarea resuelta con IA

Sitio del workshop de 3 horas (versión 2, borrador): presentación, cuatro rutas con caso semilla y kit del participante.

Publicado con GitHub Pages desde la rama `main`, carpeta raíz.

## Qué hay

| Ruta | Contenido |
| --- | --- |
| `index.html` | Página del taller: método, rutas, agenda y kit. |
| `presentacion.html` | 24 láminas. Flechas para avanzar, `f` pantalla completa, `o` índice, `n` notas. |
| `rutas/` | Una página por ruta: fuentes, prompt CLARO, resultados esperados, trampa y vuelta 2. |
| `rutas/descargas/` | Las fuentes de cada caso en `.txt`. |
| `kit/` | Método, plantilla CLARO, semáforo de datos, rescate, plataformas y hoja del participante. |
| `scripts/` | Generador de las páginas y fuentes de los casos. |

## Cambiar el contenido

Las páginas HTML se generan. Edita los archivos de `scripts/` y vuelve a generar:

```
python3 scripts/build.py
```

- Casos y resultados esperados: `scripts/rutas.py` y `scripts/fuentes/`. Las cifras se calculan en el script.
- Láminas: `scripts/deck.py`.
- Páginas y kit: `scripts/paginas.py`.
- Fecha del taller: `FECHA` en `scripts/comun.py`.
- Enlace de inscripción: `FORMS_URL` en `scripts/paginas.py`.

Los estilos `assets/site.css`, `assets/deck.css` y `assets/deck.js` vienen del sitio de la charla «Pon la IA a trabajar por ti».

## Pendiente de revisar

- Todos los casos son ficticios. Los de Empleo y estudios, Emprendimiento, Cóctel Conecta y la minuta de la mudanza son borradores nuevos.
- Ningún caso se ha probado todavía en ChatGPT, Claude y Gemini con cuenta gratuita.
- La fecha del taller y el enlace de inscripción están sin definir.
