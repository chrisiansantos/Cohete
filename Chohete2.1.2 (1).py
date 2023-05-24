import math
from builtins import enumerate
import numpy as np
import matplotlib.pyplot as plt

# Definición de constantes
g = 9.81  # Aceleración gravitatoria
rho = 1000  # Densidad del agua
Cd = 0.75  # Coeficiente de resistencia del aire
A = 0.001  # Área transversal del cohete
m = 0.2  # Masa del cohete
v0 = 20  # Velocidad inicial

print("Seleccione que modalidad desea que se ejecute: ")
print("1. Altura maxima.")
print("2. Distancia horizontal maxima.")
print("3. Lanzamiento de precision.")
print("4. Trayectoria")
selection = int(input())

# Definición de funciones
if selection == 1:
    def altura_maxima(angulo):
        masa_agua = 0.5
        masa_cohete = 0.125
        presion_chorro = 344738
        area_boquilla = 0.001
        area_cohete = 0.01
        rho_agua = 1000

        velocidad_chorro = math.sqrt((2 * presion_chorro) / (rho_agua * (1 - (area_boquilla / area_cohete))))
        velocidad_inicial = (masa_agua * velocidad_chorro) / (masa_cohete + masa_agua)

        theta_rad = math.radians(angulo)
        h = (velocidad_inicial ** 2 * math.sin(theta_rad) ** 2) / (2 * g)
        return h


    # Crear listas para almacenar los ángulos y alturas máximas
    angulos = list(range(0, 91, 5))
    alturas_maximas = []

    # Calcular las alturas máximas para cada ángulo
    for angulo in angulos:
        h_max = altura_maxima(angulo)
        alturas_maximas.append(h_max)

    # Graficar los resultados
    plt.plot(angulos, alturas_maximas)
    plt.title("Altura máxima vs Ángulo de lanzamiento")
    plt.xlabel("Ángulo de lanzamiento (grados)")
    plt.ylabel("Altura máxima (m)")
    plt.grid(True)
    plt.show()

    # Obtener y mostrar la altura máxima máxima
    altura_maxima_maxima = max(alturas_maximas)
    indice_maxima = alturas_maximas.index(altura_maxima_maxima)
    angulo_maxima = angulos[indice_maxima]
    print("Altura máxima alcanzada: {:.2f} m".format(altura_maxima_maxima))
    print("Ángulo de lanzamiento correspondiente: {} grados".format(angulo_maxima))

elif selection == 2:
    def distancia_maxima(angulo):
        masa_agua = 0.5  # Masa de agua expulsada en kilogramos
        masa_cohete = 0.125  # Masa del cohete sin agua en kilogramos
        presion_chorro = 344738  # Presión generada por el sistema de propulsión en pascales
        area_boquilla = 0.001  # Área de la boquilla del cohete en metros cuadrados
        area_cohete = 0.01  # Área de la sección transversal del cohete en metros cuadrados
        rho_agua = 1000

        velocidad_chorro = math.sqrt((2 * presion_chorro) / (rho_agua * (1 - (area_boquilla / area_cohete))))
        velocidad_inicial = (masa_agua * velocidad_chorro) / (masa_cohete + masa_agua)

        theta_rad = math.radians(angulo)
        d = (velocidad_inicial ** 2 * math.sin(2 * theta_rad)) / g
        return d

    # Crear una lista de ángulos
    angulos = list(range(0, 91, 5))

    # Calcular las distancias máximas para cada ángulo
    distancias_maximas = [distancia_maxima(angulo) for angulo in angulos]

    # Graficar los resultados
    plt.plot(angulos, distancias_maximas)
    plt.title("Distancia máxima vs Ángulo de lanzamiento")
    plt.xlabel("Ángulo de lanzamiento (grados)")
    plt.ylabel("Distancia máxima (m)")
    plt.grid(True)
    plt.show()

    # Obtener y mostrar la distancia máxima máxima
    distancia_maxima_maxima = max(distancias_maximas)
    indice_maxima = distancias_maximas.index(distancia_maxima_maxima)
    angulo_maxima = angulos[indice_maxima]
    print("Distancia máxima alcanzada: {:.2f} m".format(distancia_maxima_maxima))
    print("Ángulo de lanzamiento correspondiente: {} grados".format(angulo_maxima))

elif selection == 3:
    def encontrar_angulo_lanzamiento_deseado():
        theta = 15
        R = 2
        theta_rad = math.radians(theta)
        v0 = math.sqrt((R * g) / math.sin(2 * theta_rad))

        d = (v0 ** 2 * math.sin(2 * theta_rad)) / g
        return d


    def calcular_distancia_deseada(velocidad):
        theta = 15
        theta_rad = math.radians(theta)
        v0 = velocidad

        d = (v0 ** 2 * math.sin(2 * theta_rad)) / g
        return d


    # Rango de velocidades
    velocidades = list(range(1, 50, 1))

    # Calcular las distancias para cada velocidad
    distancias = []
    for velocidad in velocidades:
        distancia = calcular_distancia_deseada(velocidad)
        distancias.append(distancia)

    # Graficar los resultados
    plt.plot(velocidades, distancias)
    plt.axhline(y=2, color='r', linestyle='--', label='Distancia deseada')
    plt.title("Distancia vs Velocidad")
    plt.xlabel("Velocidad (m/s)")
    plt.ylabel("Distancia (m)")
    plt.grid(True)
    plt.legend()
    plt.show()

elif selection == 4:
    def trayectoria_cohete_agua(v0, theta):
        masa_agua = 0.5  # Masa de agua expulsada en kilogramos
        masa_cohete = 0.125  # Masa del cohete sin agua en kilogramos
        presion_chorro = 344738  # Presión generada por el sistema de propulsión en pascales
        area_boquilla = 0.001  # Área de la boquilla del cohete en metros cuadrados
        area_cohete = 0.01  # Área de la sección transversal del cohete en metros cuadrados
        rho_agua = 1000

        velocidad_chorro = math.sqrt((2 * presion_chorro) / (rho_agua * (1 - (area_boquilla / area_cohete))))
        velocidad_inicial = (masa_agua * velocidad_chorro) / (masa_cohete + masa_agua)

        theta_rad = math.radians(theta)
        t_total = (2 * velocidad_inicial * math.sin(theta_rad)) / g  # Tiempo total de vuelo
        t = np.linspace(0, t_total, num=100)  # Vector de tiempo
        x = velocidad_inicial * np.cos(theta_rad) * t  # Distancia horizontal
        y = velocidad_inicial * np.sin(theta_rad) * t - 0.5 * g * t ** 2  # Altura vertical

        # Graficar la trayectoria
        plt.plot(x, y)
        plt.title("Trayectoria del cohete de agua")
        plt.xlabel("Distancia Horizontal (m)")
        plt.ylabel("Altura Vertical (m)")
        plt.ylim(bottom=0)  # Establecer límite inferior de la altura en 0
        plt.xlim(left=0)  # Establecer límite inferior de la distancia en 0
        plt.show()


    # Llamar a la función trayectoria_cohete_agua con v0 = 20 y theta = 45
    trayectoria_cohete_agua(20, 45)
# Prueba de las funciones
if selection == 1:
    print("Altura máxima: {:.2f} m".format(altura_maxima(angulo)))
elif selection == 2:
    print("Distancia máxima : {:.2f} m".format(distancia_maxima_maxima))
elif selection ==3:
    print("Lanzamiento de precision: {:.2f} m".format(encontrar_angulo_lanzamiento_deseado()))
elif selection == 4:
    plt.show()
else:
    print("Selección inválida.")


