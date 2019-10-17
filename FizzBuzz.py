#https://www.hackerrank.com/challenges/fizzbuzz/problem
#Write a short program that prints each number from 1 to 100 on a new line. For each multiple of 3, print "Fizz" instead of the number. For each multiple of 5, print "Buzz" instead of the number. For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

print("FizzBuzz program for numbres from 1 to 100.")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num}: FizzBuzz")
    elif num % 3 == 0:
        print(f"{num}: Fizz")
    elif num %5 == 0:
        print(f"{num}: Buzz")
    else:
        print(num)
