import sys
import random



magic = []

raw_input ("Ask anything.")

magic.append( "It is certain.")

magic.append ("It is decidedly so.")

magic.append ("Outlook good.")

magic.append ("Better not tell you now.")

magic.append ("Concentrate and ask again.")

magic.append ("Very doubtful.")

magic.append ("Outlook not so good.")

magic.append ("Don't count on it.")
x = random.randint(0,len(magic)-1)
print magic[x]

