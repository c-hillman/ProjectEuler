"""Some functions that will help dealing with division and primes.
All functions take abs() and int() of all numbers passed to them.
"""

def isPrime(n):
    """(bool) Returns true if n is a prime integer."""
    n = abs(int(n))
    
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True

def Eratos(limit):
    """Returns a list of prime integers, where 0 < x <= limit.
    Code based on the Sieve of Eratosthenes."""
    n = abs(int(limit))
    if limit < 2: return []
    
    primes = {}
    for n in range(2, limit + 1): primes[n] = True

    for n in primes:
        for f in range(n*2, limit + 1, n): primes[f] = False
    return [n for n in primes if primes[n] == True]

def invEratos(limit):
    """Returns list of composite integers where 0 < x <= limit.
    Inverse of Eratos(limit)."""
    n = abs(int(limit))
    nonprimes = [1]
    if limit < 2: return nonprimes

    primes = {}
    for n in range(2, limit + 1): primes[n] = True

    for n in primes:
        for f in range(n*2, limit + 1, n): primes[f] = False
    nonprimes.extend([n for n in primes if primes[n] == False])
    return nonprimes

def primfac(n, form='l'):
    """Returns a list or dictionary of n's prime factors.

    form='l': 'list' (DEFAULT)
    eg. primfac(72) = [2, 2, 2, 3, 3]

    form='d': 'dictionary', such that 
    prime factors : exponent of prime factor.
    eg. primeFactorsDict(90) = {2: 1, 3: 2, 5: 1}
    Such that 90 = 2^1 * 3^2 * 5^1"""
    n = abs(int(n))
    if form == "d" or form == "D": factors = {}
    else: factors = []

    for div in range(2, int(n**0.5) + 2): # +1 for range(), +1 for ceil round
        while n%div == 0:
            if type(factors) == list:
                factors.append(div)
            else:
                if div not in factors: factors[int(div)] = 1
                else: factors[int(div)] += 1
            n /= div
    if n > 1:
        if type(factors) == list:
            factors.append(int(n))
        else:
            if n not in factors: factors[int(n)] = 1
            else: factors[int(n)] += 1
    return factors

def divnum(n):
    """Returns the number of integers that divide evenly into n."""
    n = abs(int(n))
    
    product = 1
    for item in primfac(n, form='d').values():
        product *= (item + 1)
    return product

def divisors(n):
    """Returns a sorted list of integers that divide evenly
    into n (including n)."""
    n = abs(int(n))

    divs = [x for x in range(1, int(n/2) + 1) if n%x == 0]
    divs.append(n)
    return divs

def Collatz(n):
    """Returns n's Collatz sequence."""
    n = abs(int(n))
    
    steps = [n]
    while n > 1:
        if n % 2 == 0: n /= 2
        else: n = (n*3) + 1
        steps.append(int(n))
    return steps

def GCD(*args):
    """Returns the greatest common divisor of any number of numbers."""
    args = list(map(abs, map(int, args)))
    
    if len(args) == 1: return args[0]
    while len(args) > 2: #GCD(a, b, c) = GCD(a, GCD(b, c))
        args.append(GCD(args.pop(), args.pop()))

    a, b = args
    while b != 0:
        a, b = b, a%b
    return a

def LCM(*args):
    """Returns the lowest common multiple of any number of numbers."""
    args = list(map(abs, map(int, args)))
    
    if len(args) == 1: return args[0]
    while len(args) > 2: #LCM(a, b, c) = LCM(a, GCD(b, c))
        args.append(LCM(args.pop(), args.pop()))

    a, b = args
    return int(a*b / GCD(a, b)) #LCM(a, b) = a*b / GCD(a, b)
