#Matt Wilson section 604



def longestWord(filename):
    """Opens filename and returns the length of the longest word."""
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    punctuation = ",.!?;:"
    blanks = "      "
    trantable = str.maketrans(punctuation,blanks)
    content = content.translate(trantable)
    wordlist = content.split()
             
    wordlen = 0
    for word in wordlist:
        if len(word) > wordlen:
            wordlen = len(word)
            
    return(wordlen)
    


def uniqueWordCount(filename):
    """Opens filename and returns a dictionary in {unique word: count} format."""
    
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    punctuation = ",.!?;:"
    blanks = "      "
    trantable = str.maketrans(punctuation,blanks)
    content = content.translate(trantable)
    content = content.lower()
    
    wordlist = content.split()
    worddict = {}
    
    for word in wordlist:
        if word not in worddict:
            worddict[word] = 0
        
        if word in worddict:
            worddict[word] += 1
    
    return worddict


print(longestWord('sampleFile1.txt'))
print(longestWord('sampleFile2.txt'))
print(longestWord('sampleFile3.txt'))

print(uniqueWordCount('sampleFile1.txt'))
print(uniqueWordCount('sampleFile2.txt'))
print(uniqueWordCount('sampleFile3.txt'))
