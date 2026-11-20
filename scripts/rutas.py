# Datos de las cuatro rutas. Las cifras de los resultados esperados se calculan aquí,
# no se escriben a mano, para que coincidan con las fuentes.
import math, pathlib

F = pathlib.Path(__file__).parent / "fuentes"
rd = lambda n: ("−" if n < 0 else "") + "RD$" + (f"{abs(n):,.2f}" if n != int(n) else f"{int(abs(n)):,}")


def leer(nombre):
    return (F / nombre).read_text(encoding="utf-8").strip()


# ---------- Vida cotidiana: Brisa Mini ----------
def brisa():
    asis, tope = 30, 18000
    extras = 1000 + 500
    lug = {"L1": 4500 + 1500, "L2": 7000 + 0}
    ref = {"R1": max(asis, 20) * 250 + 500, "R2": max(asis, 40) * 200 + 900}
    combos = {f"{l} + {r}": lug[l] + ref[r] + extras for l in lug for r in ref}
    assert combos == {"L1 + R1": 15500, "L1 + R2": 16400, "L2 + R1": 16500, "L2 + R2": 17400}
    assert all(v <= tope for v in combos.values())
    return ref, combos


def coctel():
    asis, tope, veg, extras = 40, 30000, 8, 1400
    lug = {"T1": 9000, "T2": 12500 + 1500}
    c1 = max(asis, 30) * 380 + 1200
    c2 = max(asis, 50) * 340 + 800
    out = {
        "T1 + C1": lug["T1"] + c1 + veg * 40 + extras,
        "T1 + C2": lug["T1"] + c2 + extras,
        "T2 + C1": lug["T2"] + c1 + veg * 40 + extras,
        "T2 + C2": lug["T2"] + c2 + extras,
    }
    assert out == {"T1 + C1": 27120, "T1 + C2": 28200, "T2 + C1": 32120, "T2 + C2": 33200}
    sin_veg = lug["T1"] + c1 + extras
    return out, sin_veg, tope


# ---------- Emprendimiento: Dulce Lote ----------
def dulce(descuento=True):
    u = 80
    productos = u * 45 * (0.9 if descuento else 1)
    delivery = 600
    cobrado = productos + delivery
    comision = round(cobrado * 0.04, 2)
    cajas = math.ceil(u / 12)
    costos = {
        "Ingredientes": u * 18,
        "Cápsulas y decoración": u * 6,
        f"Cajas ({cajas} × RD$45)": cajas * 45,
        "Mano de obra (5 h × RD$200)": 1000,
        "Delivery Zona B": delivery,
        "Comisión de tarjeta (4%)": comision,
    }
    total = round(sum(costos.values()), 2)
    return dict(productos=productos, cobrado=cobrado, comision=comision, cajas=cajas,
                costos=costos, total=total, resultado=round(cobrado - total, 2),
                sin_mano=round(cobrado - total + 1000, 2))


def mensajes():
    m2 = 2 * 420 + 350
    m3 = 24 * 45 + 600
    return m2, m2 / 2, m3, m3 / 2


_ref, _combos = brisa()
_coc, _coc_sin_veg, _coc_tope = coctel()
_d, _d0 = dulce(True), dulce(False)
assert _d["cajas"] == 7 and _d["resultado"] == -148.6 and _d["sin_mano"] == 851.4
assert _d0["resultado"] == 197.0
_m2, _m2a, _m3, _m3a = mensajes()

HERR = ("Con lo que ya resolvimos en esta conversación, crea una herramienta sencilla: {que}.\n"
        "Entrégala como un único archivo HTML, con los estilos y el JavaScript dentro.\n"
        "Sin instalaciones, sin conexiones externas, sin login y sin guardar datos en servidores.\n"
        "Usa solo los datos ficticios de este caso como valores iniciales.\n"
        "Debe mostrar una alerta cuando {alerta}.\n"
        "Al final, dime tres casos de prueba con el resultado que debo ver en cada uno.")

RUTAS = [
    dict(
        slug="vida", n="01", nombre="Vida cotidiana y comunidad",
        para="Organizar una actividad, una celebración o un viaje comparando opciones y presupuesto.",
        caso="Lanzamiento Brisa Mini",
        resumen="Un evento ficticio para 30 personas con RD$18,000. Hay dos lugares y dos refrigerios para comparar.",
        fuente=leer("vida_brisa_mini.txt"), archivo="vida_brisa_mini.txt",
        entregable="Comparación de las cuatro combinaciones, presupuesto de la opción elegida, agenda de 120 minutos y lista de pendientes.",
        reviso=["Que cada total salga de sumar las fuentes.", "Que el refrigerio use el pedido mínimo.", "Que lo pendiente no aparezca como confirmado."],
        prompt=("[Contexto] Estoy organizando el lanzamiento de Brisa Mini, un evento ficticio para 30 personas con un presupuesto máximo de RD$18,000.\n"
                "[Lo que necesito] Compara las cuatro combinaciones de lugar y refrigerio, recomienda una y prepara el plan del evento.\n"
                "[Archivos] Usa solo las fuentes B1, L, R y N1 que pego debajo. Antes de empezar, dime qué fuentes leíste.\n"
                "[Resultado] 1) Tabla con el total de cada combinación y de dónde sale cada número. 2) Agenda de 120 minutos. 3) Lista de pendientes.\n"
                "[Omite] No inventes costos ni disponibilidad. No agregues impuestos. Lo que no tenga precio va en pendientes, no como cero."),
        esperados=[("Refrigerio R1 (30 personas)", rd(_ref["R1"])), ("Refrigerio R2 (factura 40)", rd(_ref["R2"]))]
                  + [(k, rd(v)) for k, v in _combos.items()]
                  + [("Tope del presupuesto", "RD$18,000: las cuatro combinaciones caben")],
        trampa=("R2 parece más barato (RD$200 por persona contra RD$250), pero factura un mínimo de 40 y termina costando "
                f"{rd(_ref['R2'])} contra {rd(_ref['R1'])} de R1. Además hay tres pendientes que la IA no puede dar por resueltos: "
                "la disponibilidad del lugar, el transporte del expositor y el precio de venta. La agenda debe sumar 120 minutos "
                "y la persona expositora solo está de 17:20 a 18:00."),
        corrige="El total de L1 + R2 no cuadra: R2 factura el mínimo de 40 personas. Recalcula solo esa fila y muéstrame la suma.",
        b_titulo="Cóctel Conecta", b_archivo="vida_coctel_conecta.txt", b_fuente=leer("vida_coctel_conecta.txt"),
        b_pide="Compara las cuatro combinaciones, di cuáles caben en el presupuesto y qué falta confirmar.",
        b_esperados=[(k, rd(v) + (" · no cabe" if v > _coc_tope else " · cabe")) for k, v in _coc.items()]
                    + [("T1 + C1 si no se confirman los vegetarianos", rd(_coc_sin_veg))],
        b_trampa="C2 cobra menos por persona pero factura un mínimo de 50. Los 8 menús vegetarianos están pendientes: el total de C1 es un rango, no una cifra cerrada.",
        ideas=["Una celebración familiar con dos o tres cotizaciones.", "Una actividad de la iglesia, el club o la junta de vecinos.",
               "Un viaje corto: transporte, alojamiento y comidas.", "La compra de un equipo comparando tres tiendas.",
               "El presupuesto de la vuelta a clases."],
        herramienta=HERR.format(que="una calculadora del evento donde pueda cambiar la cantidad de asistentes y elegir lugar y refrigerio",
                                alerta="el total supere el presupuesto o los asistentes superen la capacidad del lugar"),
    ),
    dict(
        slug="trabajo", n="02", nombre="Trabajo",
        para="Ordenar información que llega dispersa: correos, agenda, notas y pendientes.",
        caso="Resumen de mi lunes",
        resumen="Ocho correos y la agenda de una semana ficticia. Hay que separar lo urgente, detectar choques y descartar el ruido.",
        fuente="FUENTE E · CORREOS\n" + leer("trabajo_correos.md") + "\n\n\nFUENTE A · AGENDA DE LA SEMANA (CSV)\n" + leer("trabajo_calendario.csv"),
        archivo="trabajo_semana.txt",
        entregable="Una página con lo urgente, la semana en una tabla, los choques y lo que se puede ignorar.",
        reviso=["Que cada urgente tenga quién lo pide y para cuándo.", "Que detecte el choque del miércoles.", "Que no ponga fechas que ningún correo da."],
        prompt=("[Contexto] Es lunes por la mañana y quiero arrancar la semana con claridad. Los correos y la agenda son ficticios.\n"
                "[Lo que necesito] Prepara mi \"Resumen del lunes\".\n"
                "[Archivos] Usa solo los correos (fuente E) y la agenda (fuente A) que pego debajo.\n"
                "[Resultado] Máximo una página con: 1) Lo urgente: quién lo pide, para cuándo y una respuesta de una línea. 2) Mi semana en una tabla. 3) Choques y riesgos. 4) Lo que puedo ignorar, en una línea.\n"
                "[Omite] No inventes fechas ni compromisos. Lo que no esté claro va marcado \"por confirmar\"."),
        esperados=[("Urgentes", "5: reporte Q3 para Laura (miércoles al mediodía), factura duplicada de Miguel, confirmar el pedido a Pedro, evaluaciones de RR. HH. (viernes), presentación de Carla (antes del jueves)"),
                   ("Choque", "La capacitación del miércoles a las 11:00 se pisa con la entrega del reporte Q3 al mediodía"),
                   ("Se puede ignorar", "2: el boletín y la promoción")],
        trampa=("Miguel pide resolver la factura \"antes del cierre de mes\", pero ningún correo dice qué día es el cierre: va \"por confirmar\", no con una fecha inventada. "
                "El embarque de Pedro tiene fecha \"estimada\", no confirmada. Y un detalle fino: el sistema de facturación estará fuera de servicio el martes de 6:00 a 8:00 p. m., "
                "justo el sistema que se necesita para anular la factura."),
        corrige="Pusiste una fecha para el cierre de mes y ningún correo la da. Cámbiala por \"por confirmar\" y dime qué le preguntarías a Miguel.",
        b_titulo="Minuta de la mudanza", b_archivo="trabajo_notas_reunion.txt", b_fuente=leer("trabajo_notas_reunion.txt"),
        b_pide="Convierte las notas en una minuta con acuerdos, responsable, fecha y temas abiertos.",
        b_esperados=[("Acuerdos con responsable", "3: Julio (internet), Marta (2 cotizaciones, jueves), Iván (inventario, viernes)"),
                     ("Sin responsable", "Avisar a los clientes del cambio de dirección"),
                     ("Sin decidir", "Limpieza del local nuevo y uso del ascensor de carga"),
                     ("Presupuesto", f"{rd(62000)} + {rd(9500)} estimado = {rd(71500)}; quedan {rd(85000 - 71500)} de {rd(85000)}")],
        b_trampa="Nadie quedó a cargo de avisar a los clientes: la minuta debe decir \"sin responsable\", no asignárselo a alguien. El internet no tiene fecha y las cajas son un estimado sin cotización.",
        ideas=["Un reporte que preparas cada semana o cada mes.", "La minuta de una reunión recurrente.", "El seguimiento de pendientes de tu equipo.",
               "La respuesta a un tipo de correo que se repite.", "El resumen de un documento largo para tu jefe."],
        herramienta=HERR.format(que="un priorizador donde pueda anotar pendientes con fecha y quién lo pide, y me los ordene por urgencia",
                                alerta="dos pendientes tengan la misma fecha y hora, o falte la fecha"),
    ),
    dict(
        slug="empleo", n="03", nombre="Empleo y estudios",
        para="Postularte a una vacante, una beca o un curso sin inventar nada.",
        caso="La vacante de Lucía",
        resumen="Una vacante de Analista de Compras y el currículum de una candidata ficticia que cumple solo una parte.",
        fuente=leer("empleo_vacante_y_cv.txt"), archivo="empleo_vacante_y_cv.txt",
        entregable="Tabla de requisitos contra evidencia, currículum adaptado, carta de 120 palabras y 5 preguntas de entrevista.",
        reviso=["Que cada frase del CV adaptado exista en el CV original.", "Que las brechas aparezcan como brechas.", "Que no haya cifras ni logros nuevos."],
        prompt=("[Contexto] Soy Lucía Marte y quiero postularme a la vacante de Analista de Compras. No cumplo todos los requisitos. Los datos son ficticios.\n"
                "[Lo que necesito] Ayúdame a presentar mi experiencia real de la mejor forma para esta vacante.\n"
                "[Archivos] Usa solo la vacante (V1), mi currículum (CV1) y mi nota (N1) que pego debajo.\n"
                "[Resultado] 1) Tabla: requisito, evidencia en mi CV, y si cumplo, cumplo en parte o no cumplo. 2) Mi CV reordenado para esta vacante. 3) Carta de máximo 120 palabras. 4) Cinco preguntas que me harían en la entrevista.\n"
                "[Omite] No agregues experiencia, cifras, cursos ni niveles de idioma que no estén en mi CV. Si me falta un requisito, dilo y sugiere cómo abordarlo con honestidad."),
        esperados=[("3 años en compras o abastecimiento", "No cumple: unos 2 años en tareas relacionadas, desde 2024"),
                   ("Excel avanzado", "Cumple: tablas dinámicas y BUSCARV, más el curso de 40 horas"),
                   ("Negociación con proveedores", "En parte: da seguimiento a 12 proveedores locales; no negocia ni trabaja con internacionales"),
                   ("Inglés intermedio", "No cumple: inglés básico"),
                   ("ERP (deseable)", "No aparece en el CV")],
        trampa=("La IA tiende a \"ayudar\" de más: convierte dos años en tres, el seguimiento en negociación, el inglés básico en intermedio, "
                "o agrega un logro con porcentaje. Compara línea por línea el CV adaptado con el original: todo lo que no esté en CV1 se borra. "
                "Reordenar y redactar mejor está bien; inventar, no."),
        corrige="En el CV adaptado escribiste \"negociación con proveedores\" y mi CV solo dice seguimiento de entregas. Corrige esa línea usando solo lo que dice CV1.",
        b_titulo="La beca de Daniel", b_archivo="empleo_beca.txt", b_fuente=leer("empleo_beca.txt"),
        b_pide="Revisa si Daniel cumple cada requisito, arma su lista de pendientes con fechas y dile qué hacer primero.",
        b_esperados=[("Edad", "No cumple: cumple 31 el 22 de marzo y la convocatoria cierra el 30. En la fecha de cierre tendrá 31"),
                     ("Promedio", "Cumple: 87 es mayor que 85"),
                     ("Certificación de notas", "Si la pide hoy (10 de marzo) llega el 25 de marzo, antes del cierre"),
                     ("Ensayo", "Sobran 220 palabras: tiene 720 y el máximo es 500"),
                     ("Carta de recomendación", "Pendiente: aceptada pero no enviada")],
        b_trampa="Hoy Daniel tiene 30 años y la IA suele darlo por elegible. El requisito se mide en la fecha de cierre, y para entonces tendrá 31. Lo correcto es avisarle antes de que gaste tiempo en los demás trámites, y sugerirle confirmar con la institución.",
        ideas=["Tu CV real y una vacante que te interese.", "Los requisitos de una beca o un curso.", "Un plan de estudio para una certificación.",
               "Preguntas de práctica para una entrevista.", "Un mensaje para pedir una carta de recomendación."],
        herramienta=HERR.format(que="un registro de postulaciones con empresa, puesto, fecha de envío, estado y próximo paso",
                                alerta="una postulación lleve más de 7 días sin seguimiento"),
    ),
    dict(
        slug="emprendimiento", n="04", nombre="Emprendimiento",
        para="Cotizar, poner precios y responder a clientes sabiendo cuánto ganas de verdad.",
        caso="El pedido de Dulce Lote",
        resumen="Una repostería ficticia recibe un pedido de 80 mini cupcakes con descuento, delivery y pago con tarjeta.",
        fuente=leer("emprendimiento_pedido.txt"), archivo="emprendimiento_pedido.txt",
        entregable="Cotización para la clienta, cálculo de costos y ganancia, y un mensaje de respuesta.",
        reviso=["Que estén todos los costos, incluida la mano de obra.", "Que las cajas se redondeen hacia arriba.", "Que use Zona B y la comisión de tarjeta."],
        prompt=("[Contexto] Tengo una repostería desde casa, Dulce Lote. Recibí un pedido de 80 mini cupcakes. Los datos son ficticios.\n"
                "[Lo que necesito] Calcula cuánto cobro, cuánto me cuesta y cuánto gano de verdad con este pedido. Después prepara la cotización.\n"
                "[Archivos] Usa solo el pedido (P1), la lista de precios (L1), los costos (C1) y mi nota (N1) que pego debajo.\n"
                "[Resultado] 1) Tabla de lo que cobro. 2) Tabla de costos, uno por línea, con la operación. 3) Ganancia o pérdida. 4) Mensaje corto para la clienta con la cotización y lo que falta confirmar.\n"
                "[Omite] No inventes costos ni cambies los precios de la lista. Si pierdo dinero, dímelo antes de escribir el mensaje."),
        esperados=[("Productos con 10% de descuento", rd(_d["productos"])), ("Total a cobrar (con delivery Zona B)", rd(_d["cobrado"]))]
                  + [(k, rd(v)) for k, v in _d["costos"].items()]
                  + [("Costo total", rd(_d["total"])), ("Resultado con descuento", rd(_d["resultado"]) + " · pérdida"),
                     ("Resultado sin descuento", rd(_d0["resultado"]) + " · ganancia")],
        trampa=(f"Si la IA deja fuera la mano de obra, el pedido parece dejar {rd(_d['sin_mano'])} de ganancia. Con las 5 horas incluidas, se pierden {rd(abs(_d['resultado']))}. "
                "La dueña lo pidió en su nota: quiere saber cuánto gana de verdad. Otros tres errores frecuentes: calcular 6.67 cajas en vez de 7, "
                "usar el delivery de Zona A y olvidar la comisión de la tarjeta."),
        corrige="Faltó la mano de obra: son 5 horas a RD$200. Agrégala a la tabla de costos y recalcula solo la ganancia.",
        b_titulo="Tres mensajes de clientes", b_archivo="emprendimiento_mensajes.txt", b_fuente=leer("emprendimiento_mensajes.txt"),
        b_pide="Redacta una respuesta amable para cada mensaje, con el precio y aplicando las políticas.",
        b_esperados=[("M1 · bizcocho para mañana", "No se puede: los pedidos requieren 48 horas. Ofrecer el sábado"),
                     ("M2 · brownies el domingo", f"No hay entregas los domingos. Alternativa: {rd(_m2)} en total (2 cajas más delivery Zona A), anticipo {rd(_m2a)}"),
                     ("M3 · 24 mini cupcakes en Zona B", f"{rd(_m3)} en total. No hay pago completo contra entrega: anticipo {rd(_m3a)}")],
        b_trampa="La IA quiere complacer al cliente y tiende a decir que sí a todo. Las tres respuestas correctas incluyen un \"no\" amable: por el plazo, por el domingo y por el pago contra entrega.",
        ideas=["Tu lista de precios con tus costos reales.", "Respuestas a las preguntas que más te hacen.", "El calendario de publicaciones de un mes.",
               "La cotización de un pedido grande.", "La comparación de dos proveedores."],
        herramienta=HERR.format(que="un cotizador donde pueda cambiar la cantidad de unidades, la zona de entrega, el descuento y la forma de pago",
                                alerta="el pedido deje pérdida"),
    ),
]
