"""Homework 3"""

#function: histogram(list)

## Did not use DocStrings for your headers - Prof G

def histogram(list):
    str = '*'
    for num in list:
        line = num * str
        print (line)

#histogram(list)


#function: max_in_list(num_list)

num_list = [48,89,23,51,26]

def max_in_list(num_list):
    max_num = num_list[0]
    if len(num_list) is 1: 
        return max_num
    else:
        for num in num_list[1:]:
            if num >= max_num: 
                max_num = num     
    return max_num

#max_in_list(num_list)


#function: lengths_of_words(word_list)

word_list = ('popular', 'Iowa', 'car')

def mylen(str):
    length = 0
    for chr in str:
        length += 1
    return (length)

def lengths_of_words(word_list):

    length_list = []
    for str in word_list:
        length_list.append(mylen(str))
    return length_list

#lengths_of_words(word_list)


#function: find_longest_word(word_list)

def find_longest_word(list):
    return max_in_list(lengths_of_words(word_list))

#find_longest_word(list)


#filter_long_words

def filter_long_words(word_list, n):
    long_words = []
    length_list = lengths_of_words(word_list)
    for i in range(len(length_list)):
        if length_list[i] > n:
            long_words.append(word_list[i])
    return long_words
#filter_long_words(word_list, 3)


#function: is_phrase_palindrome(str)

import re

def is_phrase_palindrome(str):
    str = re.sub('[^a-zA-Z0-9]','',str)
    back_str = str[::-1]
    if str.lower() == back_str.lower():
        return True
    else:
        return False

#is_phrase_palindrome('Was it a rat I saw?')


#function: is_pangram(str)

def is_pangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_count = 0
    for chr in str:
        if chr in alphabet:
            alphabet_count += 1
        if alphabet_count == 26:
            return True
    for chr in alphabet:
        if chr not in str:
            return False
        
#is_pangram('The quick brown fox jumps over the lazy dog.')


#function: 99_Bottles
count = 9
while count > 0:
    print(count, "bottles of coke on the wall,", count, "bottles of coke. "
    "Take one down, pass it around,", (count - 1), "bottles of coke on the wall.")
    count -= 1


#function: Eng_to_Swed(dictionary)

## Specification is to accept a list of words, not a single string containing multiple words - Prof G
def translate(str_to_trans):
    dictionary = {'merry':'god',
                   'christmas':'jul',
                   'and':'och',
                   'happy':'gott',
                   'new':'nytt',
                   'year':'år'}
    import re
    trans_str = ''
    for i in str_to_trans.split(' '):
        if (str(dictionary.get(i))):
            trans_str = trans_str+str(dictionary.get(i))+' '
        else:
            trans_str = ''
            return trans_str
    return trans_str
#translate('merry christmas and happy new year')


#function: char_freq(str)

def char_freq(str):
    dictionary = {}
    KeyWord = ''
    print(str)
    for i in range(len(str)):
        if str[i] in dictionary:
            dictionary[str[i]] = int(dictionary.get(str[i])) + 1
        else:
            dictionary[str[i]] = 1
    return dictionary
    
#char_freq("dfadef")


#function: ROT_13(str)

## This is global but should be defined in the function

key = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u',
    'i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c',
    'q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k',
    'y':'l','z':'m','A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S',
    'G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A',
    'O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I',
    'W':'J','X':'K','Y':'L','Z':'M'}
    
def ROT_13(str):
    import re
    newString = ''
    for word in (re.findall('[a-zA-Z0-9?!]+', str)):
        for j in range(len(word)):
            if word[j] in key:
                newString = newString+key[word[j]]
            else:
                newString = newString+word[j]
        newString = newString+" "
    return newString
    ##print(newString) Should return a string not print to the screen
    
#ROT_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')


#function: correct(str)

def correct(str):
    import re
    return re.sub(r'\.\s*(?!$)', r'. ', re.sub(r'\s+', ' ',str))

#correct('This  is very funny and   cool.Indeed!')


#function: make_3sg_form(str)

## Function does not work correctly in all cases - Prof G
def make_3sg_form(str):
    if str.endswith('y'):
        third_sing_form = str[:-1] + 'ies'
    elif str.endswith('o,ch,s,sh,x,z'):
        third_sing_form = str + 'es'
    else:
        third_sing_form = str + 's'
        
    return third_sing_form

#make_3sg_form('berry')


#function: make_ing_form(str)

cons = 'bcdfghjklmnpqrstvwxz'
vowel = 'aeiouy'

## Function does not work correctly in all cases - Prof G
def make_ing_form(str):
    if str.endswith('e'):
        return str[:-1] + 'ing'

    elif str.endswith('ee'):
        return str[:-1] + 'ing'

    elif str.endswith('ie'):
        pres_part = str[:-2] + 'ying'

    elif str.endswith(cons + vowel + cons):
        pres_part = str + (cons * 2) + 'ing'
    else:
        return str + 'ing'

#make_ing_form('try')

##Test Cases

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", lengths_of_words(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_words(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", is_phrase_palindrome("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", is_pangram("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", )

#print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')
print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate('merry christmas happy'), '\n')

print("10 Char Freq {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')

print("11 Decoder Caesar cipher? I much prefer Caesar salad!", ROT_13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')