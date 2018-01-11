def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    mychar = ('a','e','u','o','i','A','E','U','O','I')
    return char in mychar
    
z=isVowel2('L')
print z
