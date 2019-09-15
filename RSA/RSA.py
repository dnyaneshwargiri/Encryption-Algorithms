def gcd(a, b): # calculates GCD of a and d
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(e, phi): # calculates modulo inverse of a for mod m
    for x in range(1, phi):
        if ((phi * x)+1) % e == 0:
            print(x)
            return int(((phi* x)+1) /e)
    return None


def coprimes(a): # calculates all possible co-prime numbers with a
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 :
            l.append(x)
    '''for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    '''
    return l

def encrypt_block(m): # encrypts a single block
    c = m ** e % n
    return c


def decrypt_block(c): # decrypts a single block
    m = c ** d % n
    return m


def encrypt_string(m): # applies encryption
    return ''.join([chr(encrypt_block(ord(x))) for x in list(m)])
    #return chr(encrypt_block(s)) 


def decrypt_string(m): # applies decryption
    return ''.join([chr(decrypt_block(ord(x))) for x in list(m)])
    

if __name__ == "__main__":
    p = int(input('Enter prime p: '))
    q = int(input('Enter prime q: '))

    print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")

    n = p * q
    print("n = p * q = " + str(n) + "\n")

    phi = (p - 1) * (q - 1)
    print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")

    print("Choose an e from a below coprimes array:\n")
    print(str(coprimes(phi)) + "\n")
    e = int(input())

    d = modinv(e, phi) # calculates the decryption key d

    print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
    print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")

    m = input("Enter a message to encrypt: ")
    print("\nPlain message: " + m + "\n")
    enc = encrypt_string(m)
    print("Encrypted message: ", enc, "\n")
    dec = decrypt_string(enc)
    print("Decrypted message: " + dec + "\n")
