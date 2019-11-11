# Python program to print all prime numbers given an interval
def inputDigit(message):

    while True:
        value = input(f"Enter {message} number: ")
        if value.isdigit():
            break
        else:
            print("You need to enter an integer. Try again.")

    return(int(value))


print("Python program to print all prime numbers given an interval")

start = inputDigit('start')
end = inputDigit('stop')


for number in range(start, end + 1):
    prime = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                prime = False
                break
    if prime is True:
        print(number)
