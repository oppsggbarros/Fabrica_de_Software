import math

'''x = float(input("x: "))
y = float(input("y: "))


print(math.ceil(x))#Arrendonda pra cima
print(math.fabs(x))#Valor absoluto
x = int(x)
print(math.factorial(x))#Fatorial
print(math.isqrt(x))
print(math.sqrt(x))
print(math.pow(x,y))'''

import datetime as dt

'''print(dt.date.today())
print(dt.date.today().strftime('%d/%m/%Y'))
print(dt.datetime.now())
print(dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))'''

import time

'''a = 0
x = time.perf_counter()
while a<100:
    print(a)
    a+=1
y=time.perf_counter()
print(y-x)'''
import secrets

random = secrets.randbelow(100)
print("\n", random)
random_bits = secrets.randbits(8)
token = secrets.token_bytes(32)
print("\n", token)
token_hex = secrets.token_hex(16)
print("\n", token_hex)
token_Url = secrets.token_urlsafe(16)
print("\n", token_Url)
random = secrets.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('\n', random)
