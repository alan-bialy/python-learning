#Using sys for command-line tools.
#add.py
import sys

def adding(*y):
    sum = 0.0
    for x in y:
        try:
            sum+=float(x)
        except Exception:
            continue
    return sum

if len(sys.argv) <= 1:
    print(" Usage: python3    add.py < nums >\n    Add    some    numbers    together")
else:
    print(adding(*sys.argv))