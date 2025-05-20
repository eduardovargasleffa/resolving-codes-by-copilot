# let's test if a word is a palindrome?! A tip is: Use string manipulation concepts to invert the word and compare it with the original 

def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    A palindrome is a word that reads the same backward as forward.
    
    Args:
        word (str): The word to check.
        
    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    
    # Reverse the word and compare it with the original
    return word == word[::-1]

inform_word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(inform_word):
    print(f"{inform_word} is a palindrome.")
else:
    print(f"{inform_word} is not a palindrome.")
    