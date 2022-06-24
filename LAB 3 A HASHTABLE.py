def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'Gusion')
insert(HashTable, 25, 'Fanny')
insert(HashTable, 20, 'Lancelot')
insert(HashTable, 9, 'Diggie')
insert(HashTable, 21, 'Angela')
insert(HashTable, 21, 'Jax')

display_hash(HashTable)
