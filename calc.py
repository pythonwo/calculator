number_1 = 0
number_2 = 0
char = "-"
count = 0
error = False
q = False
while q==False:
    number_1 = float(input("Введите первое число - "))
    char = input("Введите оператор(+, -, *, /) - ")
    number_2 = float(input("Введите второе число - "))
    if char == "+":
        count = number_1 + number_2
        print(count)
    elif char == "-":
        count = number_1 + number_2
        print(count)
    elif char == "/":
        count = number_1 / number_2
        print(count)
    elif char == "*":
        count = number_1 * number_2
        print(count)
    else:
        error = True

            
        
