from collections import Counter

def verify_anagram(str_one: str, str_two: str)->bool:
    """this function verify if a word and another word are anagrams
        An anagram is when two word have a same letters

    Args:
        str_one (str): first string 
        str_two (str): second string

    Returns:
        bool: returns True if successful and False if no successful
    """
    return True if Counter(str_one)==Counter(str_two) else False

def run():
    check = verify_anagram('vaca','cava')
    if check:
        print('It\'s an anagram')
    else:
        print('It\'s not an anagram')

if __name__=='__main__':
    run()