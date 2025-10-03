sentence = 'Strings present letters a a consist Write than in with than in will when takes letter same in will with will words word all spaces'
myArray = sentence.split()
s = 0
t = 0
while t < len(myArray):
    word = myArray[t]
    l = list(word)
    if len(l) >= 5:
        l.reverse()
        myArray[t] = ''.join(l)
        s = s + 1
    else:
        s = s + 1
    t += 1
phrase = ' '.join(myArray)
print(phrase)