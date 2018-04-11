#!/usr/bin/python
def is_reverse(string1, string2):
    if len(string1) != len(string2):
       return False
    

    i=0
    j = len(string2) - 1 
    while j > 0:
          if string1[i] != string2[j]:
              return False
         
          i = i + 1
          j = j - 1
         

    return True



print is_reverse('upendar','radnepu')
