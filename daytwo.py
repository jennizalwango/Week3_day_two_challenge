vowels = 'aieou'
string = input('enter word')
lista = []

# def count_vowel():
#     for x in string:
#         count = string.count(x)
#         if count >=1 and x in vowels:
#             lista.insert(0,x)
#             lista.append(count)
#             print(tuple( lista))
#         else:
#             print('no vowel found')
#         break

# count_vowel()        

def get_vowels():
    count = len(string)
    if count > 0:
        for letter in string:
            if letter in vowels:
                lista.append(letter)
        return tuple(lista)
    else:
        return'no vowel found'
print(get_vowels())     