#Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines
#  as the person who sent the mail.
#  The program creates a Python dictionary that maps the sender's mail address
#  to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary
#  using a maximum loop to find the most prolific committer.
fname=input('Enter the file name:')
try:
    handle=open(fname)
except:
    print('Invalid file!')
    quit()
counts= dict()
bigcount=None
bigword=None
count=0
for line in handle:
    line=line.strip()
    if not line.startswith('From '): continue
    diff=line.split()
    for word in diff :
        value=diff[1]
    counts[value]=counts.get(value,0)+1
for value,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=value
        bigcount=count

print(bigword,bigcount)