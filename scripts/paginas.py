from comun import *
from rutas import RUTAS

PASOS = [("Mapear", "Qué entra, qué debe salir y qué vas a revisar antes de aceptarlo."),
         ("Pedir", "Con el marco CLARO y las fuentes pegadas en el mensaje."),
         ("Verificar", "Contra la hoja de resultados esperados, número por número."),
         ("Corregir", "Un pedido concreto: qué está mal y dónde. Nunca \"hazlo mejor\"."),
         ("Guardar", "El prompt que funcionó, como plantilla para la próxima vez.")]

AGENDA = [("0–10", "Apertura", "Qué te llevas y sondeo por ruta. Te sientas con tu mesa."),
          ("10–25", "Criterio y datos", "El hábito de criterio, el semáforo de datos y el marco CLARO."),
          ("25–45", "Demo 1", "Los 5 pasos de punta a punta con el caso Brisa Mini. Abres el kit de tu ruta."),
          ("45–85", "Vuelta 1 · caso semilla", "Resuelves el caso ficticio de tu ruta y lo verificas contra los resultados esperados."),
          ("85–95", "Pausa", "Diez minutos."),
          ("95–105", "Demo 2", "De resultado a reutilizable: plantilla de prompt y herramienta sencilla."),
          ("105–145", "Vuelta 2 · tú eliges", "Tu caso propio, el segundo caso del kit o una herramienta. Chequeo a los 20 minutos."),
          ("145–155", "Guardar", "Dejas tu plantilla de prompt guardada."),
          ("155–172", "Demos por ruta", "Una persona por ruta muestra qué resolvió, qué verificó y qué descartó."),
          ("172–180", "Cierre", "Dónde lo usarás esta semana.")]


def index():
    pasos = "".join(f'<div class="box"><span class="n">paso {i}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PASOS, 1))
    rutas = "".join(f'<a class="box{" negro" if i == 1 else ""}" href="rutas/{r["slug"]}.html"><span class="n">ruta {r["n"]}</span><h3>{r["nombre"]}</h3>'
                    f'<p{" style=\"color:rgba(255,255,255,.85)\"" if i == 1 else ""}>{r["para"]} Caso: {r["caso"]}.</p></a>' for i, r in enumerate(RUTAS))
    agenda = tabla(AGENDA, ("Min", "Bloque", "Qué pasa"))
    cuerpo = hero("workshop · 3 horas · 100% práctico",
                  'Tu primera tarea<br>resuelta con <span class="hl">IA</span>.',
                  "De principio a fin. No necesitas traer una tarea ni tener empleo: eliges una ruta, resuelves un caso con respuesta conocida y después lo repites con algo tuyo.",
                  f'''  <div class="meta">
    <a class="chip p" href="presentacion.html">▶ ver la presentación</a>
    <a class="chip" href="rutas/index.html">elige tu ruta →</a>
    <a class="chip" href="kit/index.html">kit del participante →</a>
  </div>
  {FIRMA}
''', azul=True)
    cuerpo += sec(f'<div class="grid g3">{pasos}<a class="box azul" href="kit/metodo.html"><span class="n">// kit</span><h3>Ver el método completo →</h3><p>Con las frases para corregir.</p></a></div>',
                  "el método", "Cinco pasos, dos vueltas.", "Primero con un caso que tiene respuesta correcta. Después con el tuyo.")
    cuerpo += sec(f'<div class="grid g2">{rutas}</div>', "cuatro rutas", "Elige por situación, no por cargo.",
                  "Cada ruta trae su caso, su prompt, sus resultados esperados y una trampa que te enseña a verificar.", "rutas")
    cuerpo += '<section class="band"><div class="wrap"><p class="quote">Una respuesta <em>convincente</em> todavía necesita <em>comprobación</em>. Una sugerencia de la IA no es una <em>decisión</em>.</p></div></section>'
    cuerpo += sec(agenda, "180 minutos", "La agenda.", "Ochenta minutos de práctica en dos vueltas de cuarenta.", "agenda")
    kit = "".join(f'<a class="box" href="kit/{h}"><span class="n">{k}</span><h3>{n}</h3></a>' for h, k, n in KIT_TABS[1:])
    cuerpo += sec(f'<div class="grid g3">{kit}</div>', "llévatelo", "El kit del participante.",
                  "Seis piezas comunes a todas las rutas. Los casos están en cada ruta.", "kit")
    return pagina("Tu primera tarea resuelta con IA · Workshop", "Taller práctico de 3 horas: eliges una ruta, resuelves un caso con IA de principio a fin y lo repites con algo tuyo.",
                  cuerpo, nav="taller")


# ---------- rutas ----------
def rutas_index():
    cajas = "".join(f'<a class="box" href="{r["slug"]}.html"><span class="n">ruta {r["n"]} · {r["caso"]}</span><h3>{r["nombre"]}</h3><p>{r["para"]}</p><p style="margin-top:8px">{r["resumen"]}</p></a>' for r in RUTAS)
    cuerpo = hero("rutas · elige una", "Elige tu ruta", "Las cuatro usan el mismo método. Cambia el caso. Elige la situación que más se parece a lo que quieres resolver después.")
    cuerpo += sec(f'<div class="grid g2">{cajas}</div>')
    cuerpo += sec('''<div class="grid g3">
  <div class="box"><span class="n">vuelta 1 · 40 min</span><h3>Caso semilla</h3><p>El caso ficticio de tu ruta. Tiene respuesta correcta, así que puedes comprobar sola o solo si la IA acertó.</p></div>
  <div class="box"><span class="n">vuelta 2 · 40 min</span><h3>Tú eliges</h3><p>A) tu caso propio, B) el segundo caso del kit, o C) convertir tu resultado en una herramienta. Las tres opciones valen igual.</p></div>
  <div class="box soft"><span class="n">si te atrasas</span><h3>Rescate</h3><p>Cada ruta trae sus resultados esperados. Si tu cuenta se agota, sigue verificando con ellos. <a href="../kit/recuperacion.html">Guía de rescate →</a></p></div>
</div>''', "cómo se usa cada ruta")
    return pagina("Rutas · Tu primera tarea resuelta con IA", "Cuatro rutas con caso, prompt y resultados esperados.", cuerpo, raiz="../", nav="rutas", tabs=RUTA_TABS, tab_on="index.html")


def ruta(r, i):
    lis = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    c = hero(f'ruta {r["n"]} de 04 · caso semilla: {r["caso"]}', r["nombre"], r["para"] + " " + r["resumen"])
    c += sec(f'''<div class="grid g2" style="align-items:start">
  <div class="box"><span class="n">qué debe salir</span><p>{r["entregable"]}</p></div>
  <div class="box azul"><span class="n">// qué vas a revisar antes de aceptarlo</span><ul class="check" style="margin-top:10px">{lis(r["reviso"])}</ul></div>
</div>''', "paso 1 · mapear", "Antes de pedir.", "Escríbelo en tu hoja. Si no sabes qué vas a revisar, todavía no pidas.")
    c += sec(prompt("fuentes", "Las fuentes del caso", r["fuente"], "copiar fuentes")
             + f'<p style="margin:-8px 0 26px"><a class="chip" href="descargas/{r["archivo"]}" download>↓ descargar como .txt</a></p>'
             + prompt("prompt", "Tu pedido en formato CLARO", r["prompt"], "copiar prompt")
             + '<p class="lead" style="margin-top:8px">Pega primero el prompt y debajo las fuentes, en el mismo mensaje. Si tu cuenta permite adjuntar archivos, puedes adjuntar el .txt.</p>',
             "paso 2 · pedir", "El caso y el pedido.")
    c += sec(plegable("Ver los resultados esperados", tabla(r["esperados"]))
             + plegable("Ver la trampa de este caso", f'<p>{e(r["trampa"])}</p>', "rosa")
             + '<p class="lead" style="margin-top:18px">Ábrelos después de tener tu respuesta, no antes. Marca en tu hoja un dato que comprobaste y la trampa que encontraste.</p>',
             "paso 3 · verificar", "¿Cuadra?")
    c += sec(f'<div class="phr"><b>ejemplo de corrección para este caso</b><q>{e(r["corrige"])}</q><small>Di qué está mal, dónde, y pide cambiar solo eso. <a href="../kit/metodo.html#frases">Más frases →</a></small></div>',
             "paso 4 · corregir", "Pide el cambio exacto.")
    c += sec('<div class="box soft"><p>Copia el prompt que te funcionó a un archivo de texto o a tus notas. Cambia los datos del caso por espacios entre corchetes, por ejemplo <b>[evento]</b> o <b>[presupuesto]</b>. Esa es tu plantilla. Si tu cuenta tiene proyectos o instrucciones personalizadas, puedes guardarla ahí.</p></div>',
             "paso 5 · guardar", "Que te sirva otra vez.")
    c += sec(f'''<div class="grid g3" style="align-items:start">
  <div class="box"><span class="n">opción a</span><h3>Tu caso propio</h3><p>Mismos cinco pasos, con algo tuyo. Ideas:</p><ul class="lista">{lis(r["ideas"])}</ul><p style="margin-top:10px"><a href="../kit/datos.html">Revisa el semáforo de datos →</a></p></div>
  <div class="box"><span class="n">opción b</span><h3>{r["b_titulo"]}</h3><p>El segundo caso de esta ruta. {r["b_pide"]}</p></div>
  <div class="box"><span class="n">opción c</span><h3>Una herramienta</h3><p>Convierte lo que resolviste en algo que puedas abrir y reutilizar en el navegador.</p></div>
</div>''', "vuelta 2 · 40 min", "Ahora eliges tú.", "Las tres opciones valen igual. A los 20 minutos, revisa cómo vas.", "vuelta2")
    c += sec(prompt("opción b", f'Fuentes de {r["b_titulo"]}', r["b_fuente"], "copiar fuentes")
             + f'<p style="margin:-8px 0 20px"><a class="chip" href="descargas/{r["b_archivo"]}" download>↓ descargar como .txt</a></p>'
             + plegable(f'Resultados esperados de {r["b_titulo"]}', tabla(r["b_esperados"]))
             + plegable("Ver la trampa", f'<p>{e(r["b_trampa"])}</p>', "rosa")
             + '<div style="height:26px"></div>'
             + prompt("opción c", "Prompt para la herramienta", r["herramienta"], "copiar prompt")
             + '<div class="box soft"><span class="n">antes de confiar en la herramienta</span><p>Que abra en el navegador no demuestra que calcule bien. Prueba los tres casos que te dio la IA y uno con un dato inválido. Es un prototipo para explorar con datos ficticios, no un sistema para usuarios reales.</p></div>')
    prev = (RUTA_TABS[i][0], RUTA_TABS[i][2])
    nxt = (RUTA_TABS[i + 2][0], RUTA_TABS[i + 2][2]) if i + 2 < len(RUTA_TABS) else ("../kit/index.html", "Kit")
    c = c[:-len("</div></section>")] + pager(prev, nxt) + "</div></section>"
    return pagina(f'{r["nombre"]} · Ruta {r["n"]}', r["para"], c, raiz="../", nav="rutas", tabs=RUTA_TABS, tab_on=r["slug"] + ".html")


# ---------- kit ----------
def kit(nombre, titulo, desc, cuerpo):
    i = [t[0] for t in KIT_TABS].index(nombre)
    prev = (KIT_TABS[i - 1][0], KIT_TABS[i - 1][2]) if i else None
    nxt = (KIT_TABS[i + 1][0], KIT_TABS[i + 1][2]) if i + 1 < len(KIT_TABS) else ("../rutas/index.html", "Rutas")
    cuerpo = cuerpo.rstrip()
    assert cuerpo.endswith("</div></section>")
    cuerpo = cuerpo[:-len("</div></section>")] + pager(prev, nxt) + "</div></section>"
    return pagina(f"{titulo} · Kit del participante", desc, cuerpo, raiz="../", nav="kit", tabs=KIT_TABS, tab_on=nombre)


def kit_index():
    piezas = [("metodo.html", "01", "Método", "Los cinco pasos y las frases para corregir."),
              ("claro.html", "02", "Plantilla CLARO", "El marco de prompt, para llenar, con un ejemplo."),
              ("datos.html", "03", "Semáforo de datos", "Qué puedes pegar en una IA y qué no."),
              ("recuperacion.html", "04", "Rescate", "Qué hacer si te atascas o se agota tu cuenta."),
              ("plataformas.html", "05", "Plataformas", "ChatGPT, Claude o Gemini: la misma ruta."),
              ("hoja.html", "06", "Hoja del participante", "Para imprimir y llenar durante el taller.")]
    cajas = "".join(f'<a class="box" href="{h}"><span class="n">{k}</span><h3>{n}</h3><p>{d}</p></a>' for h, k, n, d in piezas)
    c = hero("kit del participante", "El kit", "Seis piezas comunes a todas las rutas. Los casos, los prompts y los resultados esperados están en cada ruta.",
             '  <div class="meta"><a class="chip p" href="../rutas/index.html">ir a las rutas →</a></div>\n')
    c += sec(f'<div class="grid g3">{cajas}</div>')
    return kit("index.html", "Kit", "Kit del participante del taller.", c)


def kit_metodo():
    filas = "".join(f'<div class="box"><span class="n">paso {i}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PASOS, 1))
    frases = [("largo", "Déjalo en tres párrafos y pon la fecha en el primero.", "Di cuánto y qué va primero."),
              ("tono", "Escríbelo como se lo dirías a un colega, sin frases de cortesía largas.", "Compara con alguien concreto."),
              ("falta algo", "Falta el costo del transporte. Agrégalo en la tabla y recalcula el total.", "Di qué falta y dónde va."),
              ("un número no cuadra", "El total de la fila 2 no cuadra. Muéstrame la suma paso a paso y corrige solo esa fila.", "Pide la operación, no solo el resultado."),
              ("inventó algo", "Ese dato no está en las fuentes. Quítalo y márcalo como pendiente.", "Lo que no está en las fuentes no existe."),
              ("antes de asumir", "Si te falta información para responder, pregúntame antes de suponer.", "Sirve al principio de cualquier pedido."),
              ("opciones", "Dame dos versiones: una formal y una más cercana.", "Elegir es más fácil que describir.")]
    fr = "".join(f'<div class="phr"><b>{a}</b><q>{b}</q><small>{c}</small></div>' for a, b, c in frases)
    c = hero("kit · pieza 01 de 06", "El método", "Cinco pasos que se repiten en todas las rutas. En el taller los recorres dos veces.")
    c += sec(f'<div class="grid g3">{filas}<div class="box azul"><span class="n">// el hábito de criterio</span><p>Antes de pedir, escribe qué debe salir y dos o tres cosas que vas a revisar. Si no puedes escribirlo, todavía no sabes qué pedir.</p></div></div>')
    c += sec(fr, "paso 4 · corregir", "Frases que funcionan.", "\"Hazlo mejor\" no dice qué está mal ni cómo se ve bien. La IA adivina y cambia cosas al azar.", "frases")
    c += sec('''<div class="grid g2">
  <div class="box"><span class="n">¿lo usarías tal cual?</span><h3>La pregunta de cierre</h3><p>No midas solo el tiempo. Pregúntate: ¿enviaría esto así?, ¿qué le falta?, ¿qué descarté de lo que propuso la IA y por qué?</p></div>
  <div class="box soft"><span class="n">cuándo no usar ia</span><h3>La herramienta equivocada</h3><p>Cálculo exacto y repetitivo: una hoja de cálculo. Reglas fijas: una automatización. Decisiones legales o sobre personas: la IA asiste, tú decides.</p></div>
</div>''', "después de verificar")
    return kit("metodo.html", "Método", "Los cinco pasos del taller y las frases para corregir.", c)


def kit_claro():
    campos = [("C", "Contexto", "Quién eres, para quién es, qué pasa.", "Soy… / Esto es para… / La situación es…"),
              ("L", "Lo que necesitas", "La tarea, con un verbo claro.", "Compara / Resume / Redacta / Calcula…"),
              ("A", "Archivos", "Las fuentes o datos que le entregas.", "Usa solo estas fuentes… / Dime qué leíste antes de empezar."),
              ("R", "Resultado", "El formato: tabla, correo, una página.", "Una tabla con… / Máximo … palabras."),
              ("O", "Omite", "Qué no hacer: límites, tono, lo prohibido.", "No inventes… / Lo que falte va como pendiente.")]
    f = "".join(f'<div class="field"><div class="fh"><b>{l}</b><span>{n}</span><small>{d}</small></div><textarea placeholder="{p}" aria-label="{n}"></textarea></div>' for l, n, d, p in campos)
    c = hero("kit · pieza 02 de 06", "Plantilla CLARO", "El marco de prompt del taller. Cinco piezas: mientras más importante la tarea, más conviene llenarlas todas.")
    c += sec(f'''<div class="grid g2" style="align-items:start">
  <div>{f}</div>
  <div><div class="box azul"><span class="n">// ejemplo resuelto</span><p style="font-size:15.5px;line-height:1.6"><span style="color:#E31C79">[Contexto]</span> Estoy organizando un evento ficticio para 30 personas con un presupuesto máximo de RD$18,000. <span style="color:#E31C79">[Lo que necesito]</span> Compara las cuatro combinaciones de lugar y refrigerio y recomienda una. <span style="color:#E31C79">[Archivos]</span> Usa solo las fuentes que pego debajo y dime cuáles leíste. <span style="color:#E31C79">[Resultado]</span> Una tabla con el total de cada combinación y de dónde sale cada número. <span style="color:#E31C79">[Omite]</span> No inventes costos ni disponibilidad. Lo que no tenga precio va en pendientes.</p>
    <p style="margin-top:18px;font-size:14px"><b style="color:#fff">Regla de oro:</b> escríbelo como si se lo pidieras a una persona inteligente que empezó hoy.</p></div>
  <div class="box soft" style="margin-top:22px"><span class="n">si aprendiste otro marco</span><p>Es lo mismo con otros nombres. En las 6 partes de la charla, CLARO cubre contexto, tarea, insumos, formato y límites. El criterio de calidad es el hábito de escribir qué vas a revisar antes de pedir.</p></div></div>
</div>''')
    return kit("claro.html", "Plantilla CLARO", "El marco de prompt del taller, para llenar.", c)


def kit_datos():
    c = hero("kit · pieza 03 de 06", "Semáforo de datos", "Antes de pegar algo en una IA, mira de qué color es. En el taller los casos son ficticios; el semáforo es para tu caso propio.")
    c += sec('''<div class="grid g3" style="align-items:start">
  <div class="box"><span class="n"><i class="luz v"></i>verde · sí</span><h3>Adelante</h3><ul class="lista"><li>Datos ficticios o de ejemplo.</li><li>Información que ya es pública.</li><li>Tus propios borradores y notas sin datos de otras personas.</li></ul></div>
  <div class="box"><span class="n"><i class="luz a"></i>amarillo · con cuidado</span><h3>Primero límpialo</h3><ul class="lista"><li>Tus datos personales, como tu currículum: tú decides, pero quita cédula, dirección y teléfono.</li><li>Datos de clientes, compañeros o familiares: cambia los nombres y quita los contactos.</li><li>Información de tu empresa: solo si está autorizado y en la herramienta autorizada.</li></ul></div>
  <div class="box"><span class="n"><i class="luz r"></i>rojo · nunca</span><h3>No lo pegues</h3><ul class="lista"><li>Contraseñas, claves y códigos de verificación.</li><li>Números de cédula, tarjetas o cuentas.</li><li>Datos privados de otras personas sin su permiso.</li></ul></div>
</div>''')
    c += sec('''<div class="grid g2">
  <div class="box azul"><span class="n">// seis reglas</span><ul class="check" style="margin-top:10px"><li>Verifica cada dato, cifra, cita y fuente.</li><li>Desconfía de documentos de terceros: pueden traer instrucciones ocultas.</li><li>La IA propone; tú decides qué aceptar.</li><li>Una persona revisa antes de que algo llegue a un cliente, a un pago o a otra persona.</li><li>Revisa en la configuración de tu cuenta si tus conversaciones se usan para entrenar.</li><li>Si tienes dudas sobre datos de tu trabajo, pregunta antes a quien corresponda.</li></ul></div>
  <div class="box soft"><span class="n">en una organización</span><h3>Shadow AI</h3><p>Es usar IA fuera de lo que la organización autoriza o supervisa. Antes de llevar un caso de tu trabajo, revisa qué herramientas y qué datos están permitidos.</p></div>
</div>''', "reglas de uso")
    return kit("datos.html", "Semáforo de datos", "Qué puedes pegar en una IA y qué no.", c)


def kit_recuperacion():
    casos = [("No sé qué ruta elegir", "Elige la que más se parece a lo que quieres resolver el mes que viene. Si dudas, usa Vida cotidiana: es la que se muestra en la demo."),
             ("La IA no leyó todas las fuentes", "Pídele que liste qué fuentes leyó. Pega de nuevo la que falta y pide recalcular solo lo afectado."),
             ("No puedo adjuntar archivos", "No hace falta. Copia las fuentes desde la página de tu ruta y pégalas debajo del prompt."),
             ("Mi resultado no coincide con el esperado", "Bien: encontraste algo que verificar. Pide la operación paso a paso de esa cifra y corrige solo esa parte."),
             ("Llegué al límite de mi cuenta", "Sigue con los resultados esperados de tu ruta: compáralos con lo que alcanzaste a obtener y anota qué corregirías. Retoma cuando se restablezca."),
             ("La conversación se enredó", "Pide un resumen de lo acordado, abre una conversación nueva y pega el resumen con las fuentes."),
             ("No sé qué caso propio elegir", "Usa la lista de ideas de tu ruta o toma la opción B. Las tres opciones de la vuelta 2 valen igual."),
             ("Mi caso propio tiene datos rojos", "Cámbialos por datos inventados que se parezcan, o toma la opción B. Mira el semáforo de datos."),
             ("La herramienta no abre o calcula mal", "Dile a la IA qué esperabas ver y qué viste. Cambia una cosa a la vez y conserva la versión anterior."),
             ("Terminé antes", "Prueba tu plantilla con el segundo caso de tu ruta, o ayuda a alguien de tu mesa sin tocar su teclado.")]
    fr = "".join(f'<div class="phr"><b>{a}</b><q>{b}</q></div>' for a, b in casos)
    c = hero("kit · pieza 04 de 06", "Rescate", "Si te detienes, busca tu situación aquí antes de levantar la mano. Casi siempre hay una salida de un minuto.")
    c += sec(fr)
    return kit("recuperacion.html", "Rescate", "Qué hacer si te atascas durante el taller.", c)


def kit_plataformas():
    c = hero("kit · pieza 05 de 06", "ChatGPT, Claude o Gemini", "El taller funciona igual en las tres. Usa una sola durante toda la sesión. La cuenta gratuita sirve.")
    c += sec('''<div class="grid g3">
  <div class="box"><span class="n">mismas fuentes</span><h3>Texto pegado</h3><p>Copia las fuentes desde la página de tu ruta y pégalas debajo del prompt. Funciona en cualquier plataforma y en cualquier plan.</p></div>
  <div class="box"><span class="n">mismo encargo</span><h3>Una conversación por caso</h3><p>Abre una conversación nueva para cada caso. Si se enreda, pide un resumen y empieza otra.</p></div>
  <div class="box"><span class="n">misma comprobación</span><h3>Resultados esperados</h3><p>Los números no dependen de la plataforma. Si tu respuesta no coincide, hay algo que corregir.</p></div>
</div>''')
    c += sec(tabla([("ChatGPT", "Proyectos, GPT, instrucciones personalizadas"), ("Claude", "Proyectos, estilos, artefactos"), ("Gemini", "Gems, Canvas")],
                   ("Plataforma", "Dónde puedes guardar instrucciones o ver una herramienta"))
             + '<p class="lead" style="margin-top:18px">Los nombres, los botones y lo que incluye cada plan cambian con frecuencia. Si no ves una función en tu cuenta, guarda tu plantilla en un archivo de texto: funciona siempre.</p>'
             + '<div class="box soft"><span class="n">para la herramienta de la vuelta 2</span><p>Pide el resultado como un único archivo HTML. Si tu plataforma muestra una vista previa, úsala. Si no, copia el código, guárdalo como <b>herramienta.html</b> y ábrelo con tu navegador.</p></div>',
             "opcional", "Si tu cuenta lo permite.")
    return kit("plataformas.html", "Plataformas", "La misma ruta en ChatGPT, Claude o Gemini.", c)


def kit_hoja():
    linea = lambda t, n=1: f'<div class="hl-campo"><b>{t}</b>' + '<span></span>' * n + '</div>'
    c = hero("kit · pieza 06 de 06", "Hoja del participante", "Imprímela o llénala a mano durante el taller. Dos páginas.",
             '  <div class="meta no-print"><button class="chip n" onclick="window.print()" type="button">imprimir o guardar como PDF</button></div>\n')
    c += sec(f'''<div class="print-only print-head"><img src="../assets/logo-cecomsa-color.png" alt="CECOMSA"><span>Tu primera tarea resuelta con IA · Hoja del participante · Solenny Peralta</span></div>
<div class="hoja">
  <div class="grid g2">{linea("Nombre")}{linea("Mi ruta")}</div>
  <div class="box"><span class="n">vuelta 1 · paso 1 · mapear</span><h3>Antes de pedir</h3>{linea("Qué entra (fuentes)")}{linea("Qué debe salir")}{linea("Qué voy a revisar", 3)}</div>
  <div class="box"><span class="n">paso 2 · pedir</span><h3>Mi prompt CLARO</h3>{linea("C · Contexto")}{linea("L · Lo que necesito")}{linea("A · Archivos")}{linea("R · Resultado")}{linea("O · Omite")}</div>
  <div class="box"><span class="n">pasos 3 y 4 · verificar y corregir</span><h3>¿Cuadra?</h3>{linea("Un dato que comprobé")}{linea("La trampa que encontré")}{linea("La corrección que pedí")}{linea("Lo que descarté de la IA y por qué", 2)}</div>
  <div class="box salto"><span class="n">vuelta 2 · tú eliges</span><h3>A · mi caso &nbsp; B · segundo caso &nbsp; C · herramienta</h3>{linea("Qué voy a resolver")}{linea("Qué entra")}{linea("Qué debe salir")}{linea("Qué voy a revisar", 2)}{linea("Color de mis datos en el semáforo")}</div>
  <div class="box"><span class="n">paso 5 · guardar</span><h3>Mi plantilla</h3>{linea("Dónde la guardé")}{linea("Qué cambio cada vez que la uso", 2)}</div>
  <div class="box"><span class="n">cierre</span><h3>¿Lo usaría tal cual?</h3>{linea("Qué le falta")}{linea("Dónde lo voy a usar esta semana")}{linea("Qué necesito para dar ese paso")}</div>
  <div class="box soft"><span class="n">registro de uso · dos semanas</span>{tabla([("", "", "", "")] * 4, ("Fecha", "Qué le pedí", "¿Lo usé tal cual?", "Qué falló o qué descarté"))}</div>
</div>''')
    return kit("hoja.html", "Hoja del participante", "Hoja para imprimir y llenar durante el taller.", c)


TALLER_CSS = """/* Añadidos del taller sobre site.css */
.pleg{border:3px solid var(--ink);border-radius:12px;background:var(--blanco);box-shadow:5px 5px 0 var(--ink);margin-bottom:16px;overflow:hidden;}
.pleg summary{cursor:pointer;padding:14px 16px;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:13.5px;text-transform:uppercase;letter-spacing:.04em;background:var(--soft);list-style:none;}
.pleg summary::-webkit-details-marker{display:none;}
.pleg summary::before{content:"+ ";color:var(--mag);}
.pleg[open] summary::before{content:"– ";}
.pleg[open] summary{border-bottom:3px solid var(--ink);}
.pleg.rosa summary{background:var(--rosa);color:var(--blanco);}
.pleg.rosa summary::before{color:var(--blanco);}
.pleg-in{padding:16px;}
.pleg-in .tbl{box-shadow:none;border-width:2px;}
.pleg-in p{font-size:16px;line-height:1.6;}
ul.lista{margin:8px 0 0 1.1em;}
ul.lista li{margin-bottom:6px;font-size:15px;line-height:1.45;}
.luz{display:inline-block;width:12px;height:12px;border-radius:50%;border:2px solid var(--ink);margin-right:8px;vertical-align:-1px;}
.luz.v{background:#1F9D6B;} .luz.a{background:#F2A516;} .luz.r{background:#E5484D;}
.prompt pre{max-height:420px;overflow:auto;}
.hoja .box{margin-top:18px;}
.hl-campo{display:flex;flex-direction:column;gap:0;margin-top:10px;font-size:14px;}
.hl-campo b{font-family:'JetBrains Mono',monospace;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--mag);}
.hl-campo span{display:block;height:30px;border-bottom:2px solid var(--line);}
button.chip{cursor:pointer;font:inherit;font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;}
@media print{
  .pleg{box-shadow:none;} .pleg summary{background:none;}
  .prompt pre{max-height:none;}
  .hoja .box{margin-top:10px;} .hoja .salto{break-before:page;}
  .hl-campo span{height:26px;}
}
"""
