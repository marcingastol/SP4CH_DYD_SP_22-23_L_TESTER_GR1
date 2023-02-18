# Zdefiniuj funkcję, która będzie pobierała dwie wartości liczbowe 
# i zwracała sumę tych wartości 

def suma_sposob_1(liczba1,liczba2):
    return liczba1 + liczba2

def suma_sposob_2(liczba1,liczba2):
    suma = liczba1 + liczba2
    return suma

print(suma_sposob_1(3,5))
print(suma_sposob_2(3,5))

# Zdefiniuj funkcję, która będzie pobierała dwie wartości liczbowe 
# i zwracała sumę oraz różnicę tych wartości w jednym poleceniu return

def suma_roznica_sposob_1(liczba1,liczba2):
    return liczba1 + liczba2, liczba1 - liczba2

def suma_roznica_sposob_2(liczba1,liczba2):
    dodawanie = liczba1 + liczba2
    odejmowanie = liczba1 - liczba2
    return dodawanie, odejmowanie

print(suma_roznica_sposob_1(10,3))
print(suma_roznica_sposob_2(10,3))

# Zdefiniuj funkcję, która pobierze jedną wartość liczbową i wykona takie założenia:
# - jeśli zostanie przekazana wartość argumentu podczas odwołania się do funkcji, 
#   to zwraca kwadrat tej liczby
# - jeśli nie zostanie przekazana żadna wartość do funkcji, to zwraca liczbę 0 (zero)

def zadanie_3(liczba="hello"):
    if liczba != "hello":
        return liczba**2
    else:
        return 0

print(zadanie_3(100))