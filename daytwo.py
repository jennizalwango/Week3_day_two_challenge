vowels = 'aieou'
string = input('enter word')
lista = []

def get_vowel():
    for x in string:
        count = string.count(x)
        if count >=1 and x in vowels:
            lista.insert(0,x)
            lista.append(count)
            print(tuple( lista))
        else:
            print('no vowel found')
        break

get_vowel()        