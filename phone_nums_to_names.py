# A program to convert phone numbers to a combination of English words (when possible) - 697-466-3686 could become MYPHONENUM; 724-6837 could become PAINTER
# Computation time may be the biggest challenge - if both numbers AND the corresponding letters are checked, a 10-digit phone number could result in over 1 million combinations, each to be checked against a dictionary of over 50,000 words...
# Some numbers will have multiple results, others will have none.  Since no letters correspond to the 0 or 1 keys, those numbers can't be converted to letters.

# letters = [["0"],["1"],["A","B","C","2"],["D","E","F","3"],["G","H","I","4"],["J","K","L","5"],["M","N","O","6"],["P","Q","R","S","7"],["T","U","V","8"],["W","X","Y","Z","9"]]

from datetime import datetime
import re
letters = [["0"],["1"],["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]

def sortedFind(word, sortedList):
    startpoint = 0
    endpoint = len(sortedList)
    while startpoint < endpoint:
        midpoint = (endpoint-startpoint)//2+startpoint
        if sortedList[midpoint] == word:
            return True
        if word > sortedList[midpoint]:
            startpoint = midpoint+1
        else:
            endpoint = midpoint
    return False



def createNumber(word):
    returnNumber = ""
    word = word.upper()
    for letter in word:
        for onelist in range(len(letters)):
            if letter in letters[onelist]:
                returnNumber += str(onelist)
                break
    return returnNumber
    

thingie = input("Enter a word to test: ")
print(createNumber(thingie))

wordSplitStart = datetime.now()
filename = "words.txt"
#with open(filename, 'r') as previousscrape: 
#    reader = csv.reader(previousscrape)
#    previousinfo = list(reader)
handle = open(filename,'r')
text = handle.read()
handle.close()
wordlist = text.split()
sorttimer = datetime.now()
wordlist.sort()
# print(wordlist)
sorttimerend = datetime.now()
print("sort took",(sorttimerend-sorttimer).total_seconds(),"seconds")



# seed list of words with empty array for 0, letters of alphabet for 1, and empty arrays for 2 through 10
words = [[],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],[],[],[],[],[],[],[],[],[]]


# to speed checking, divide words by length (if first 5 numbers of 10-digit # match a word, no need comparing remaining 5 to words of length 6 or greater...)

for word in wordlist:
#    if word.upper() == "SOFTEN":
#        print("found soften, its length: ", len(word))
    if len(word) > 1 and len(word) < 11:
        words[len(word)].append(word.upper())

# no longer need test - test had been created to determine if word list was fully sorted (it wasn't)
#for wordlength in range(2,11):
#    print("sort testing words of length", wordlength)
#    counter = 0
#    for aword in range(len(words[wordlength])-1):
#        if words[wordlength][aword]>words[wordlength][aword+1]:
#            counter += 1
#    print("found", counter, "words out of", len(words[wordlength]), "words of length", wordlength, "that were out of order.")


wordSplitEnd = datetime.now()      
print("Splitting the word list into categories took", (wordSplitEnd-wordSplitStart).total_seconds(), "seconds.")

# can add more tests in future (7 or 10 digits), allow other formats, etc....
while True:
    phoneno = input("Please enter a phone number - numbers only ")
    try:
        int(phoneno)
        break
    except:
        continue

print("You entered", phoneno)
combinations =  3**len(re.findall('[234568]', phoneno))*4**len(re.findall('[79]', phoneno))
print("Checking",combinations,"possible combinations.")

possiblesStart = datetime.now()
possibles = [""]
for digit in phoneno:
    newpossibilities = []
    for possible in possibles:
        for onelet in letters[int(digit)]:
            newpossibilities.append(possible+onelet)
    possibles = newpossibilities.copy()
possiblesEnd = datetime.now()
# print(possibles)  
print("Finding possible words took", (possiblesEnd-possiblesStart).total_seconds(), "seconds.  Now assembling all possible combinations of words and numbers.")




matchStart = datetime.now()
matches = set()


# step through each possible combination, starting with longest word
for shortener in range(len(phoneno)-1):
    for possible in possibles:
        for pointer in range(shortener+1):
            wordLen = len(possible)-shortener
            if sortedFind(possible[pointer:wordLen+pointer], words[wordLen]):
                matches.add((pointer,wordLen+pointer-1,possible[pointer:wordLen+pointer]))

matchEnd = datetime.now()      
print("Checking for words of all lengths (1 pass) took", (matchEnd-matchStart).total_seconds(), "seconds.")



def checkAgain(start):
    moreStuff = set()
    for match in matches:
        if match[0] >= start:
            moreStuff.add(match)
    return moreStuff


def addToWord(item):
    if item[1] <= len(phoneno) - 2:
        for match in matches:
            if match[0] > item[1] and match[1] < len(phoneno):
                fullList.add((phoneno[:item[0]]+'-'+item[2] + '-' + phoneno[item[1]+1:match[0]] + '-' + match[2]+'-'+phoneno[match[1]+1:]).strip('-').replace('--','-'))
                recursiveCheck = (item[0],match[1],(item[2] + '-' + phoneno[item[1]+1:match[0]] + '-' + match[2]).strip('-').replace('--','-'))
                addToWord(recursiveCheck)
                
            
        

#fullList = set(matches)
#addToWord(0)

# seed the final list with initial list of matches
fullList = set()
for match in matches:
    fullList.add((phoneno[:match[0]]+'-'+match[2]+'-'+phoneno[match[1]+1:]).strip('-'))
    addToWord(match)



#if len(matches) == 0:
#    print("We found no matches")
#    quit()
    
#matchCopy = set(match)
#****mark****
# set = function call, returning multiple additions
# within function call, if there's room left at the end, it calls itself
# does function call have to return anything?  Could just append to set?
# let's say function gets called with two numbers, & they yield nothing - it won't call itself again
# ... it also won't call itself again if it finds a two letter word, as there will be nothing left
# so... function gets called with start index...
# function pulls all possible items that can fill spots...
# after each one is received, if there is room after the end, the function calls itself again...
# function functionname(index)
# for match in matches, if match fits within index, append it to set?  (but needs to be tied to part before... so something must be returned OR function must be called with preceding item(s))
# so if returning something, would have to return a set.  Each set would then be appended to match which called it.
# word1 calls function
# function finds word2, word3, word4
# word2 finds word5, word6; word3 finds word5, word6
# ...word2word5word6, word3word5word6, word4
# word1word2word5word6, etc.
#for match in matches:
    #fullList.add((phoneno[:match[0]]+'-'+match[2]+'-'+phoneno[match[1]+1:]).strip('-'))  ####??????? need / want this?
    # fulllist.add(functionName(match, including start & end indices, BUT future calls would have to have modified matches, including interspersing #s and dashes... )
    # morestuff = function(start index) - but could return multiple items... could I call it with [morestuff]? ... cuz need to have recursive function add in each additional thing... oy!

#for match in matches:
#    fullList.add((phoneno[:match[0]]+'-'+match[2]+'-'+phoneno[match[1]+1:]).strip('-'))
#    if match[1] < len(phoneno)-2:
#        posts = checkAgain(match[1])
#        for pre in pres:
#            fullList.add((phoneno[:pre[0]]+'-'+pre[2] + '-' + phoneno[pre[1]+1:match[0]] + '-' + match[2]+'-'+phoneno[match[1]+1:]).strip('-').replace('--','-'))
#        posts = checkAgain(match[1],)


#fullList = set()
#def checkAgain(start,end):
#    moreStuff = set()
#    for match in matches:
#        if match[0] >= start and match[1] < end:
#            moreStuff.add(match)
#    return moreStuff

#if len(matches) == 0:
#    print("We found no matches")
#else:
#    print("Your matches:")
#    for match in matches:
#        fullList.add((phoneno[:match[0]]+'-'+match[2]+'-'+phoneno[match[1]+1:]).strip('-'))
#        if match[0] > 1:
#            pres = checkAgain(0,match[0])
#            for pre in pres:
#                fullList.add((phoneno[:pre[0]]+'-'+pre[2] + '-' + phoneno[pre[1]+1:match[0]] + '-' + match[2]+'-'+phoneno[match[1]+1:]).strip('-').replace('--','-'))
#            posts = checkAgain(match[1],)

if len(fullList) == 0:
    print("We found no matches")
    quit()
 

           
firstSort = []
for item in fullList:
    # Do I want to replace all 2s with As and 4s with Is or create additional combinations with those substitutions??
    item = item.replace("2","-A-").replace("4","-I-").replace("--","-").strip("-")
    firstSort.append(item)
firstSort.sort()

### SORT THE LIST BASED UPON THE NUMBER OF DASHES FOUND (want, say, "FREEHOLD" to appear before "FREE-HOLD")
### SORTING IN REVERSE OF DESIRED ORDER SINCE NEXT SORT REVERSES THIS SORT
semifinalList = [firstSort.pop(0)]                
for oneThing in firstSort:
    dashLength = oneThing.count('-')
    found = False
    for anIndex in range(len(semifinalList)):
        if dashLength > semifinalList[anIndex].count('-'):
            found = True
            semifinalList = semifinalList[:anIndex] + [oneThing] + semifinalList[anIndex:]
            break
    if not found:
        semifinalList.append(oneThing)




### SORT THE LIST BASED UPON THE NUMBER OF LETTERS FOUND
finalList = [semifinalList.pop()]                
for oneThing in semifinalList:
    letterLength = len(re.findall("[A-Z]", oneThing))
    found = False
    for anIndex in range(len(finalList)):
        if letterLength > len(re.findall("[A-Z]", finalList[anIndex])):
            found = True
            finalList = finalList[:anIndex] + [oneThing] + finalList[anIndex:]
            break
    if not found:
        finalList.append(oneThing)

maxResults = 100
for oneThing in finalList[:maxResults]:
    print(oneThing)
# sample result in matches:
# (5, 8, 'FAD')
# a tuple with the word that was found, its starting index in the phone number, and its ending index
# need to add in all possibilities for missing digits...
# finalList = set()

#for match in matches:
    
