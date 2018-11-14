#Lab 4: Functional Programming
#Functional Tools
#Lambdas

print((lambda val: val ** 2)(5))  # => 25
print((lambda x, y: x * y)(3, 8))  # => 24
print((lambda s: s.strip().lower()[:2])('  PyTHon'))  # => 'py'

#Map
# ['12', '-2', '0']     =>	    [12, -2, 0]
print(list(map(int,['12', '-2', '0'] )))

#['hello', 'world']     =>	    [5, 5]
print(list(map(len,['hello', 'world'] )))

#['hello', 'world']     =>      ['olleh', 'dlrow']
print(list(map(lambda x: x[::-1],['hello', 'world'] )))

#range(2, 6)            =>  	[(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
print(list(map(lambda x: (x, x**2, x**3),range(2, 6) )))

#zip(range(2, 5), range(3, 9, 2)) =>	[6, 15, 28]
print(list(map(lambda args: args[0]*args[1],zip(range(2, 5), range(3, 9, 2)))))

print(list(map(int, ('10110', '0xCAFE', '42'), (2, 16, 10)))) # generates 22, 51966, 42

#
print()
#Filter

#['12', '-2', '0'] 	    =>   ['12', '0']
print(list(filter(lambda x: int(x)>=0,['12', '0'])))

#['hello', 'world'] 	=>   ['world']
print(list(filter(lambda x: x.startswith('w'),['hello', 'world'])))

#['Stanford', 'Cal', 'UCLA'] =>	['Stanford']
print(list(filter(lambda x: x.startswith('S'),['Stanford', 'Cal', 'UCLA'])))

#range(20)      =>  	[0, 3, 5, 6, 9, 10, 12, 15, 18]
print(list(filter(lambda x: x%3 == 0 or x%5 == 0,range(20))))

#Other Useful Tools (optional)