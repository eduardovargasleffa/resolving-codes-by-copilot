# we will request a string and an integer number as input. Then we will have to return the string repeated string the number of times informed.

number = int(input('Write a number: '))
string = input('Write a string: ')

# # we will return the string repeated the number of times informed
def repeat_string(string, number):
    return ((string  + "\n") * number)

print('The string repeated the number of times is: ', repeat_string(string, number))
