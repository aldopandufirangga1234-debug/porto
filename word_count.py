import string

def wordcount(text):
    for tanda in string.punctuation:
        text = text.replace(tanda,"") 
    words = text.lower().split(" ")
    counts = {}
    
    for word in words :
        if word in counts :
            counts[word]= counts[word]+1
        else:
            counts[word] = 1 
            pass

    return counts

print(wordcount("Saya suka Python. Python itu mudah, saya suka!"))

