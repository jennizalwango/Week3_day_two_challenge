vowels = 'aieou'
string = input('enter word')
list = []
def get_vowel():
    for x in string:
        count = string.count(x)
        if count >=1 and x in vowels:
            list.append(x)
            tuple()
            print(f'( {list}, {count} )')
        else:
            print('no vowel found')
        break
get_vowel()        