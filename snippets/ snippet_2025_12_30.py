import re
import unicodedata

def slugify(text: str, separator: str = '-') -> str:
    """
    Converts a string into a URL-friendly slug.

    Normalizes unicode characters (e.g., converts 'Ä' to 'A'), converts
    the string to lowercase, replaces non-alphanumeric characters and
    spaces with the specified `separator`, and cleans up duplicate,
    leading, or trailing separators. Ideal for creating clean URLs,
    filenames, or unique identifiers.

    Args:
        text (str): The input string to slugify.
        separator (str, optional): The character to use as a word separator.
                                   Defaults to '-'.

    Returns:
        str: The slugified string.

    Example:
        >>> slugify("Hello, World! This is a test.")
        'hello-world-this-is-a-test'
        >>> slugify("My Article Title with special chars & numbers 123", separator='_')
        'my_article_title_with_special_chars_numbers_123'
        >>> slugify("  Another  Example  ", separator='-')
        'another-example'
        >>> slugify("ÄÖÜ Some German Characters")
        'aou-some-german-characters'
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    # Normalize unicode characters to their closest ASCII representation
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = text.lower()

    # Replace non-word characters (excluding whitespace and the separator) with the separator
    pattern = r'[^\w\s{}]'.format(re.escape(separator))
    text = re.sub(pattern, separator, text)

    # Replace whitespace with the separator
    text = re.sub(r'\s+', separator, text)

    # Remove leading/trailing separators and multiple consecutive separators
    text = re.sub(r'{}+'.format(re.escape(separator)), separator, text).strip(separator)

    return text