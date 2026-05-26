print("Калькулятор")
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = input("Введите знак операции: ")
otvet=0.0
if z =="+":
    otvet=x+y
elif z=="-":
    otvet=x-y
elif z=="*":
    otvet=x*y
elif z=="/":
    otvet=x/y
print(otvet)