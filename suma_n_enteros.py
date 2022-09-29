# Suma de los primeros N primeros numeros positivos
print("---Suma-de-N-positivos----")

N = int(input("Ingrese el valor de N: "))

# Proceaaing
i = 1
sum = 0

while i <= N:
    sum= sum + i
    i = i + 1

# Output
print("la suma es :" + str (sum))