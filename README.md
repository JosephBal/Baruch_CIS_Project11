# Baruch_CIS_Project11
This was my final project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Description

The project includes a main.py that defines a list of 7-letter words called my_list:

```py
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
```
 
 All the words have exactly 7 letters.
 Let us define 3 categories of words: LEFTIES, RIGHTIES, and CENTRIES.

 LEFTIES have more vowels (a,e,i,o,u) in the first 3 consecutive 
 letters than the last 3 consecutive letters. An example is 'youthly': 
 the first 3 letters (y,o,u) contain more vowels than the last 3 
 letters (h,l,y)

 Similarly, RIGHTIES have more vowels in the last 3 consecutive letters 
 than in the first 3 consecutive letters. An example is 'dungeon': the 
 last 3  letters (e,o,n) contain more vowels than the first 3 
 letters (d,u,n)

 Finally, CENTRIES are balanced and have an equal number of vowels on 
 both sides. An example is 'yodeled': the first 3 letters (y,o,d) 
 has 1 vowel, and so does the last 3 letters (l,e,d)

 
 Write Python code that prints a single value (A+B+C) as defined below:

 A = number of CENTRIES words from my_list where the words have at least
     3 letters in common with MY_WORD. As an example: if MY_WORD is orchids
     then 'morning' is such a CENTRIES word (common letters are o,r,i)

 B = number of LEFTIES words from my_list where the Nth index letter of 
     the word exists in MY_WORD. Here, N is the smallest digit of MY_NUM.
     In your case if N > 6, use N=6.  As an example: if MY_WORD is 'orchids'
     and MY_NUM is 10233, then 'outputs' is such a LEFTIES word - the 
     letter in 0th index is o and it exists in orchids.

 C = number of RIGHTIES words from my_list where middle 5 letters of that
     word has at  most three letter in common with MY_WORD. As an 
     example: if MY_WORD is orchids, then 'sequoia' is such a word -- 
     the middle 5 letters (equoi) has i and o in common with orchids.
 
 Make sure your program does not print anything else besides
 the computed result (A+B+C) (comment out all other extra print 
 statements)
