# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. File are FileOverlap_happynumbers.txt and FileOverlap_primenumbers.txt

list_to_show = []
with open('FileOverlap_happynumbers.txt', 'r') as f1:
    happylist = f1.readlines()
    with open('FileOverlap_primenumbers.txt', 'r') as f2:
        primelist = f2.readlines()
        for i in happylist:
            for j in primelist:
                if i == j:
                    list_to_show.append(int(i))

print("The list of overlapping number is the following:\n", list_to_show)
sum = 0
for i in range(len(list_to_show)):
    sum = sum + list_to_show[i]

print("The sum of numbers is: ", sum)
