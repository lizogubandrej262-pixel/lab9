import string

T = ("Київ", 3.5, 10, " Харків", 2.5, 7, 4.0, "Одеса", 1.0, 42)
print("Кортеж:", T)
 
summa = 0
N = 0
for elem in T:
    if type(elem) == float:      
        summa = summa + elem
        N = N + 1
 
if N > 0:
    print("Дійсних чисел:", N)
    print("Середнє арифметичне =", summa / N)
else:
    print("у кортежі немає дійсних чисел")
