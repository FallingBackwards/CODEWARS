word = "yellow"
myArray = list(word)
secondArray = []
q = 0
while q < len(myArray):
    k = myArray[q]
    g = 0
    w = 0
    while w < len(myArray):
        if myArray[q].lower() == myArray[w].lower() and q == w:
            w = w + 1
        elif myArray[q].lower() == myArray[w].lower():
            g = g + 1
            w = w + 1
        else:
            w = w + 1
    if g > 0:
        secondArray.append(')')
    else:
        secondArray.append('(')
    q = q + 1
l = ''.join(secondArray)
print(l)
##supershort answer
##def duplicate_encode(word):
    ##return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])