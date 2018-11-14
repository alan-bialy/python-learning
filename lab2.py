#Investigating Data Structures
#Lists

s = [0] * 3
s[0] += 1
print(s)

s = [''] * 3
s[0] += 'a'
print(s)

s = [[]] * 3
print(id(s[0]),id(s[1]))
s[0] += [1] # calling __iadd__ special method
print(s[0] is s[1])
s[0] = s[0] + [1] # __add__ special method using + operator
print(s[0] is s[1])
print(s)
print(id(s[0]),id(s[1]))

#
print('\n')
#Tuples
#Write a function to compute the GCD of two numbers.

def gcd(a, b):
    if b == a or b == 0:
        return a
    else:
        if a > b:
            return gcd(a-b,b)
        else:
            return gcd(a,b-a)
def gcd2(a,b):
    while b:
        a,b = b,a%b
    return a

print(gcd(10, 25))  # => 5
print(gcd(14, 15))  # => 1
print(gcd2(3, 9)) # => 3
print(gcd2(1, 1)) # => 1

#
print('\n')
#Dictionaries
#Write a function that properly reverses the keys and values of a dictionary
# - each key (originally a value) should map to a set of values (originally keys) that mapped to it


def flip_dict(d):
    inv = {}
    for k, v in d.items():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv
    #return {value: key for key, value in dictionary.items()}

print(flip_dict({"CA": "US", "NY": "US", "ON": "CA"}))

#
print('\n')
#Comprehensions

print([x for x in [1, 2, 3, 4]])
print([n - 2 for n in range(10)])
print([k % 10 for k in range(41) if k % 3 == 0])
print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

# Something is fishy here. Can you spot it?
arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
print(arr)
[el.append(el[0] * 4) for el in arr]  # What does this return?
print(arr)

print([letter for letter in "pYthON" if letter.isupper()])
print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})

#Write
#Write a comprehension to transform the input data structure into the output data structure

#[0, 1, 2, 3] -> [1, 3, 5, 7]
print([x+i+1 for x,i in enumerate([0, 1, 2, 3])])

#[3, 5, 9, 8] -> [True, False, True, False]
print([k%3 == 0 for k in [3, 5, 9, 8]])

#["TA_sam", "TA_guido", "student_poohbear", "student_htiek"] -> ["sam", "guido"]
print([x[3:] for x in ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"] if x.startswith("TA_")])

#['apple', 'orange', 'pear'] -> ['A', 'O', 'P']
print([x[0].upper() for x in ['apple', 'orange', 'pear']])

#['apple', 'orange', 'pear'] -> ['apple', 'pear']
print([x for x in ['apple', 'orange', 'pear'] if len(x) < 6])

#['apple', 'orange', 'pear'] -> [('apple', 5), ('orange', 6), ('pear', 4)]
print([(x,len(x)) for x in ['apple', 'orange', 'pear']])

#['apple', 'orange', 'pear'] -> {'apple': 5, 'orange': 6, 'pear': 4}
d = {}
[d.update({x:len(x)}) for x in ['apple', 'orange', 'pear']]
print(d)

#
print('\n')
#Cyclone Phrases (challenge)

import math


def is_cyclone_phrase(phrase):
    for p in phrase.split():
        m=int(math.ceil(len(p)/2))
        if len(p) == 0 or len(p) == 1:
            break
        else:
            if len(p) == 2:
                if p[0] > p[1]:
                    return False
            else:
                for n,i in enumerate(p):
                    if n + 1 == m:
                        break
                    if p[n] > p[-1-n]:
                        return False
                    if p[-1-n] >p[n+1]:
                        return False
    return True

print(is_cyclone_phrase("adjourned")) # => True
print(is_cyclone_phrase("settled")) # => False
print(is_cyclone_phrase("all alone at noon")) # => True
print(is_cyclone_phrase("by myself at twelve pm")) # => False
print(is_cyclone_phrase("acb")) # => True
print(is_cyclone_phrase("")) # => True

print(is_cyclone_phrase("abcca")) # => True
print(is_cyclone_phrase("accdb")) # => False

