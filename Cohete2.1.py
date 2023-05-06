import math
import matplotlib.pyplot as plt

# Definición de constantes
g = 9.81  # Aceleración gravitatoria
rho = 1000  # Densidad del agua
Cd = 0.75  # Coeficiente de resistencia del aire
A = 0.001  # Área transversal del cohete
m = 0.2  # Masa del cohete
v0 = 10  # Velocidad inicial

# Definición de funciones
def altura_maxima():
    h = (m/(2*rho*A*math.sqrt(2*g)))*math.log(1+Cd*rho*A*v0**2/(2*m*g))
    return h

def distancia_maxima():
    d = (m*v0)/(Cd*rho*A*math.sqrt(2*g))
    return d

def trayectoria():
    dt = 0.01  # Intervalo de tiempo
    t = 0
    x = 0  # Posición horizontal inicial
    y = 0  # Posición vertical inicial
    vx = v0  # Velocidad horizontal inicial
    vy = v0  # Velocidad vertical inicial
    datos_x = [x]  # Lista para guardar las posiciones horizontales
    datos_y = [y]  # Lista para guardar las posiciones verticales

    while y >= 0:
        # Cálculo de la fuerza de arrastre
        Fd = 0.5*Cd*rho*A*vy**2
        # Cálculo de la fuerza gravitatoria
        Fg = m*g
        # Cálculo de la fuerza total
        Ft = Fg - Fd
        # Cálculo de la aceleración
        ax = -Fd/m
        ay = -g - Fg/m
        # Cálculo de la nueva posición y velocidad
        x = x + vx*dt
        y = y + vy*dt
        vx = vx + ax*dt
        vy = vy + ay*dt
        # Agregamos las posiciones a las listas
        datos_x.append(x)
        datos_y.append(y)
        # Actualizamos el tiempo
        t = t + dt

    return datos_x, datos_y

# Prueba de las funciones
print("Altura máxima: {:.2f} m".format(altura_maxima()))
print("Distancia máxima: {:.2f} m".format(distancia_maxima()))

# Generación de la gráfica
x, y = trayectoria()
plt.plot(x, y)
plt.title("Trayectoria del cohete de agua")
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.show()
