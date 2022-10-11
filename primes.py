"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    totalPrimes = 0
    number = 3
    isPrime = True

    if number_of_primes == 0:
        return list

    list.append(2)

    while totalPrimes < number_of_primes - 1:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False

        if(isPrime == True):
            list.append(number)
            totalPrimes+= 1

        isPrime = True
        number += 1

    return list
