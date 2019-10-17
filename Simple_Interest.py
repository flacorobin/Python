# Program to calculate simple interest
# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

print('Program to calculate simple interest')
P = input('Principle Amount:' )
R = input('Rate:' )
T = input('Time:' )

SI = (int(P) * int(T) * int(R))/100

print('Simple Interest for is: ', SI)
