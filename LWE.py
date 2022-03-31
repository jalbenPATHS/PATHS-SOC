'''This code is adopted from Buchanan, William J (2022). Learning With Errors (LWE) and Ring LWE. Asecuritysite.com. 
https://asecuritysite.com/encryption/lwe_output
Prime number check function:https://www.pythonpool.com/check-if-number-is-prime-in-python/
This code is going to be used to demonstrate lattice based key generation but adding more randomness to the oringal code
'''
import numpy as np
import sys
import random
#pick a random q between 1 and 1000
q=random.randint(1,1000)
#check if the q is prime
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
#run the loop until a prime number is detected
while isprime(q) != True:
    q=random.randint(1,1000)

print(str(q) + " is the prime number to work with")

#Fill the 7x4 matrix with random numbers less than the prime number determined above
A=np.array([[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)],[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)],[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)],[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)],[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)],[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)],[random.randint(0,q) ,random.randint(0,q), random.randint(0,q), random.randint(0,q)]])
#sA = np.array([[6],[9],[11],[11]])
#build a random security matrix
sA = np.array([[random.randint(0,q) ],[random.randint(0,q)], [random.randint(0,q)], [random.randint(0,q)]])
#generate random noise to add
eA = np.array([[random.randint(-1,1)],[random.randint(-1,1)],[random.randint(-1,1)],[random.randint(-1,1)],[random.randint(-1,1)],[random.randint(-1,1)],[random.randint(-1,1)]])
#eA = np.array([[0],[-1],[1],[1],[1],[0],[-1]])

bA = np.matmul(A,sA)%q
#print (bA)

bA = np.add(bA,eA)%q
print
print ("Print output bA Value\n",bA)