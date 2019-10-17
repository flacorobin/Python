#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
#Prints the Fibonacci sequence up to Nth digit. Saves on list, displays the list.
def input_control():
    value_NotOk = True
    value = 0
    while value_NotOk:
        value = input('Choose an upper limit: ')
        if (not value.isdigit()):
            print("Input is not a number")
        else:
            value = int(value)
            if value <= 3:
                print("Number needs to be 3 or higher")
            else:
                value_NotOk = False

    return value

def Fibonacci(limit):
    Fibonacci_array = [int(0), int(1)]
    while Fibonacci_array[len(Fibonacci_array)-1] < limit:
        new_num = Fibonacci_array[len(Fibonacci_array)-2] + Fibonacci_array[len(Fibonacci_array)-1]
        Fibonacci_array.append(new_num)

    Fibonacci_array.pop(len(Fibonacci_array)-1)
    return Fibonacci_array


print("This script prints the Fibonacci sequence.")
limit = input_control()
array = Fibonacci(limit)
print(array)
