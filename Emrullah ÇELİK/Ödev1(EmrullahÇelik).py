number = int(input("Enter a number please: "))

number1 = [x for x in range(number) if x != 0 ]
number1.append(number)
print(number1)
x, y= 2, 1
while len(number1) > x:
    del number1[y::x]
    print(number1)
    x += 1
    y += 1