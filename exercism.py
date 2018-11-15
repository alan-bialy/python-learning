#Just Say Hello World
print("Hello, World!")

#Reverse String
def Reverse(str):
    return str[::-1]

print(Reverse('Test'))

#Isogram

def Isogram(word):
    x = True
    for i in word:
        if(str(word.lower()).count(i)>1):
            x = False
            break
    if x:
        print(str(word)+' is an isogram')
    else:
        print(str(word)+' is not an isogram')

Isogram('word')
Isogram('banana')
Isogram('customizable')
Isogram('Adam')

#Leap year
def Leap(rok):
    return ((rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0))

print(Leap(2016))
print(Leap(2018))