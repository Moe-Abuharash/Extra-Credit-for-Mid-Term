keywords = ["Father", "God", 'Christ', "Spirit", 'spirit', 'life', 'man']
dict = {}

with open('book of John text.txt', 'r') as x:
    text = x.read().split(' ')


for word in text:
    dict[word] = dict[word]+1 if word in dict else 1

print([{dict[i], i} for i in keywords])
