"""Task 4. Variant 27.
"""

STRING = "So she was considering in her own mind, as well as she could, \
for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain \
would be worth the trouble of getting up and picking the zdaisies, when suddenly a White Rabbit with pink eyes ran close by her."

def upper_amount(string: str) -> int:
    """Count uppercase characters in the string

    Args:
        string (str): any string

    Returns:
        int: characters
    """
    return sum(1 for char in string if char.isupper())


def find_letter_z(string: str) -> str:
    """Find the first letter 'z' in the string

    Args:
        string (str): any string

    Returns:
        str: index of the first 'z' letter
    """
    for index, word in enumerate(start=1, iterable=string.split()):
        if 'z' in word:
            return f"{index} {word}"

def excluse_a_words(string: str) -> str:
    """Exclude words begi with letter 'a'

    Args:
        string (str): any string

    Returns:
        str: str
    """

    return ' '.join(word for word in string.split()
                if not word.startswith('a'))
