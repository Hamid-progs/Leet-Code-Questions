# the below hashing function are examples which mainly count int ,characters usin hashing!

def hashing_1(a = [1,3,2,1,3]):
    hash = [0] * 13  # it will create list with 13 zeros index upto 12
    
    # hash computation
    for  i in range(0,len(a)):
        hash[a[i]] += 1

    # fetching count
    q = int(input("how many time you want to check numbers: "))
    while q:
        number = int(input('Enter the Number you want to find count: '))
        print(hash[number])
        q = q-1

# hashing_1()

# array a  element max number is more then 12 
def hashing_2(a = [1,3,2,1,3,53]):
    length = max(a)  + 1 
    hash = [0] * length  # it will create list with 13 zeros index upto 12

    # hash computation
    for  i in range(0,len(a)):
        hash[a[i]] += 1

    # fetching count
    q = int(input("how many time you want to check numbers: "))
    while q:
        number = int(input('Enter the Number you want to find count: '))
        print(hash[number])
        q = q-1

# hashing_2()

# ----------------------------------------------------------------------------------

# hashing lower case character using arrays
def hashing_3(s = 'abcdabcj'):
    hash = [0]*26
    
    # hash computation
    # this will add 1 in the a particula index if character come
    for i in s:
        hash[ord(i) - ord('a')] += 1   # ord returns character ascii value

    # fetching count
    q = int(input("how many time you want to check the character: "))
    while q:
        c = input('Enter the character you want to count: ')
        print(hash[ord(c) - ord('a')])
        q -= 1

# hashing_3()

# hashing using dictionaries 
# best for hashing and effective

def hashing_4(s = 'abcdabcj'):
    hash = dict()

    # hash computation
    for i in s:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1  # it will assigne 1 to upcoming new character

    # fetching
    q = int(input("how many time you want to check the character: "))
    while q:
        c = input('Enter the character you want to count: ')
        if c in hash:
            print(hash[c])
        else:
            print(0) # if the character no in the stiring hence its count will be zeor
        q -= 1

# hashing_4()
