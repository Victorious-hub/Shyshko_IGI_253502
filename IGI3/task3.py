"""Task 27. Variant 27. Count non-whitespace characters int the string
"""

def count_non_whitespace(string: str) -> int:
    """Count non-whitespace characters in the string

    Args:
        string (str): any string

    Returns:
        int: characters
    """
    return len(''.join(string.split()))
