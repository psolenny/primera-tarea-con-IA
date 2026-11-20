from comun import FONTS, FIRMA, FECHA
from rutas import RUTAS, _combos, _ref, rd


def s(clase, eyebrow, cuerpo, notas):
    return (f'<section class="slide{(" " + clase) if clase else ""}">\n  <div class="eyebrow">// {eyebrow}</div>\n{cuerpo}\n'
            f'  <div class="notes">{notas}</div>\n</section>')


def stack(filas, w=None):
    return (f'  <div class="stack"{f" style=\"--w:{w}\"" if w else ""}>\n'
            + "<br>\n".join(f'    <span class="lbl">{a}</span><span class="val">{b}</span>' for a, b in filas) + "\n  </div>")


def steps(items):
    return '  <div class="loop">\n' + "\n".join(
        f'    <div class="step{(" " + c) if c else ""}"><span class="n">{n}</span><h3>{h}</h3><p>{p}</p></div>' for c, n, h, p in items) + "\n  </div>"


def terms(items):
    return '  <div class="terms">\n' + "\n".join(f'    <div class="term"><span class="t">{t}</span><span class="d">{d}</span></div>' for t, d in items) + "\n  </div>"


filas_combo = "".join(f"<tr><td>{k}</td><td>{rd(v)}</td><td>{rd(18000 - v)}</td></tr>" for k, v in _combos.items())

SLIDES = [
    s("azul", "workshop · 3 horas · 100% práctico",
      '  <h1>Tu primera tarea<br>resuelta con <span class="hl">IA</span>.</h1>\n  <p class="sub wide">De principio a fin.</p>\n  ' + FIRMA,
      "⏱ 0–10 · APERTURA\nBienvenida. La meta: cada persona sale con un caso resuelto y verificado, un segundo resultado y su plantilla de prompt guardada. Todos los casos del kit son ficticios. El taller admite ChatGPT, Claude y Gemini; no prometer resultados idénticos ni límites de uso iguales."),
    s("", "quién te acompaña",
      '  <h2>Soy Solenny Peralta.<br>Puedes llamarme <span class="hl">Sole</span>.</h2>\n'
      + stack([("trabajo", "Proyectos de Innovación y Servicios TI en CECOMSA"), ("enfoque", "sistemas, proyectos y gestión del cambio"), ("comunidad", "PythonSDQ y PyLadiesSDQ")], "6.5em")
      + '\n  <p class="sub wide">Me interesa lo que pasa después de implementar: <strong>¿la gente lo usa?</strong></p>',
      "Presentación breve. Conectar gestionar el cambio con aprender a usar una herramienta."),
    s("pop", "sondeo · a mano alzada",
      '  <h2>¿En cuál <span class="hl">ruta</span> te ves?</h2>\n  <div class="poll">\n'
      + "\n".join(f'    <div class="opt"><span class="k">{"ABCD"[i]}</span><span><strong>{r["nombre"]}.</strong> {r["para"]}</span></div>' for i, r in enumerate(RUTAS))
      + '\n  </div>\n  <p class="sub wide">No necesitas traer una tarea ni tener empleo. <strong>Siéntate con tu ruta.</strong></p>',
      "SONDEO Y MESAS (3 min). Mano alzada por ruta y reubicar: una mesa por ruta. Si una ruta queda con una sola persona, que elija entre quedarse o sumarse a otra. Preguntar también quién vino a la charla y quién trae una tarea propia: esa gente la usará en la vuelta 2.\nSi alguien duda: Vida cotidiana, que es la ruta de la demo."),
    s("", "lo que te llevas",
      '  <h2>Tres cosas, <span class="hl">hoy</span>.</h2>\n'
      + steps([("", "vuelta 1", "Un caso resuelto y verificado", "Con una respuesta correcta contra la cual comprobar."),
               ("inv", "vuelta 2", "Un segundo resultado", "Tu caso propio, otro caso del kit o una herramienta."),
               ("", "para después", "Tu plantilla guardada", "El prompt que funcionó, listo para repetirlo.")])
      + '\n  <p class="sub wide">El tiempo de <strong>revisión</strong> forma parte del trabajo con IA.</p>',
      "Criterio de terminado por persona: 1) un dato verificado y la trampa detectada en la vuelta 1; 2) un segundo resultado verificado; 3) la plantilla guardada. Sin puntuaciones."),
    s("", "nuestra ruta · 180 min",
      '  <h2>Dos demos, <span class="hl">dos vueltas</span>.</h2>\n'
      + terms([("0–25 · criterio", "Qué pedir, qué aceptar, qué datos usar."), ("25–45 · demo 1", "Los 5 pasos con un caso completo."),
               ("45–85 · vuelta 1", "El caso semilla de tu ruta."), ("85–95 · pausa", "Diez minutos."),
               ("95–145 · demo 2 y vuelta 2", "Tu caso, otro caso o una herramienta."), ("145–180 · guardar y demos", "Tu plantilla y una demo por ruta.")]),
      "Mostrar la ruta y los tres hitos: H1 dato verificado y trampa detectada; H2 segundo resultado; H3 plantilla guardada."),
    s("dark", "si vienes de la charla, ya lo sabes",
      '  <h2>Contexto.<br>Especificidad.<br><span class="hl">Verificación.</span></h2>\n'
      '  <ol class="big"><li><strong>La IA no busca la verdad.</strong> Predice la respuesta más probable.</li><li><strong>Cuando le falta contexto, completa con supuestos.</strong> Sin avisar.</li></ol>',
      "⏱ 10–25 · CRITERIO Y DATOS\nRecap de 2 min. No repetir las demos de la charla (CV, bot). Quien no vino a la charla recibe aquí lo mínimo: una respuesta convincente todavía necesita comprobación."),
    s("", "el hábito de criterio",
      '  <h2>Saber qué pedir, qué aceptar<br>y qué <span class="hl">descartar</span>.</h2>\n'
      + stack([("antes", "escribe qué debe salir"), ("antes", "anota 2 o 3 cosas que vas a revisar"), ("después", "compara, corrige y decide tú")], "5.5em")
      + '\n  <p class="sub wide">Si no puedes escribir qué vas a revisar, <strong>todavía no pidas</strong>.</p>',
      "El hábito se practica en la hoja, paso 1. Es lo que diferencia usar la IA de dejar que la IA decida."),
    s("", "datos · antes de pegar algo",
      '  <h2>El <span class="hl">semáforo</span> de datos.</h2>\n'
      + steps([("", "verde · sí", "Adelante", "Datos ficticios, información pública, tus propios borradores."),
               ("", "amarillo · con cuidado", "Primero límpialo", "Tu CV sin cédula ni dirección. Datos de otras personas, sin nombres. Datos de tu empresa, solo si está autorizado."),
               ("rosa", "rojo · nunca", "No lo pegues", "Contraseñas, cédulas, tarjetas, cuentas y datos privados de otras personas.")])
      + '\n  <p class="sub wide">Hoy los casos son ficticios. El semáforo es para <strong>tu caso propio</strong>.</p>',
      "QUIZ EN VOZ ALTA (3 min):\n1) Pegar la lista de precios de mi negocio → verde: es tuya.\n2) Pegar mi currículum con cédula y dirección → amarillo: quita cédula y dirección.\n3) Pegar el Excel de clientes de la empresa con teléfonos → no sin autorización; si está autorizado, anonimiza.\nNo convertirlo en charla jurídica."),
    s("", "un solo marco de prompt",
      '  <h2>Pídelo <span class="hl">CLARO</span>.</h2>\n'
      + stack([("C", "Contexto · quién eres, para quién es, qué pasa"), ("L", "Lo que necesitas · la tarea, con un verbo claro"),
               ("A", "Archivos · las fuentes que le entregas"), ("R", "Resultado · el formato que quieres"), ("O", "Omite · qué no hacer")], "2.2em")
      + '\n  <p class="sub wide">Escríbelo como para una persona inteligente que <strong>empezó hoy</strong>.</p>',
      "Si aprendieron las 6 partes en la charla: es lo mismo con otros nombres. El criterio de calidad pasa al hábito de la lámina anterior. La plantilla está en el kit, pieza 02."),
    s("", "el método",
      '  <h2>Cinco pasos, <span class="hl">dos vueltas</span>.</h2>\n'
      + stack([("1 mapear", "qué entra, qué sale, qué reviso"), ("2 pedir", "con CLARO y las fuentes"), ("3 verificar", "contra resultados esperados"),
               ("4 corregir", "un cambio concreto"), ("5 guardar", "el prompt que funcionó")], "7em"),
      "⏱ 25–45 · DEMO 1\nPresentar los cinco pasos antes de abrir la IA. Se repiten iguales en las cuatro rutas."),
    s("pop", "demo 1 · en vivo · 15 min",
      '  <h2>El lanzamiento de<br><span class="hl">Brisa Mini</span>.</h2>\n'
      + stack([("30", "asistentes"), ("RD$18,000", "presupuesto máximo"), ("2 × 2", "lugares y refrigerios para comparar")], "7em")
      + '\n  <p class="sub wide">Ruta Vida cotidiana. Todo es ficticio: nombres, precios y condiciones.</p>',
      "DEMO EN VIVO, 15 min. Abrir rutas/vida.html.\n1) Mapear (2 min): leer qué debe salir y qué voy a revisar.\n2) Pedir (4 min): copiar el prompt CLARO y pegar las fuentes debajo. Pedir que liste las fuentes leídas.\n3) Verificar (5 min): comparar los cuatro totales con los resultados esperados.\n4) Corregir (2 min): si falló el mínimo de R2, usar la frase del kit. Si acertó, comprobarlo y decirlo: no inventar un fallo.\n5) Guardar (2 min): copiar el prompt a un archivo de texto.\nNo enviar ni reservar nada."),
    s("", "paso 3 · verificar",
      '  <h2>El presupuesto tiene que <span class="hl">cuadrar</span>.</h2>\n'
      f'  <table class="tbl"><tr><th>combinación</th><th>total conocido</th><th>margen contra RD$18,000</th></tr>{filas_combo}</table>\n'
      f'  <p class="sub wide">R2 cobra menos por persona, pero factura un <strong>mínimo de 40</strong>: {rd(_ref["R2"])} contra {rd(_ref["R1"])} de R1.</p>',
      "Derivación: L1 = 4,500 + 1,500 de audio. L2 = 7,000 con audio incluido. Extras B1 = 1,000 + 500. R1 = 30 × 250 + 500. R2 = 40 × 200 + 900.\nSon totales de costos conocidos, no definitivos: falta el transporte del expositor."),
    s("dark", "paso 3 · verificar",
      '  <h2>Lo que falta<br>sigue <span class="hl">pendiente</span>.</h2>\n'
      + stack([("lugar", "disponibilidad sin confirmar"), ("expositor", "transporte sin precio · solo 17:20 a 18:00"), ("producto", "precio de venta sin aprobar")], "6em")
      + '\n  <p class="sub wide">Una sugerencia de la IA todavía no es una <strong>decisión aprobada</strong>.</p>',
      "Si la IA puso el transporte en cero o dio la sala por disponible, señalarlo en vivo. La agenda debe sumar 120 minutos y respetar la ventana del expositor. Al terminar: 5 min para que cada mesa abra el kit de su ruta."),
    s("", "tu turno · abre tu ruta",
      '  <h2>Mismo método,<br>cuatro <span class="hl">casos</span>.</h2>\n'
      + terms([(f'{r["n"]} · {r["nombre"].lower()}', f'{r["caso"]}. {r["resumen"]}') for r in RUTAS]),
      "Cada mesa abre rutas/ y entra a su ruta. Confirmar que todos ven las fuentes y el prompt antes de arrancar el cronómetro."),
    s("pop", "vuelta 1 · 40 minutos",
      '  <h2>Tu <span class="hl">caso semilla</span>.</h2>\n'
      + steps([("", "primeros 10 min", "Mapear y pedir", "Llena el paso 1 de tu hoja. Pega el prompt y las fuentes."),
               ("", "siguientes 15 min", "Obtener", "Consigue el entregable completo. Pide que liste las fuentes leídas."),
               ("", "últimos 15 min", "Verificar y corregir", "Abre los resultados esperados. Busca la trampa. Pide una corrección.")])
      + '\n  <p class="sub wide"><strong>Hito 1:</strong> un dato comprobado y la trampa detectada, anotados en tu hoja.</p>',
      "⏱ 45–85 · VUELTA 1\nCronómetro visible. Recorrer las mesas en orden. A los 25 min avisar: \"abran los resultados esperados\".\nTrampas por ruta: Vida, el mínimo de R2 y los pendientes. Trabajo, la fecha de cierre de mes que nadie dio. Empleo, experiencia inventada. Emprendimiento, la mano de obra omitida.\nSi a alguien la IA le acertó todo: que lo compruebe y lo diga. No se inventa un fallo."),
    s("azul", "pausa",
      '  <h2>Diez <span class="hl">minutos</span>.</h2>\n  <p class="sub wide">Al volver: cómo convertir lo que hiciste en algo que puedas repetir.</p>',
      "⏱ 85–95 · PAUSA\nDejar abierto el caso de la demo para la demo 2."),
    s("", "demo 2 · 10 min",
      '  <h2>De resultado a <span class="hl">reutilizable</span>.</h2>\n'
      + steps([("", "plantilla", "Guarda el prompt", "Cambia los datos del caso por espacios entre corchetes. Sirve en cualquier cuenta."),
               ("inv", "herramienta", "Vibe coding ligero", "Describes una función en lenguaje cotidiano. La IA propone código y tú pruebas el resultado.")])
      + '\n  <p class="sub wide">Que abra en el navegador <strong>no demuestra</strong> que sea correcto ni seguro.</p>',
      "⏱ 95–105 · DEMO 2 PARA TODA LA SALA\n1) Plantilla (3 min): tomar el prompt de Brisa Mini y reemplazar evento, asistentes y presupuesto por corchetes.\n2) Herramienta (7 min): pegar el prompt de la opción C de la ruta Vida. Abrir el HTML, cambiar asistentes a 40 y mostrar que el total llega justo a RD$18,000 y que la capacidad de L1 se excede por 5.\nLímites: un único HTML, sin login, pagos, base de datos ni conexiones. Es un prototipo para explorar, no un sistema para usuarios reales. Si falla dos veces, seguir con la plantilla."),
    s("pop", "vuelta 2 · 40 minutos",
      '  <h2>Ahora <span class="hl">eliges tú</span>.</h2>\n'
      + steps([("", "opción a", "Tu caso propio", "Algo tuyo, con los mismos cinco pasos. Revisa el semáforo."),
               ("", "opción b", "El segundo caso", "Otro caso de tu ruta, con resultados esperados."),
               ("", "opción c", "Una herramienta", "Convierte tu resultado en algo que se abre en el navegador.")])
      + '\n  <p class="sub wide">Las tres valen igual. <strong>Hito 2:</strong> un segundo resultado verificado.</p>',
      "⏱ 105–145 · VUELTA 2\nDar 2 minutos para elegir. Quien no decida: opción B. Quien elige la A llena primero el mini mapa de la hoja y revisa el semáforo. Si su caso tiene datos rojos: datos inventados parecidos u opción B.\nNadie queda sin material: las opciones B y C están completas en la página de cada ruta."),
    s("", "minuto 20 · chequeo",
      '  <h2>“Hazlo mejor”<br><span class="hl">no sirve</span>.</h2>\n'
      + stack([("qué", "“el total de la fila 2 no cuadra”"), ("dónde", "“corrige solo esa fila”"), ("cómo", "“muéstrame la suma paso a paso”")], "4.5em")
      + '\n  <p class="sub wide">Si tu caso es muy grande, quédate con <strong>un solo paso</strong> y termínalo.</p>',
      "CHEQUEO A LOS 20 MIN. Preguntar mesa por mesa: ¿ya tienes un primer resultado? Quien no lo tenga reduce el alcance a un solo entregable. Recordar las frases del kit, pieza 01."),
    s("dark", "antes de darlo por bueno",
      '  <h2>¿Lo usarías<br><span class="hl">tal cual</span>?</h2>\n'
      '  <ol class="big"><li><strong>¿Qué le falta</strong> para enviarlo o usarlo?</li><li><strong>¿Qué descartaste</strong> de lo que propuso la IA, y por qué?</li></ol>',
      "La medida no es solo el tiempo. Para una tarea que se hace una vez (un CV, una cotización) la pregunta es si el resultado se puede usar. Quien tenga una tarea repetitiva puede estimar el tiempo antes y con IA: es una estimación; la medición real sale del registro de dos semanas."),
    s("", "paso 5 · guardar · 10 min",
      '  <h2>Que te sirva<br><span class="hl">otra vez</span>.</h2>\n'
      + stack([("plantilla", "tu prompt con [corchetes], en un .txt"), ("proyecto", "solo si tu cuenta lo permite"), ("herramienta", "guarda el .html antes de cambiarlo")], "8em")
      + '\n  <p class="sub wide"><strong>Hito 3:</strong> tu plantilla guardada y anotado dónde.</p>',
      "⏱ 145–155 · GUARDAR\nEl archivo de texto funciona en cualquier plan. Proyectos, Gems o instrucciones personalizadas son opcionales y dependen de cada cuenta.\nCuándo la IA no es la herramienta: cálculo exacto y repetitivo, hoja de cálculo; reglas fijas, automatización; decisiones legales o sobre personas, la persona decide."),
    s("pop", "demos por ruta · 3 min cada una",
      '  <h2>Muéstranos tu <span class="hl">criterio</span>.</h2>\n'
      + stack([("1", "qué resolviste"), ("2", "qué verificaste y cómo"), ("3", "qué descartaste de la IA")], "2em")
      + '\n  <p class="sub wide">Después, cuéntaselo a tu mesa en un minuto.</p>',
      "⏱ 155–172 · DEMOS\nUna persona voluntaria por ruta, 3 minutos. Luego demo cruzada dentro de cada mesa. Reconocer en voz alta a quien rechazó y rehízo algo que propuso la IA."),
    s("", "cierre",
      '  <h2>Lo que hiciste hoy<br>debe servirte <span class="hl">mañana</span>.</h2>\n'
      + stack([("dónde", "¿en qué lo usarás esta semana?"), ("qué falta", "¿qué necesitas para dar ese paso?"), ("registro", "anota tus usos durante dos semanas")], "6em"),
      "⏱ 172–180 · CIERRE\nDos o tres respuestas en voz alta. Aceptar \"todavía no sé\" y \"necesito apoyo\". Recordar el segundo caso de cada ruta para practicar en casa.\nPróximos talleres: preguntar a mano alzada qué tarea concreta les gustaría resolver."),
    s("dark", "gracias",
      '  <h2>Pide claro.<br>Verifica <span class="hl">siempre</span>.</h2>\n  <p class="sub wide">El kit y las cuatro rutas quedan abiertos para que repitas el método.</p>\n  ' + FIRMA,
      "Dejarla en pantalla mientras la gente sale. Si hay encuesta de satisfacción, agregar aquí el código QR."),
]

DECK = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tu primera tarea resuelta con IA · slides</title>
<link rel="icon" href="assets/logo-cecomsa-color.png">
{FONTS}
<link rel="stylesheet" href="assets/deck.css">
<style>.pop .stack .lbl{{color:var(--negro);}} .step.rosa h3{{color:var(--negro);}}</style>
</head>
<body>

{chr(10).join(f"<!-- {i} -->{chr(10)}{x}{chr(10)}" for i, x in enumerate(SLIDES, 1))}
<img id="logo" class="logo" alt="CECOMSA" data-color="assets/logo-cecomsa-color.png" data-blanco="assets/logo-cecomsa-blanco.png" src="assets/logo-cecomsa-color.png">
<div class="bar" id="bar"></div>
<div class="num" id="num"></div>
<a class="home" id="home" href="index.html">← el taller</a>
<div class="hint" id="hint">← → espacio · f pantalla completa · o índice · n notas</div>
<div id="ov"><h3>Índice · clic para saltar (o / esc para cerrar)</h3><ol id="ovl"></ol></div>
<aside id="np"><h4>Notas del presentador</h4><p id="npt"></p></aside>

<script src="assets/deck.js"></script>
</body>
</html>
"""
