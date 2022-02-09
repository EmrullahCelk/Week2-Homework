list = int(input("Enter a number for list: "))
number =int(input("Enter a number: "))

list = [x for x in range(1, list+1)]
print(list)

if number > 0:
    x = list[-number:] + list[:len(list)-number]
    print(x)
else:
    x = list[-number:] + list[:-number]
    print(x)
