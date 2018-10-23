# A program to convert phone numbers to a combination of English words (when possible) - 697-466-3686 could become MYPHONENUM; 724-6837 could become PAINTER
# Computation time may be the biggest challenge - if both numbers AND the corresponding letters are checked, a 10-digit phone number could result in over 1 million combinations, each to be checked against a dictionary of over 50,000 words...
# Some numbers will have multiple results, others will have none.  Since no letters correspond to the 0 or 1 keys, those numbers can't be converted to letters.

# letters = [["0"],["1"],["A","B","C","2"],["D","E","F","3"],["G","H","I","4"],["J","K","L","5"],["M","N","O","6"],["P","Q","R","S","7"],["T","U","V","8"],["W","X","Y","Z","9"]]

letters = [["0"],["1"],["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]

filename = "words.txt"
handle = open(filename,'r')
text = handle.read()
words = text.split()

letters1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters2 = []
letters3 = []
letters4 = []
letters5 = []
letters6 = []
letters7 = []
letters8 = []
letters9 = []
letters10 = []

# to speed checking, divide words by length (if first 5 numbers of 10-digit # match a word, no need comparing remaining 5 to words of length 6 or greater...)
for word in words:
    if len(word)==2:
        letters2.append(word.upper())
    elif len(word)==3:
        letters3.append(word.upper())
    elif len(word)==4:
        letters4.append(word.upper())
    elif len(word)==5:
        letters5.append(word.upper())
    elif len(word)==6:
        letters6.append(word.upper())
    elif len(word)==7:
        letters7.append(word.upper())
    elif len(word)==8:
        letters8.append(word.upper())
    elif len(word)==9:
        letters9.append(word.upper())
    elif len(word)==10:
        letters10.append(word.upper())
    

# can add more tests in future (7 or 10 digits), allow other formats, etc....
while True:
    phoneno = input("Please enter a phone number - numbers only ")
    try:
        int(phoneno)
        break
    except:
        continue

print("You entered", phoneno)


possibles = [""]
for digit in phoneno:
    newpossibilities = []
    for possible in possibles:
        for onelet in letters[int(digit)]:
            newpossibilities.append(possible+onelet)
    possibles = newpossibilities.copy()

print(possibles)
#for number in range(100000):
#    bigarray.append("asdfsdds")
    
#bigarray[50000]="the"

#for testword in bigarray:
#    if testword in words:
#        print(testword,"is a word")

#####   FUNCTIONS BELOW WERE BROUGHT IN FROM OTHER PROGRAM...
#function to create the dictionary and count word occurrences
#def lyrics_to_frequencies(lyrics):
#    myDict = {}
#    for word in lyrics:
#        word = word.lower()
#        word = word.rstrip(',.;:!?()"')
#        word = word.lstrip('"')
 #       if word in myDict:
 #           myDict[word] += 1
 #       else:
 #           myDict[word] = 1
 #   return myDict
    
#function counts the most common words (returns all words that tie for the greatest frequency, as well as the number of occurrences).  A dictionary should be passed to it - words & number of occurrences (the results of the lyrics_to_frequencies function).
#def most_common_words(freqs):
#    values = freqs.values()
#    best = max(values)
#    words = []
#    for k in freqs:
#        if freqs[k] == best:
#            words.append(k)
#    return (words, best)
    
#function returns all words that occur at least a specified minimum number of times.  Uses as input the dictionary created by lyrics_to_frequencies and the desired number of occurrences.  NOTE - it works by MUTATING THE ORIGINAL DICTIONARY, deleting words that meet the criteria.
#def words_often(freqs, minTimes):
#    result = []
#    done = False
#    while not done:
#        temp = most_common_words(freqs)
#        if temp[1] >= minTimes:
#            result.append(temp)
#            for w in temp[0]:
#                del(freqs[w])
#        else:
#            done = True
#    return result

#print("This program returns a list of the words in a file that occur at least as many times as the frequency that is requested by the user.")
#name = input('Please enter a file name (full path), or simply hit "enter" to use the default file:')
#mincount = input('Enter minimum number of word occurrences to return:')
#if name == "":
#    name = "c:\python27\myprograms\Text01.txt"
#handle = open(name,'r')
#text = handle.read()
#words = text.split()

#worddict = lyrics_to_frequencies(words)
#print(words_often(worddict, int(mincount)))    