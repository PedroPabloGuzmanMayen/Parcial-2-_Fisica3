import numpy as np
import scipy.integrate as integrate

"""Calcula la capacidad de un condensador esférico.
    Args:
        r1: El radio de la esfera interna.
        r2: El radio de la esfera externa.
        epsilon: La permitividad del dieléctrico entre las esferas.

    Return:
        La capacidad del condensador esférico en faradios.
"""

def spherical_capacitor_capacity(r1, r2, epsilon):

    def integrand(x):
      if x ==r1:
        return 0
      else:
        return 4 * np.pi * epsilon * x**2 / (x**2 - r1**2)

    integral = integrate.quad(integrand, r1, r2)
    capacity = integral[0]

    return capacity

def main():
    r1 = float(input("Ingrese el radio de la esfera interna: "))
    r2 = float(input("Ingrese el radio de la esfera externa: "))
    epsilon = float(input("Ingrese la permitividad del dieléctrico: "))

    capacity = spherical_capacitor_capacity(r1, r2, epsilon)

    print("La capacidad del condensador esférico es de {} faradios.".format(capacity))
#pinche pedro
main()
