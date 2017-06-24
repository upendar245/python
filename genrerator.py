#!/bin/python
def countdown():
    i=5
    while i > 0:
         yield i 
         i -= 1
for k in countdown():
    print k

def cntmod():
    return 4

temp = cntmod()
print temp
