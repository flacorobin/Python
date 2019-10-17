#Print uses
print('Hello World!') #Print
print('*' * 10)
print('\n')

#Python Data Types
price = 10 #Integer variables
rating = 4.9 #Floating variables
name = 'Pablo' #String variables
mylist = [1, 2.3, 'four'] #List variables use [], can hold different data types
mydictionary = {'key1':'value1', 'key2':'value2'} #Dictionaryies use {} to define [] to access. Can hold different data type
mytuple = (1, 'two', 3.4) #Tuples use (), very siilar to lists but cannot be changed
is_published = False #Boolean variables True/False are case sensitive,

#Access to lists
print("-- Lists --")
print("Print a list", mylist)
print('Print a list item mylist[0]: ', mylist[0])
print("List lenght with len(mylist): ", len(mylist))
mylist[0] = 'ONE ALL CAPS'
print("Assign new values on the list: ", mylist)
print('\n')

#Dictionaries functions
print("-- Dictionaries --")
print("Print a dictionary item mydictionary['key1']: ", mydictionary['key1'])
mydictionary['key3'] = 'value3' #Add new values to a dictionary
print(mydictionary)

keys = mydictionary.keys() #Retrieves all the keys from a dictionary
values = mydictionary.values() #Retrieves all the values from a dictionary
items = mydictionary.items() #Retrieves tuples of the key/value
print(keys, values)
print(items)
print('\n')

#Tuple functions
print("-- Tuples --")
print("Tuple lenght with len(myutple): ", len(mytuple))

mytuple = ('a', 'a', 'b')
print("Print tuple: ", mytuple)
print("Get tuple index with mytuple.index('a')", mytuple.index('a'))
print("Get tuple cout with mytuple.count('a')", mytuple.count('a'))
print('\n')

#Basic I/O with files
print("-- Basic I/O with files --")
myfile = open('AAAPythonCheat.txt')
print("myfile.read() returns the file as a string: " + myfile.read()) #Returns the whole file a one string
myfile.seek(0) #This function rewinds the cursor to 0 allowing you to read the file again
print("myfile.readlines() returns the file in separate lines in a list: ", myfile.readlines()) #Reutrns the file into a list

myfile.close() # Close a file once you have done using it

# with open('AAAPythonCheat.txt', 'a') as f:
#     f.write('\nThis is is a new line')
#
# myfile = open('AAAPythonCheat.txt')
# print(myfile.read())
# myfile.close()



print('\n')

#Transform variables into other types
print("-- Data Transformations --")
string = '10'
num1 = 10 + int(string) #transform string into Integer
string = '10.9'
float1 = 10.0 + float(string) #transform string into Floating

Boolean_string = 'False'
bool1 = bool(Boolean_string) #transform string into float

print(num1)
print(float1)
print(Boolean_string)

print(type(num1)) #prints the variable type, can do this with any variable

print('\n')


#String Methods
print("String Methods")
message = 'John Smith is a coder'
print("String length with len(string): ", len(message)) #lenght function to count characters on a strings
print(message.upper()) #UPPER CASE
print(message.lower()) #lower case
print(message.title()) #Title Case
position = message.find('coder')#looks for the string and returns the first index
print('The position for word coder starts at:', position)
print(message.replace('coder','programmer'))  #Finds one string and replaces it with another strings
print('coder' in message) #finds string in other string and returns True/False
print(message[1:-1]) #string Slice [start:finish -1]
print('\n')

#Print Formatting
first_name = 'John'
last_name = 'Smith'
print('The name is ' + first_name + ' ' + last_name) #String Concatenation
print('The name is {} {}'.format(first_name, last_name)) #String format method
print(f"{first_name} [{last_name}] is a coder") #String Interpolation

print('\n')

#Controling User Input
#Checking if an input is a number
#With Catching Exception
print('-- Controling User Input --')

user_input = input ("Enter an Integer number: ")
try:
   val = int(user_input)
   print("Value entered is a number!")
   print("Number is: ", val)
except ValueError:
   print("Not a number")

#With Value control
user_input  = input("Enter a Integer number: ")
if( user_input.isdigit()):
    print("User input is Number ")
else:
    print("User input is string ")

#Checking if the input is a float
user_input = input ("Enter a floating point value [XX.XXXX]: ")
try:
   if "." in user_input :
     val = float(user_input)
     print(val, "Yes, user input is a float number.")
   else:
      val = int(user_input)
      print(val, "Yes, input string is an Integer.")
except ValueError:
   print("No.. the input string is not a number. It's a string")
