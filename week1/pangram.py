import string
def pangrams(s:str):
    for letter in list(string.ascii_lowercase):
        if letter not in s.lower():
            return 'not pangram'
        
    return 'pangram'
    