## 📥 Datos de Entrada

| NOMBRE | DEFINICIÓN | TIPO | UNIDAD |
| :--- | :--- | :--- | :--- |
| **Presion** | Presión barométrica atmosférica medida por los sensores del cohete | Real | hPa |
| **Aceleracion** | Aceleración vertical experimentada por la nave durante el trayecto | Real | m/s² |
| **Temperatura** | Temperatura ambiental registrada en el exterior del cohete | Real | °C |

---

## 📤 Datos de Salida

| NOMBRE | DEFINICIÓN | TIPO | UNIDAD |
| :--- | :--- | :--- | :--- |
| **Altitud** | Altitud sobre el nivel del mar calculada a partir de la presión | Real | m |
| **Estado_Vuelo** | Fase operativa actual del cohete (Ascenso, Apogeo / Caída libre, Paracaídas) | Texto | - |
| **Alerta_Temperatura** | Diagnóstico sobre si la temperatura sobrepasa el límite de seguridad (80 °C) | Texto | - |
| **Altitud_Maxima** | Mayor altura registrada a lo largo de toda la misión | Real | m |
| **Promedio_Temperatura**| Temperatura promedio calculada al finalizar todas las lecturas | Real | °C |
| **Apogeo_Detectado** | Indicador de confirmación sobre si se registró el punto más alto del vuelo | Booleano | - |

---

## ⚙️ Operaciones y Fórmulas

| NOMBRE | FÓRMULA / OPERACIÓN | DESCRIPCIÓN |
| :--- | :--- | :--- |
| **Calcular Altitud** | $Altitud = 44330.0 \times (1.0 - (Presion / 1013.25)^{0.1903})$ | Convierte la presión barométrica a altitud estimada en metros |
| **Promedio Temperatura** | $Promedio\_Temperatura = \frac{\sum Temperatura}{Total\_Lecturas}$ | Suma acumulada de temperaturas dividida por la cantidad total de lecturas |

---

## 🔍 Notas sobre Funciones Utilizadas

Para realizar la simulación de forma automática y fluida, utilizamos dos conceptos adicionales desarrollados con la lógica vista en clase:

1. **Lista de Telemetría Estandarizada (`datos_telemetria`):** En lugar de pedir los datos manualmente por consola uno a uno (`input()`), usamos una lista con lecturas fijas de presión, aceleración y temperatura para procesarlas secuencialmente.
2. **Control de Tiempo (`time.sleep`):** Usamos la librería nativa `time` para hacer pausas de 1.5 segundos en cada iteración del bucle. Esto permite simular visualmente la llegada de datos segundo a segundo.

---

## 📝 Pseudocódigo

```text
ALGORITMO Simulación_Cohete

  FUNCION calcular_altitud(presion_hpa: Real) -> Real
      altitud <- 44330.0 * (1.0 - ((presion_hpa / 1013.25) ^ 0.1903))
      RETORNAR altitud
  FIN_FUNCION

  FUNCION determinar_estado_vuelo(altitud_actual: Real, altitud_previa: Real, aceleracion: Real) -> Texto
      SI altitud_actual > altitud_previa ENTONCES
          RETORNAR "1: Ascenso"
      SINO SI altitud_actual <= altitud_previa Y altitud_actual > 500 ENTONCES
          RETORNAR "2: Apogeo / Caida libre"
      SINO
          RETORNAR "3: Despliegue de Paracaidas"
      FIN_SI
  FIN_FUNCION

  FUNCION evaluar_alerta_temperatura(temp_celsius: Real) -> Texto
      SI temp_celsius > 80 ENTONCES
          RETORNAR "¡ALERTA CRITICA: Temperatura muy alta!"
      SINO
          RETORNAR "Temperatura Normal"
      FIN_SI
  FIN_FUNCION

INICIO
    altitud_maxima <- 0.0
    altitud_previa <- 0.0
    suma_temperatura <- 0.0
    contador_lecturas <- 0
    apogeo_detectado <- FALSO

    PARA CADA (presion, aceleracion, temperatura) EN datos_telemetria HACER
        altitud_actual <- calcular_altitud(presion)
        estado <- determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alerta <- evaluar_alerta_temperatura(temperatura)

        SI altitud_actual > altitud_maxima ENTONCES
            altitud_maxima <- altitud_actual
        FIN_SI

        SI altitud_actual < altitud_previa Y NO apogeo_detectado ENTONCES
            apogeo_detectado <- VERDADERO
        FIN_SI

        suma_temperatura <- suma_temperatura + temperatura
        contador_lecturas <- contador_lecturas + 1
        altitud_previa <- altitud_actual
    FIN_PARA

    SI contador_lecturas > 0 ENTONCES
        promedio_temp <- suma_temperatura / contador_lecturas
        MOSTRAR "Altitud Máxima:", altitud_maxima
        MOSTRAR "Promedio Temperatura:", promedio_temp
    FIN_SI
FIN

## 🔍 Notas de Investigación en Internet / Google

Para lograr una simulación automática más avanzada sin alterar la lógica básica vista en clase, investigamos en la documentación de Google / Python lo siguiente:

1. **Estructura de Datos Estandarizada (`datos_telemetria`):** Se buscó en internet cómo almacenar un grupo estandarizado de datos predefinidos usando una lista de tuplas, evitando tener que solicitar las lecturas a mano con `input()`.
2. **Librería `time` y comando `time.sleep(1.5)`:** Se investigó en la web sobre la librería nativa `time` para pausar la ejecución por 1.5 segundos en cada iteración del bucle, simulando la recepción de telemetría en tiempo real.
