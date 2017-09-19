
import re

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    full = pieces[1]
    print(full)
    email = full.split('@')[1]
    print(email)
