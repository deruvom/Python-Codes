#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')

animals = {'c': [4], 'b': [15, 12, 6], 'e': [0, 5, 7], 'H': [5, 19], 'K': [1, 17, 10, 19, 16], 'J': [1], 'Q': [14, 3, 12, 5], 's': [7, 3], 'U': [], 't': [], 'T': [17, 12, 16]}

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    number = 0
    # Your Code Here
    for key in aDict.keys():
        number += len(aDict[key])
    return number
    
    # result = 0
    #for value in aDict.values():
    #    # Since all the values of aDict are lists, aDict.values() will 
    #    #  be a list of lists
    #    result += len(value)
    #return result
    
#print howMany(animals)


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
   
       # print aDict[key] # returns the values
  
    
   
print biggest(animals)