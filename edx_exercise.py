

'''n = 12

while n > 10:
    print('Hello!')
    n -= 2
    while n >=2:
        print(n)
        n -= 2'''
        
	
'''end = 6
mysum = 0
while end > 1:
    mysum += end                                                         	
    end -= 1
    while end == 1:
        mysum += end
        print(mysum)
        end -= 1'''
        
        

'''for n in range(2,12,2):
    print(n)
print("Goodbye!")'''

'''for i in range(12,0,-2):
    if i == 12:
        print('Hello!')
        i -= 2
    else:
        print(i)'''
        
'''end = 6
mysum =0
for i in range(1,end):
    mysum += i
    i += 1
    if i == end:
        mysum += i
        print(mysum)
        i += 1'''
        
'''for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') '''

'''school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))'''

'''
s = 'azcbobobegghaklbobob'


bobs = 0
start = 0
end = 3
while end <= len(s) + 1 and start < len(s)-2 :
    if s.count('bob', start,end) == 1:
        bobs += 1
    start += 1
    end += 1

print("Number of times bob occurs is: " + str(bobs))'''

'''
s = 'azcbobobegghaklbobob'
r,p,t = '','',''
for c in s:
    if p <= c:
        t += c
        p = c
    else:
        if len(t) > len(r):
            r = t
        t,p = c,c
if len(t) > len(r):
    r = t
print( 'Longest substring in alphabetical order is: ' + r)'''

'''                            
s = 'azcbobobegghaklbobob'  #The original string
l = len(s)    #The length of the original string

maxlenstr = s[0]    #maximum length sub-string, taking the first letter of original string as value.

curlenstr = s[0]    #current length sub-string, taking the first letter of original string as value.

for i in range(1,l):    #in range, the l is not counted. 

    if s[i] >= s[i-1]:    #If current letter is greater or equal to previous letter,
        curlenstr += s[i] #add the current letter to current length sub-string
    else:        
        curlenstr = s[i]  #otherwise, take the current letter as current length sub-string

    if len(curlenstr) > len(maxlenstr): #if current cub-string's length is greater than max one,
            maxlenstr = curlenstr;      #take current one as max one.

print("Longest substring in alphabetical order is:", maxlenstr)'''

secret_num = int(input("Please think of a number between 0 and 100! "))

low = 0
high = 100
ans = (high + low)/2

while ans >= 0 and ans < 100 :
    print("is your secret number " + str(ans) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    elif x == 'c':
        print("Game over your secret number was: " + str(ans))
        break
    else :
        print("Sorry, I did not understand your input")
    
    ans = int((high + low)/2)
    















