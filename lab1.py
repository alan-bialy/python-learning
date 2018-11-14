#Printing
#Write a program using print() that, when run, prints out a tic-tac-toe board.

print('  |  |\n--------\n'*2,' |  |')

#
print('\n')
#Printing 2 (challenge)
#Write a program that, when run, prints out a SUPER tic-tac-toe board.

t1 = "  |  |  "
t2 = "--+--+--"
t3 = "="*8
h="H"

for i in range(3):
    print((t1+h)*2+t1,
          (t1+h)*2+t1,
          (t1+h)*2+t1,
          sep='\n'+ (t2+h)*2+t2 +'\n')
    if i != 2:
        print((t3+'+')*2+t3)

#
print('\n')
#Fizz, Buzz, FizzBuzz!
#Find the sum of all the multiples of 3 or 5 below 1001.

sum=0
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        sum+=i
print("Sum = "+str(sum))

#
print('\n')
#Collatz Sequence
#What is the length of the longest chain which has a starting number under 1000?

def collatz(n):
    max=0;
    for i in range(1,n):
        start=i;
        length = 1;
        while(i!=1):
            length+=1
            if(i%2==0):
                i/=2
            else:
                i=3*i+1
        #print("Sequence starting from "+str(start)+" contains "+str(length)+" terms")
        if(length > max):
            max=length
            st=start
    print("Longest chain sequence under "+str(n)+" contains "+str(max)+" terms and it starts from "+str(st))

collatz(1000)
#collatz(1000000) # takes minute to run but works

#
print('\n')
#Fahrenheit-to-Celsius converter

def convert():
    f = input('Temperature F? ')
    c = (float(f) - 32)*5/9
    print('It is {0} degrees Celsius.'.format(round(c,2)))

convert()
convert()
convert()