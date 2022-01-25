

# Excercise 1

while True:
    calculation = input('please enter: divide, add multiply or subtract. ')
    message = input('enter "quit" when you are finished. Press "Enter to continue.')


    x = int(input('please enter first number: '))
    y = int(input('please enter second number: '))


    def arithmetic(a, b):
        if calculation == 'add':
             print(a + b)
        elif calculation == 'subtract':
            print(a - b)
        elif calculation == 'multiply':
            print(a * b)
        elif calculation == 'divide':
            print(a / b)



#     arithmetic(x, y)


# Exercise 2




    for i in range(5):
        for j in range(i + 1):
            print('x', end ='')
        print()
    



