# 5.3.3.1 Formas de pago

FormaPago = {
  '1': '1 - Contado'
}

# 5.3.3.2 Medios de pago

MedioPago = {
    "1": "1 Instrumento no definido ",
    "40": "40 Débito Negocio Intercambio Corporativo (CTX)",
    "2": "2 Crédito ACH ",
    "41": "41 Concentración efectivo/Desembolso Crédito plus (CCD+)  ",
    "3": "3 Débito ACH ",
    "42": "42 Consignación bancaria",
    "4": "4 Reversión débito de demanda ACH ",
    "43": "43 Concentración efectivo / Desembolso Débito plus (CCD+)",
    "5": "5 Reversión crédito de demanda ACH   ",
    "44": "44 Nota cambiaria",
    "6": "6 Crédito de demanda ACH ",
    "45": "45 Transferencia Crédito Bancario",
    "7": "7 Débito de demanda ACH ",
    "46": "46 Transferencia Débito Interbancario",
    "8": "8 Mantener ",
    "47": "47 Transferencia Débito Bancaria",
    "9": "9 Clearing Nacional o Regional ",
    "48": "48 Tarjeta Crédito",
    "10": "10 Efectivo ",
    "49": "49 Tarjeta Débito",
    "11": "11 Reversión Crédito Ahorro ",
    "50": "50 Postgiro",
    "12": "12 Reversión Débito Ahorro ",
    "51": "51 Telex estándar bancario francés",
    "13": "13 Crédito Ahorro ",
    "52": "52 Pago comercial urgente",
    "14": "14 Débito Ahorro ",
    "53": "53 Pago Tesorería Urgente",
    "15": "15 Bookentry Crédito ",
    "60": "60 Nota promisoria",
    "16": "16 Bookentry Débito ",
    "61": "61 Nota promisoria firmada por el acreedor",
    "17": "17 Concentración de la demanda en efectivo /Desembolso Crédito (CCD) ",
    "62": "62 Nota promisoria firmada por el acreedor, avalada por el banco",
    "18": "18 Concentración de la demanda en efectivo / Desembolso (CCD) débito ",
    "63": "63 Nota promisoria firmada por el acreedor, avalada por un tercero",
    "19": "19 Crédito Pago negocio corporativo (CTP) ",
    "64": "64 Nota promisoria firmada por el banco",
    "20": "20 Cheque ",
    "65": "65 Nota promisoria firmada por un banco avalada por otro banco",
    "21": "21 Proyecto bancario ",
    "66": "66 Nota promisoria firmada  ",
    "22": "22 Proyecto bancario certificado ",
    "67": "67 Nota promisoria firmada por un tercero avalada por un banco",
    "23": "23 Cheque bancario ",
    "70": "70 Retiro de nota por el por el acreedor",
    "24": "24 Nota cambiaria esperando aceptación ",
    "71": "71 Bonos",
    "25": "25 Cheque certificado ",
    "72": "72 Vales",
    "26": "26 Cheque Local ",
    "74": "74 Retiro de nota por el por el acreedor sobre un banco",
    "27": "27 Débito Pago Negocio Corporativo (CTP) ",
    "75": "75 Retiro de nota por el acreedor, avalada por otro banco",
    "28": "28 Crédito Negocio Intercambio Corporativo (CTX) ",
    "76": "76 Retiro de nota por el acreedor, sobre un banco avalada por un tercero",
    "29": "29 Débito Negocio Intercambio Corporativo (CTX) ",
    "77": "77 Retiro de una nota por el acreedor sobre un tercero",
    "30": "30 Transferencia Crédito ",
    "78": "78 Retiro de una nota por el acreedor sobre un tercero avalada por un banco",
    "31": "31 Transferencia Débito ",
    "91": "91 Nota bancaria transferible",
    "32": "32 Concentración Efectivo / Desembolso Crédito plus (CCD+) ",
    "92": "92 Cheque local trasferible",
    "33": "33 Concentración Efectivo / Desembolso Débito plus (CCD+) ",
    "93": "93 Giro referenciado",
    "34": "34 Pago y depósito pre acordado (PPD) ",
    "94": "94 Giro urgente",
    "35": "35 Concentración efectivo ahorros / Desembolso Crédito (CCD) ",
    "95": "95 Giro formato abierto",
    "36": "36 Concentración efectivo ahorros / Desembolso Crédito (CCD) ",
    "96": "96 Método de pago solicitado no usado",
    "37": "37 Pago Negocio Corporativo Ahorros Crédito (CTP) ",
    "97": "97 Clearing entre partners",
    "38": "38 Pago Negocio Corporativo Ahorros Débito (CTP) ",
    "98": "98 Cuentas de Ahorro de Tramite Simplificado (CATS)(Nequi, Daviplata, etc)",
    "39": "39 Crédito Negocio Intercambio Corporativo (CTX) ZZZ Acuerdo mutuo",
}

# 5.5.1 Periodo de Nomina

PeriodoNomina = {
  '1': '1 - Semanal',
  '2': '2 - Decenal',
  '3': '3- Catorcenal',
  '4': '4 - Quincenal',
  '5': '5 - Mensual',
  '6': '6 - Otro',
}

# 5.5.2 Tipo de contrato

TipoContrato = {
  '1': '1 - Termino fijo',
  '2': '2 - Termino Indefinido',
  '3': '3 - Obra o Labor',
  '4': '4 - Aprendizaje',
  '5': '5 - Practicas o Pasantias',
}

# 5.5.3 Tipo de Trabajador

TipoTrabajador = {
    '01': '01 Dependiente',
    '02': '02 Servicio domestico',
    '04': '04 Madre comunitaria',
    '12': '12 Aprendices del Sena en etapa lectiva',
    '18': '18 Funcionarios públicos sin tope máximo de ibc',
    '19': '19 Aprendices del SENA en etapa productiva',
    '21': '21 Estudiantes de postgrado en salud',
    '22': '22 Profesor de establecimiento particular',
    '23': '23 Estudiantes aportes solo riesgos laborales',
    '30': '30 Dependiente entidades o universidades públicas con régimen especial en salud',
    '31': '31 Cooperados o pre cooperativas de trabajo asociado',
    '47': '47 Trabajador dependiente de entidad beneficiaria del sistema general de participaciones ‐ aportes patronales',
    '51': '51 Trabajador de tiempo parcial',
    '54': '54 Pre pensionado de entidad en liquidación.',
    '56': '56 Pre pensionado con aporte voluntario a salud',
    '58': '58 Estudiantes de prácticas laborales en el sector público',
}

# 5.5.4 Subtipo de Trabajador

SubTipoTrabajador = {
   '00': 'No Aplica',
   '01': 'Dependiente pensionado por vejez activo',
}

# 5.5.5 Tipo de Hora Extra o Recargo

Porcentaje = [
    # 1 Hora Extra Diurna 25.00
    {
        'codigo': '1',
        'tipo': 'Hora Extra Diurna',
        'porcentaje': 25.00
    },

    # 2 Hora Extra Nocturna 75.00
    {
        'codigo': '2',
        'tipo': 'Hora Extra Nocturna',
        'porcentaje': 75.00
    },

    # 3 Hora Recargo Nocturno 35.00
    {
        'codigo': '3',
        'tipo': 'Hora Recargo Nocturno',
        'porcentaje': 35.00
    },

    # 4 Hora Extra Diurna Dominical y Festivos 100.00
    {
        'codigo': '4',
        'tipo': 'Hora Extra Diurna Dominical y Festivos',
        'porcentaje': 100.00
    },

    # 5 Hora Recargo Diurno Dominical y Festivos 75.00
    {
        'codigo': '5',
        'tipo': 'Hora Recargo Diurno Dominical y Festivos',
        'porcentaje': 75.00
    },

    # 6 Hora Extra Nocturna Dominical y Festivos 150.00
    {
        'codigo': '6',
        'tipo': 'Hora Extra Nocturna Dominical y Festivos',
        'porcentaje': 150.00
    },

    # 7 Hora Recargo Nocturno Dominical y Festivos 110.00
    {
        'codigo': '7',
        'tipo': 'Hora Recargo Nocturno Dominical y Festivos',
        'porcentaje': 110.00
    },
]

# 5.5.6 Tipo de Incapacidad

Tipo = [
    {
        'codigo': '1',
        'descripcion': 'Comun',
    },
    {
        'codigo': '2',
        'descripcion': 'Profesional',
    },
    {
        'codigo': '3',
        'descripcion': 'Laboral'
    },
]

# 5.5.7 Tipo de XML

TipoXML = [
    {
        'codigo': '102',
        'nombre': 'NominaIndividual',
        'descripcion': 'Documento Soporte de Pago de Nómina Electrónica',
    },
    {
        'codigo': '103',
        'nombre': 'NominaIndividualDeAjuste',
        'descripcion': 'Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica',
    },
]