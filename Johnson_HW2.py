## Need to write doc string headers for all your functions.

"""Exercise 2.1"""

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    return (a)
fib (500)

"""Exercise 2.2"""

#function: mymax(num1,num2)

def mymax(num1,num2): 
    if num1 >= num2:
        return num1
    else:
        return num2
mymax(18,88)

"""Exercise 2.3"""

#function: max_of_three(num1, num2, num3)

def max_of_three(num1,num2,num3):
    return mymax(mymax(num1,num2),num3)
max_of_three(17,56,7)

"""Exercise 2.4"""

#function: mylen(str)

def mylen(str):
    length = 0
    for chr in str:
        length += 1
    return (length)    
mylen('values')

"""Exercise 2.5"""

#function: identify_vowel(chr)

def identify_vowel(chr):
    vowel = 'aeiouy'
    if chr == vowel:
        return True   
    else:
        return False
identify_vowel('u')

"""Exercise 2.6"""

#function: translate(str)
## The else is not at the propoer level and doesn't work as you might expect
def translate(str):
    consonant = 'bcdfghjklmnpqrstvwxz'
    ret_str = ''
    for letter in str:
        if letter in consonant:
            ret_str += letter + 'o' + letter
    else: 
        ret_str += letter
    return ret_str
translate('this is fun')

"""Exercise 2.7"""

#function: sum(list)

def sum(list):
    #list = [7,8,9] ## This should not have been initialized in the function
    sum=0
    for num in list:
        sum = sum + num
    return(sum)

#sum(list)

#function: multiply(list)

def multiply(list):
    ##list = [7,8,9] ## This should not have been initialized in the function
    product = 1
    for x in list:
        product *= x
    return product
#multiply(list)

"""Exercise 2.8"""

#function: reverse()

def reverse(str):
    return(str[::-1])

reverse('This is a milestone.')

"""Exercise 2.9"""

#function: is_palindrome()

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

is_palindrome('radar')

"""Exercise 2.10"""

#function: is_member()
## This function should have two parameters
# def is_member(value):
#     a = ['c','5','N','street']
#     for str in a:
#         if value == str:
#             return True
#     else:
#         return False
#
# is_member('motorcycle')

"""Exercise 2.11"""

#function: overlapping()

list1 = [3, 6, 9, 12]
list2 = [2, 4, 6, 8, 10, 12]

def overlapping(list1,list2):
    for element in list1:
        if element in list2:
            return True
    else:
        return False
        
overlapping(list1,list2)

"""Exercise 2.12"""

#function: generate_n_chars()

def generate_n_chars(num, str):
    generated_string = num * str
    return(generated_string)
    
generate_n_chars(6,'u')

print('\n#1\n')
fib(500)
print('\n')

print('#2\n')
print(mymax(45,987), '\n')

print('#3\n')
print(max_of_three(3,4,5),'\n')

print('#4\n')
print(mylen('Gerhard'))
print(mylen([1,2,3,4,5,6,7]))
print('\n')

print('#5\n')
print(identify_vowel('e'))
print(identify_vowel('H'))
print('\n')

print('#6\n')
print(translate("this is fun"))
print(translate('aeiou'))
print(translate('YYYYYYY'))
print(translate("mmmmmm"))
print('\n')

print('#7\n')
print(sum([1,2,3,4,5]))
print('\n')

print('#8\n')
print(multiply([0,1,2,3]))
print(multiply([1,2,3,4]))
print('\n')

print('#9\n')
print(reverse("gnitset ma I"))
print('\n')

print('#10\n')
print(is_palindrome('radar'))
print(is_palindrome('Gerhard'))
print('\n')

print('#11\n')
# print(is_member('dog', ['cat', 'dog', 'zebra']))
# print(is_member(3, [1,2,3,4]))
# print(is_member(3, [5,6,7]))
print('\n')

print('#12\n')
print(overlapping([1,2,3], [3,4,5]))
print(overlapping([1,2,3], [6,4,5]))
print('\n')

print('#13\n')
print(generate_n_chars(7, 'g'))