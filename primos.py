#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPrime(num):
    for i in range(2, num):  # Recorro los numeros desde 2 hasta el deseado
        if num % i == 0:    # Si el resto de division entera en 0 no es primo
            return False
    return True


def sumPrimeNumbersbetween0and50(): # Obtengo la suma de los numero primos entre 0 y 50
    sum = 0
    for i in range(50):
        if isPrime(i): sum += i
    print (sum)

def sumFirst50PrimeNumbers():
    sum = i = count = 0
    while count <= 50:
        if isPrime(i):
            sum += i
            count += 1
        i += 1
    print (sum)

# Console Out
print("\n")
print ('Suma de los números primos de 0 a 50: ')
sumPrimeNumbersbetween0and50()
print("\n")
print ('Suma de los primeros 50 números primos: ')
sumFirst50PrimeNumbers()
print("\n")

# cambio para push
