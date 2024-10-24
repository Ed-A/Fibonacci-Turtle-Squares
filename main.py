from turtle import *

forward(10)
i = 1
while i <= 3:
    right(90)
    forward(10)
    i += 1

fibo0 = 0
fibo1 = 1

i = 0
while True:
    temp = fibo1
    fibo1 = fibo0 + fibo1
    forward(10 * fibo1)
    i = 1
    while i <= 4:
        right(90)
        forward(10 * fibo1)
        i += 1
    right(90)
    forward(10 * fibo1)
    fibo0 = temp
