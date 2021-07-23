count =dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('counting...')
for word in words:
    count[word]=count.get(word,0)+1
print('Counts',count)
#dictinary excercise