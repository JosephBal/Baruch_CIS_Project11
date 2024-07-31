# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:29:07 2023

@author: Joseph Balbuena
"""

# In all questions MY_WORD refers to your unique 7-letter word 
#  and MY_NUM refers to your unique 5 digit number that you selected
#  in the beginning of the term.

# the list below has some 7-letter words:
my_list = \
['qabalah','qasidas', 'qigongs','qindars','qintars','qiviuts','quacked',
'orchids','chamber','phoenix','central','juggler','dungeon','passive',
'capable','creator','rabbits','succeed','compute','achieve','attempt',
'network','address','supreme','believe','concern','explore','finance',
'quadric','quaered','quaeres','quaffed','quaffer','quaggas','quahaug',
'benifit','license','carcass','abalone','morning','abandon','macabre',
'teacher','billion','yankees','mistake','suspect','barrack','connect',
'operate','cabbage','ability','rushing','passion','perfect','fashion',
'outputs','success','banking','journal','quaichs','quaighs','quailed',
'douleia','eulogia','miaoued','moineau','sequoia','toxemia','sodaine',
'yibbles','yickers','yielded','yielder','yikkers','yippers','yippies',
'yipping','yirding','yirking','yirring','ymolten','ynambus','yobbery',
'yobbish','yobbism','yobboes','yocking','yodeled','yodeler','yodlers',
'yodling','yoghurt','yoginis','yogisms','yogurts','yohimbe','yoicked',
'yojanas','yokings','yokking','yolkier','yomping','yonders','yonkers',
'yoppers','yorkers','yorkies','yorking','youking','younger','youngly',
'youngth','younker','youpons','youthen','youthly','yowlers','yowleys',
'yowling','yperite','yplight','ypsilon','yshends','yslaked','yttrias',
'yttrium','yuchier','yuckers','yuckier','yucking','yukatas','yukiest',
'yukkier','yukking','yummier','yummies','yumpies','yumping','yuppies']

my_word = 'ORANGES'
my_num = 65875

A = 0
B = 0
C = 0

vowels = "aeiouAEIOU"

word_letters = set(my_word)
# Write python code that prints a single value (A+B+C) as defined below:
#
# A = number of CENTRIES words from my_list where the words have at least
#     3 letters in common with MY_WORD. As an example: if MY_WORD is orchids
#     then morning is such a CENTRIES word (common letters are o,r,i)

# CENTRIES are balanced and have equal number of vowels on 
# both sides. An example is 'yodeled': the first 3 letters (y,o,d) 
# has 1 vowel, and so does the last 3 letters (l,e,d)
#

def CENTRIES(word):
    list_letters = set(word)
    common_letters = list_letters.intersection(word_letters)
    if len(common_letters) >= 3:
        return False
    first_half = word[:3]
    second_half = word[-3:]
    first_half_vowels = sum(1 for letter in first_half if letter in vowels)
    second_half_vowels = sum(1 for letter in second_half if letter in vowels)
    return first_half_vowels == second_half_vowels
       
       


# B = number of LEFTIES words from my_list where the Nth index letter of 
#     the word exists in MY_WORD. Here, N is the smallest digit of MY_NUM.
#     In your case if N > 6, use N=6.  As an example: if MY_WORD is 'orchids'
#     and MY_NUM is 10233, then 'outputs' is such a LEFTIES word - the 
#     letter in 0th index is o and it exists in orchids.
# LEFTIES have more vowels (a,e,i,o,u) in the first 3 consecutive 
# letters than the last 3 consecutive letters. An example is 'youthly': 
# the first 3 letters (y,o,u) contain more vowels than the last 3 
# letters (h,l,y)
#
def LEFTIES(word):
    list_letters = set(word[5])
    common_letters = list_letters.intersection(word_letters)
    if len(common_letters) >= 1:
        return False
    first_half = word[:3]
    second_half = word[-3:]
    first_half_vowels = sum(1 for letter in first_half if letter in vowels)
    second_half_vowels = sum(1 for letter in second_half if letter in vowels)
    return first_half_vowels > second_half_vowels   



# C = number of RIGHTIES words from my_list where middle 5 letters of that
#     word has at least most three letter in common with MY_WORD. As an 
#     example: if MY_WORD is orchids, then 'sequoia' is such a word -- 
#     the middle 5 letters (equoi) has i and o in common with orchids.
# Similarly, RIGHTIES have more vowels in the last 3 consecutive letters 
# than  the first 3 consecutive letters. An example is 'dungeon': the 
# last 3  letters (e,o,n) contain more vowels than the first 3 
# letters (d,u,n)
#

def RIGHTIES(word):
    middle_part = set(word[1:6])
    common_letter = middle_part.intersection(word_letters)
    if len(common_letter) <=3 :
        return False
    first_half = word[:3]
    second_half = word[-3:]
    first_half_vowels = sum(1 for letter in first_half if letter in vowels)
    second_half_vowels = sum(1 for letter in second_half if letter in vowels)
    return first_half_vowels < second_half_vowels

         
# Make sure your program does not print anything else besides
# the computed result (A+B+C) (comment out all other extra print 
# statements)

for word in my_list:
    if CENTRIES(word):
        A += 1
    elif LEFTIES(word):
         B += 1
    elif RIGHTIES(word):
         C += 1

result = A + B + C

# The Result shouldnt be more than 133
print(result)
