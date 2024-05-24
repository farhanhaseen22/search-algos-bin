def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    value = None
    while True:
        try:
            value = x / y
            break
        except ZeroDivisionError:
            print('Value is not dividable by 0, try again')
            break
    return value


def exponent(x, y):
    X1 = None
    
    return x * y


def num_input(prompt='Enter a number: '):
    while True:
        try:
            print(prompt, end='')
            x = int(input())
            break
        except ValueError:
            print('You must input a number. Try again.')
    return x


def get_two_val():
    x, y = num_input(), num_input()
    return x, y


print("Welcome to Simple Calc")

# declaration of variables
num_of_calc_counter = 0
index_of_calc = 1
calculations = []

while True:

    print("Choose from the following options:")
    print(" 1. Add")
    print(" 2. Subtract")
    print(" 3. Multiply")
    print(" 4. Divide")
    print(" 5. Sales Tax Calculator")
    print(" 6. Recent Calculations")
    print(" 0. Quit")

    usrChoice = num_input('Enter your choice: ')

    '''
    Menu workflow
        options 1-4 take in two numbers and perform the specified calculation and
        then add the result to a master list that the user can reference later.
        lastly, the workflow increments the num_of_calc variable by 1 for recent
        calc logic

        option 5 is a simple tax calculator that needs work or option to enter
        or find tax rate

        option 6 returns a list of all the calculations perform by the user
    '''
    if usrChoice is 1:
        numbers = get_two_val()
        result = add(*numbers)
        print(numbers[0], "plus", numbers[1], "equals", result)
        calculations.extend([result])
        num_of_calc_counter += 1

    elif usrChoice is 2:
        numbers = get_two_val()
        result = sub(*numbers)
        print(numbers[0], "minus", numbers[1], "equals", result)
        calculations.extend([result])
        num_of_calc_counter += 1

    elif usrChoice is 3:
        numbers = get_two_val()
        result = mul(*numbers)
        print(numbers[0], "times", numbers[1], "equals", result)
        calculations.extend([result])
        num_of_calc_counter += 1

    elif usrChoice is 4:
        numbers = get_two_val()
        result = div(*numbers)
        print(numbers[0], "divided by", numbers[1], "equals", result)
        calculations.extend([result])
        num_of_calc_counter += 1

    elif usrChoice is 5:
        tax_rate = .0875
        price = float(input("What is the price?: "))
        total_tax = tax_rate * price
        final_amount = total_tax + price
        print('Tax rate: ', tax_rate, '%')
        print('Sales tax: $', total_tax)
        print('_____________________________')
        print('Final amount: $', final_amount)
    #
    elif usrChoice is 6:
        if len(calculations) is 0:
            print('There are no calculations')
        elif num_of_calc_counter == 0:
            index_of_calc = 1
            for i in calculations:
                print(index_of_calc, i)
                index_of_calc += 1
            num_of_calc_counter += 1
        elif index_of_calc == num_of_calc_counter:
            index_of_calc = 1
            for i in calculations:
                print(index_of_calc, i)
                index_of_calc += 1
            num_of_calc_counter += 1
        elif num_of_calc_counter > index_of_calc:
            index_of_calc = 1
            for i in calculations:
                print(index_of_calc, i)
                index_of_calc += 1
            num_of_calc_counter -= 1
        elif num_of_calc_counter < index_of_calc:
            index_of_calc = 1
            for i in calculations:
                print(index_of_calc, i)
                index_of_calc += 1
            num_of_calc_counter += 1

    elif usrChoice is 0:
        break
