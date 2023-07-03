"""
#FebFull
from collections import Counter
a = [3,14,33,31,18,25,24,34,2,22,9,24,16,12,7,34,11,21,1,23,22,17,28,17,22,21,34,24,16,
     34,24,7,12,9,29,12,31,25,1,17,7,11,30,31,24,32,34,25,8,21,34,33,9,16,21,7,11,
     2,12,17,18,22,24,25,28,29,30,31,27,34,21,24,5,19,2,33,32,30,
     1,9,8,17,12,10,1,11,7,31,7,24,30,33,11,21,2,7,
     33,24,9,24,12,1,8,33,6,25,17,33,7,8,31,12,10,17,8,34,21,33,14,24,1,7,31,12,10,1,10,22,12]
print (Counter(a))
for key, c in Counter(a).most_common():
    print("{}: {}".format(key, c)) 
"""
"""
P = 21(3)
"""
#June 2-28
from collections import Counter


a = [1,23,21,8,24,5,14,10,26,9,
     30,17,20
     ]
     
b = [
     5,11,8,10,
     3,7,12,31,
     1,30,17,14,7,29,12,2,29,13,
     24,7,11,21,16,1,
     3,15,
     ]

cc = [34,
     3,30,
     3,24,34,9,8,31,12,23,7,
     10,11,12,
     8,16,24,1,
     ]

d = [1,7,8,23,
     34,
     8,3,7,
     31,1,8,24,34,
     24,
     30,24,8,14,21,
     
     24,34,5,12,32,
     1,8,21,23]

x = a+b+cc+d

print (Counter(a))
for key, c in Counter(a).most_common():
    print("{}: {}".format(key, c))
print("A===============")

print (Counter(b))
for key, c in Counter(b).most_common():
    print("{}: {}".format(key, c))
print("B===============")

print (Counter(cc))
for key, c in Counter(cc).most_common():
    print("{}: {}".format(key, c))
print("CC===============")

print (Counter(d))
for key, c in Counter(d).most_common():
    print("{}: {}".format(key, c))
print("D===============")

print (Counter(x))
for key, c in Counter(x).most_common():
    print("{}: {}".format(key, c))
print("Total===============")

