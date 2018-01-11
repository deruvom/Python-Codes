
def isVowel(char):
    '''
        char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    ''' 
    return {
    'a': True,
    'e': True,
    'i': True,
    'o': True,
    'u': True,
  }.get(char.lower(), False)  

z=isVowel('H')
print z