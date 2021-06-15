def gcd(a,b):
    if(a==0):
        return b
    else:
        return gcd(b%a,a)

def CaesarEncoder(txt,key):
    
    alphabet = 'aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPrRsSşŞtTuUüÜvVyYzZ'
    txt1 = ""
    a = " "
    for i in txt:
        if(i == a):
            txt1 = txt1 + a
        else:
            loc = -1
            for j in alphabet:
                loc +=1
                if(i == j and loc%2 == 1):

                    txt1 = txt1 + alphabet[(loc+2*int(key))%58]
                elif(i == j and loc%2 == 0):
                    txt1 = txt1 + alphabet[(loc+2*int(key))%58]
    
    return txt1

def CaesarDecoder(txt,key):
    
    alphabet = 'aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPrRsSşŞtTuUüÜvVyYzZ'
    txt1 = ""
    a = " "
    for i in txt:
        if(i == a):
            txt1 = txt1 + a
        else:
            loc = -1
            for j in alphabet:
                loc +=1
                if(i == j and loc%2 == 1):

                    txt1 = txt1 + alphabet[(loc-2*int(key))%58]
                elif(i == j and loc%2 == 0):
                    txt1 = txt1 + alphabet[(loc-2*int(key))%58]
    
    return txt1

def EncodeCaesar(text,key):
    a=ord('a')
    alph=[chr(i) for i in range(a,a+26)]
    text = text.lower().split()
    enc_word=""
    for elements in text:
        for letters in elements :
            letter_index = alph.index(letters)
            letter_index += (int(key))%26
            enc_word =enc_word + alph[letter_index%26]
        enc_word = enc_word + " "
    return (enc_word.rstrip(" "))


def DecodeCaesar(text,key):
    a=ord('a')
    alph=[chr(i) for i in range(a,a+26)]
    text = text.lower().split()
    enc_word=""
    for elements in text:
        for letters in elements :
            letter_index = alph.index(letters)
            letter_index += 26-(int(key))%26
            enc_word =enc_word + alph[letter_index]
        enc_word = enc_word + " "
    return (enc_word.rstrip(" "))

def sumList(N):
    s = 0
    for i in N:
        s+=int(i)
    return s

def mean(N):
    return sumList(N)/len(N)

def median(N):
    if(len(N)%2==1):
        return int(len(N)/2)
    else:
        L = []
        L.append(N[int(len(N)/2)])
        L.append(N[int(len(N)/2)-1])
        return mean(L)

def mod(N):
    freq = N.count(N[0])
    elt = N[0]
    for i in N:
        if(N.count(i)>freq):
            freq = N.count(i)
            elt = i
    return elt

def fib(n):# return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def primes(a,b):
    l = [i for i in range(a,b+1)]
    prime = []
    for i in l:
        t = [k for k in range(2,i)]
        if(i>1):
            for j in t:
                if(i%j == 0):
                    break
            else:
                prime.append(i)
    return prime

def isPerfect(l):#check if the number is a perfect number
    sum = 0
    div = list()
    for i in range(1,l):
        if(l%i == 0):
            div.append(i)
            
    for i in div:
        sum += i
    if(sum == l):
        return True
    else:
        return False
