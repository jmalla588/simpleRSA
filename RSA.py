#!/usr/bin/python3
import sys
import fractions

#vars
valid_choice = False
numerical = []
result = []
decrypted = []
entry = []


#get string and uppercase it
def get_string():
    original_string = input("Enter your string to be converted.\nNOTE: String will be converted to all caps, only A-Z are supported.\nString: ")
    return original_string.upper()


#make sure string contains only A-Z
def check_valid(mod_string):
    for char in mod_string:
        if char > 'Z' or char < 'A':
            return False
    return True


#functions for modular inverse (from stack overflow: http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


#function for euler totient (phi) function
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1                                
    return amount


#choice of encrypt/decrypt
def e_or_d():
    choice = input("Enter (E/e) for encipher or (D/d) for decipher: ")
    if 'e' in choice or 'E' in choice:
        encrypt()
    if 'd' in choice or 'D' in choice:
        decrypt()
    else:
        return False


#encryption
def encrypt():

    valid_string = False

    while not valid_string:
        mod_string = get_string()
        valid_string = check_valid(mod_string)

    #convert string
    for char in mod_string:
        letter_num = ord(char) - 65
        numerical.append(letter_num)

    #perform calculations
    for num in numerical:
        result.append(pow(num, int(e), int(m))) 

    print(result)
    sys.exit()


#decryption
def decrypt():
    print("Enter numbers one by one. When complete, type \"end\"")
    letter = input("Digit #1: ")
    i = 1
    while letter != "end":
        i+=1
        entry.append(int(letter))
        letter = input("Digit #%d: " % (i))

    #calculate modular inverse
    inv = modinv(int(e), phi(int(m)))
    print("Modular Inverse: %d" % (inv))

    #letters collected.
    for num in entry:
        converted = pow(num, inv, int(m))
        result.append(chr(converted+65))
        decrypted.append(converted)

    print(result)
    #uncomment next line to print decrypted numbers before converting to letters
    #print(decrypted)
    sys.exit()



#main
print("Simple RSA encipher/decipher. Only works with block size 2.\n")

#get input values
e = input("Enter your value for e: ")
m = input("Enter your value for m (modulus): ")

while not valid_choice:
    valid_choice = e_or_d()
    print("Not a valid choice...\n")




