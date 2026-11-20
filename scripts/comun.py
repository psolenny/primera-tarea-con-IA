from html import escape as e

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">')
FIRMA = '<div class="firma"><b>Solenny Peralta</b><span>Gerente de Proyectos de Innovación y Servicios TI</span></div>'
MARQ = "· tu primera tarea resuelta con ia · mapear · pedir · verificar · corregir · guardar "
FECHA = "Fecha por anunciar"

KIT_TABS = [("index.html", "00", "Inicio"), ("metodo.html", "01", "Método"), ("claro.html", "02", "CLARO"),
            ("datos.html", "03", "Datos"), ("recuperacion.html", "04", "Rescate"),
            ("plataformas.html", "05", "Plataformas"), ("hoja.html", "06", "Hoja")]
RUTA_TABS = [("index.html", "00", "Rutas"), ("vida.html", "01", "Vida cotidiana"), ("trabajo.html", "02", "Trabajo"),
             ("empleo.html", "03", "Empleo y estudios"), ("emprendimiento.html", "04", "Emprendimiento")]

SCRIPT = """<script>
document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){
  var t=b.closest('.prompt').querySelector('pre').innerText;
  navigator.clipboard.writeText(t).then(function(){var o=b.textContent;b.textContent='¡copiado!';b.classList.add('ok');setTimeout(function(){b.textContent=o;b.classList.remove('ok');},1500);});
});});
</script>"""


def pagina(titulo, desc, cuerpo, raiz="", nav="", tabs=None, tab_on=""):
    def a(href, txt, clave):
        return f'<a href="{raiz}{href}"{" class=\"on\"" if nav == clave else ""}>{txt}</a>'
    t = ""
    if tabs:
        t = '<nav class="tabs" aria-label="Secciones"><div class="wrap">' + "".join(
            f'<a href="{h}" class="{"on" if h == tab_on else ""}"><span class="k">{k}</span>{n}</a>' for h, k, n in tabs) + "</div></nav>"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="{raiz}assets/logo-cecomsa-color.png">
{FONTS}
<link rel="stylesheet" href="{raiz}assets/site.css">
<link rel="stylesheet" href="{raiz}assets/taller.css">
</head>
<body>
<div class="marq" aria-hidden="true"><div class="marq-track"><span>{MARQ}</span><span>{MARQ}</span></div></div>
<header class="top"><div class="wrap">
  <a href="{raiz}index.html"><img src="{raiz}assets/logo-cecomsa-color.png" alt="CECOMSA"></a>
  <nav>{a("index.html", "El taller", "taller")}{a("presentacion.html", "Slides", "slides")}{a("rutas/index.html", "Rutas", "rutas")}{a("kit/index.html", "Kit", "kit")}</nav>
</div></header>
{t}
<main>
{cuerpo}
</main>
<footer class="foot"><div class="wrap">
  <img src="{raiz}assets/logo-cecomsa-color.png" alt="CECOMSA">
  {FIRMA}
</div></footer>
{SCRIPT}
</body>
</html>
"""


def hero(tag, h1, p, extra="", azul=False):
    return (f'<section class="hero{" azul" if azul else ""}"><div class="wrap">\n  <div class="tag">// {tag}</div>\n'
            f'  <h1>{h1}</h1>\n  <p>{p}</p>\n{extra}</div></section>')


def sec(inner, eyebrow="", h2="", lead="", id_=""):
    out = f'<section class="sec"{f" id=\"{id_}\"" if id_ else ""}><div class="wrap">\n'
    if eyebrow: out += f'  <div class="eyebrow">// {eyebrow}</div>\n'
    if h2: out += f'  <h2>{h2}</h2>\n'
    if lead: out += f'  <p class="lead">{lead}</p>\n'
    return out + inner + "\n</div></section>"


def prompt(n, titulo, texto, boton="copiar"):
    return (f'<div class="prompt"><div class="prompt-head"><span class="prompt-n">{n}</span><span class="prompt-t">{titulo}</span>'
            f'<button class="copy" type="button">{boton}</button></div><pre>{e(texto)}</pre></div>')


def tabla(filas, cab=("Qué", "Resultado esperado")):
    return ('<div class="scroll"><table class="tbl"><tr>' + "".join(f"<th>{c}</th>" for c in cab) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{e(str(c))}</td>" for c in f) + "</tr>" for f in filas) + "</table></div>")


def plegable(titulo, inner, clase=""):
    return f'<details class="pleg {clase}"><summary>{titulo}</summary><div class="pleg-in">{inner}</div></details>'


def pager(prev=None, nxt=None):
    out = '<div class="pager">'
    out += f'<a class="chip" href="{prev[0]}">← {prev[1]}</a>' if prev else "<span></span>"
    out += f'<a class="chip p" href="{nxt[0]}">{nxt[1]} →</a>' if nxt else ""
    return out + "</div>"
