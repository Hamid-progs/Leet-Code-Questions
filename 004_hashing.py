def hashing_1(a = [1,3,2,1,3]):
    hash = [0] * 13  # it will create list with 13 zeros index upto 12
    for  i in range(0,len(a)):
        hash[a[i]] += 1

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
    for  i in range(0,len(a)):
        hash[a[i]] += 1

    q = int(input("how many time you want to check numbers: "))
    while q:
        number = int(input('Enter the Number you want to find count: '))
        print(hash[number])
        q = q-1

# hashing_2()

# ----------------------------------------------------------------------------------

