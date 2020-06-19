#given a:b b:c then a:b:c

def solveProportion(a, b1, b2, c): 

  

    A = a * b2 
    B = b1 * b2 
    C = b1 * c 
    gcd1 = math.gcd(math.gcd(A, B), C) 
    print( str(A // gcd1) + ":" + str(B // gcd1) + ":" + str(C // gcd1))
a = 3
b1 = 4
b2 = 8
c = 9
solveProportion(a, b1, b2, c) 


Output:
6:8:9
