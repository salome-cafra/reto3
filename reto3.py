import math
import time  # [INVESTIGADO EN GOOGLE]

# ==========================================
# 1. FUNCIONES PRINCIPALES (LOGICA SENCILLA)
# ==========================================

def calcular_altitud(presion_hpa):
    """Calcula la altitud en metros usando la fórmula barométrica."""
    # Usamos math.pow(base, exponente) para elevar la relación de presión
    altitud = 44330.0 * (1.0 - math.pow((presion_hpa / 1013.25), 0.1903))
    return altitud


def determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion):
    """Determina la fase actual del vuelo según la variación de la altitud."""
    if altitud_actual > altitud_previa:
        return "1: Ascenso"
    elif altitud_actual <= altitud_previa and altitud_actual > 500:
        return "2: Apogeo / Caida libre"
    else:
        return "3: Despliegue de Paracaidas"


def evaluar_alerta_temperatura(temp_celsius):
    """Evalúa si la temperatura excede los límites seguros."""
    if temp_celsius > 80:
        return "¡ALERTA CRITICA: Temperatura muy alta!"
    else:
        return "Temperatura Normal"


# ==========================================
# 2. PROGRAMA PRINCIPAL (AUTOMATIZADO)
# ==========================================

def main():
    print("=== SISTEMA DE CONTROL DE VUELO - SIMULACION AUTOMATICA ===")
    print("Procesando telemetria en tiempo real...\n")

    # [INVESTIGADO EN GOOGLE]: Lista de tuplas estandarizada para evitar pedir datos a mano con input()
    datos_telemetria = [
        (1013.25, 15.0, 25.0),  # Segundo 1: Despegue
        (850.0,    9.8, 45.0),  # Segundo 2: Ascenso rápido
        (700.0,    2.0, 85.0),  # Segundo 3: Alta altitud y ALERTA de temperatura
        (750.0,   -9.8, 60.0),  # Segundo 4: Apogeo / Caída libre
        (980.0,   -2.0, 30.0)   # Segundo 5: Cerca de tierra / Paracaídas
    ]

    # Variables acumuladoras y métricas iniciales
    altitud_maxima = 0.0
    altitud_previa = 0.0
    suma_temperatura = 0.0
    contador_lecturas = 0
    apogeo_detectado = False

    segundo = 1

    # Bucle 'for' para recorrer los datos de telemetría uno a uno
    for presion, aceleracion, temperatura in datos_telemetria:
        print(f"--- Segundo {segundo} ---")
        print(f"Lectura automatica -> Presion: {presion} hPa | Acel: {aceleracion} m/s² | Temp: {temperatura} °C")

        # Cálculos del segundo actual usando las funciones
        altitud_actual = calcular_altitud(presion)
        estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alerta_temp = evaluar_alerta_temperatura(temperatura)

        # Evaluación de altitud máxima registrada
        if altitud_actual > altitud_maxima:
            altitud_maxima = altitud_actual

        # Detección del punto de apogeo
        if altitud_actual < altitud_previa and not apogeo_detectado:
            apogeo_detectado = True
            print(">> [EVENTO]: Apogeo detectado en este segundo <<")

        # Acumulación para el promedio de temperatura
        suma_temperatura += temperatura
        contador_lecturas += 1

        # Muestra de resultados procesados en pantalla
        print(f"[RESULTADOS SEGUNDO {segundo}]")
        print(f"  • Altitud calculada : {altitud_actual:.2f} m")
        print(f"  • Estado de vuelo   : {estado}")
        print(f"  • Diagnostico Temp  : {alerta_temp}\n")

        # Guardar la altitud actual como previa para el siguiente segundo
        altitud_previa = altitud_actual
        segundo += 1

        # [INVESTIGADO EN GOOGLE]: time.sleep(1.5) busca pausar la ejecución 1.5 segundos entre cada lectura
        time.sleep(1.5)

    # Resumen global al finalizar la simulación
    print("==========================================")
    print("        RESUMEN FINAL DE LA MISION        ")
    print("==========================================")
    if contador_lecturas > 0:
        promedio_temp = suma_temperatura / contador_lecturas
        print(f"• Altitud maxima alcanzada : {altitud_maxima:.2f} m")
        print(f"• Temperatura promedio     : {promedio_temp:.2f} °C")
        if apogeo_detectado:
            print("• Apogeo detectado         : SI (transicion a descenso registrada)")
        else:
            print("• Apogeo detectado         : NO")


if __name__ == "__main__":
    main()