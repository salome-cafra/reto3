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
