

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    print(lin)

    wds = lin.split()

    for w in wds:
        # retrieve/create/update counter
        di[w] = di.get(w,0) + 1

    # most common word
largest = -1
word = None
for k,v in di.items() :
    if v > largest :
        largest = v
        # capture/remember the word that was the largest
        word = k

print('+------------------------------+')
print('   ','**Results**', word, largest)
print('+------------------------------+')