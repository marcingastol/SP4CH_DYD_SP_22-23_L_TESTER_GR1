### Zdefiniuj pętle wyrzucającą na konsolę liczby od 1 do 10 włącznie (za pomocą pętli for)

# za pomoca petli while
a = 1

while a <= 10:
    print(a)
    a += 1

# wyswietlenie w jednym ciagu znakow
suma = ""
for c in range(1,11):
    suma = suma + " " + str(c)

print(suma)

# dodanie do listy
suma_lista = []
for d in range(1,11):
    suma_lista.append(d)

print(suma_lista)

### Ciag Fibonacci

liczba1 = 0
liczba2 = 1

print(liczba1)
print(liczba2)

iteracja = 0

while iteracja < 9:
    kolejna_liczba = liczba1 + liczba2
    liczba1 = liczba2
    liczba2 = kolejna_liczba

    print(kolejna_liczba)

    iteracja += 1