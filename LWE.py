'''This code is adopted from Buchanan, William J (2022). Learning With Errors (LWE) and Ring LWE. Asecuritysite.com. 
https://asecuritysite.com/encryption/lwe_output
https://asecuritysite.com/encryption/lwe
Prime number check function:https://www.pythonpool.com/check-if-number-is-prime-in-python/
String to binary code source: https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/
This code is going to be used to demonstrate lattice based key generation but adding more randomness to the original code
'''
import numpy as np
import sys
import random
#check if the q is prime
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
#selected secret list from known working values
good_secrets = [5,7,15,17,19]
decrypt =""
#create the selected public key sample
def selectedPK(public_key):
	res = random.sample(public_key, len(public_key)//2)
	print("Initial Public key",public_key)
	print("Selected values from Public Key",res)
	sum = np.sum(res)
	return sum
#pick a random q between 1 and 1000
q=random.randint(10,1000)
#run the loop until a prime number is detected
while isprime(q) != True:
    q=random.randint(10,1000)
#create the empty public key lsit
public_key=[]
#populate the public key with random prime numbers
vals = [random.randint(10,q), random.randint(10,q), random.randint(10,q), random.randint(10,q), random.randint(10,q), random.randint(10,q), random.randint(10,q), random.randint(10,q), random.randint(10,q),random.randint(10,q) ]
#pick a random secret key from the compatible value list
s = random.choice(good_secrets)
print ("Secret=",s)
#set the e to a static value
e = 5
print("E=",e)
message = 1
#input the plaintext and convert to binary
encode = input("Enter your message to encypt: ")
res = ''.join(format(ord(i), '08b') for i in encode)
print ("Message to send ",res)

#fill up the initial public key array with the LWE formula
for x in range(0,len(vals)):
	public_key.append(vals[x]*s+e)

print("Random values:",vals)
print("-----------------------\n")
#create the PK sample
sum = selectedPK(public_key)	
#display for testing
print('Sum is:',sum)
#add 1 to the value for the encrypted message bit
for bin in res:
	if bin == "1":
		sum=sum+1
		rem = sum % s
		if (rem%2==1):
			decrypt += bin
		sum -= 1
	elif bin == "0":
		rem = sum % s
		if (rem%2==0):
			decrypt += bin


print("Message Received: ",decrypt)
binary_int = int(decrypt,2)
# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8
  # Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")
  # Converting the array into ASCII text
ascii_text = binary_array.decode()
# Getting the ASCII value
print("Decrypted message: ",ascii_text)
