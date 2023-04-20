# Variables del cohete
masa_cohete = 10.0  # masa del cohete (kg)
masa_agua = 10.0  # masa del agua (kg)
velocidad_salida = 10.0  # velocidad de salida del agua (m/s)
area_seccion_transversal = 0.1  # área de la sección transversal del cohete (m^2)
coeficiente_arrastre = 0.2  # coeficiente de arrastre del cohete
altura_inicial = 0.0  # altura inicial del cohete (m)
tiempo_total = 20.0  # tiempo total de simulación (s)
delta_tiempo = 0.1 # paso de tiempo de la simulación (s)

# Constantes físicas
gravedad = 9.81  # aceleración debida a la gravedad (m/s^2)
densidad_agua = 1.0  # densidad del agua (kg/m^3)
densidad_aire = 1.2  # densidad del aire (kg/m^3)

# Variables de estado
estado = {
    "altura": altura_inicial,
    "velocidad": 0.0,
    "aceleracion": 0.0,
    "masa_total": masa_cohete + masa_agua,
    "tiempo_actual": 0.0,
    "distancia_recorrida": 0.0
}
# Lista para almacenar los datos de la simulación
datos_simulacion = []

# Simulación
while estado["altura"] >= altura_inicial and estado["tiempo_actual"] <= tiempo_total:
    # Cálculo de la fuerza de empuje
    volumen_agua = masa_agua / densidad_agua  # volumen de agua expulsada (m^3)
    fuerza_empuje = volumen_agua * velocidad_salida * densidad_agua * gravedad

    # Cálculo de la fuerza de arrastre
    fuerza_arrastre = 0.5 * coeficiente_arrastre * densidad_aire * area_seccion_transversal * estado["velocidad"] ** 2

    # Cálculo de la aceleración resultante
    estado["aceleracion"] = (fuerza_empuje - fuerza_arrastre - estado["masa_total"] * gravedad) / estado["masa_total"]

    # Actualización de la velocidad y la altura
    estado["velocidad"] += estado["aceleracion"] * delta_tiempo
    estado["altura"] += estado["velocidad"] * delta_tiempo

    # Actualización del tiempo y la distancia recorrida
    estado["tiempo_actual"] += delta_tiempo
    estado["distancia_recorrida"] += estado["velocidad"] * delta_tiempo

    # Si el cohete ha agotado el agua, la fuerza de empuje es cero
    if masa_agua <= 0.0:
        fuerza_empuje = 0.0

    # Actualización de la masa total del cohete
    estado["masa_total"] = masa_cohete + masa_agua
   # Almacenar datos de la simulación en la lista
    datos_simulacion.append((estado["distancia_recorrida"], estado["altura"]))

# Calcular la distancia máxima alcanzada y la altura máxima alcanzada
distancia_maxima = max([datos[0] for datos in datos_simulacion])
altura_maxima = max([datos[1] for datos in datos_simulacion])

# Calcular la distancia recorrida
distancia_recorrida = estado["distancia_recorrida"]

# Mostrar resultados en consola
print("Distancia máxima: ", distancia_maxima, "m")
print("Altura máxima: ", altura_maxima, "m")
