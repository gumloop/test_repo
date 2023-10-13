import os, json, hashlib
from datetime import datetime


def capitalize_first(s: str) -> str:
    """
    Function to capitalize the first character of a given string.

    Args:
        s: The string to be capitalized.

    Returns:
        The input string with its first character capitalized.
    """
    return s and s[0].upper() + s[1:]


def reverse_string(s: str) -> str:
    """
    Function to reverse a string.

    Args:
        s: The string to be reversed.

    Returns:
        The reversed string.
    """
    return s[::-1]


def read_json(f: str) -> dict:
    """
    Function to read a JSON file and return its contents as a dictionary.

    Args:
        f: The name or path of the JSON file.

    Returns:
        The contents of the JSON file as a dictionary.
    """
    with open(f, 'r') as _f: 
        return json.load(_f)


def write_json(f: str, c: dict):
    """
    Function to write a dictionary to a JSON file.

    Args:
        f: The name or path of the JSON file.
        c: The dictionary to be written to the file.
    """
    with open(f, 'w') as _f: 
        json.dump(c, _f)


def checksum(f: str, a: str = 'sha256') -> str:
    """
    Function to calculate the checksum of a file.

    Args:
        f: The file whose checksum is to be calculated.
        a: The algorithm to be used to calculate the checksum. Defaults to 'sha256'.

    Returns:
        The checksum of the file.
    """
    h = hashlib.new(a)
    with open(f, 'rb') as _f:
        for chunk in iter(lambda: _f.read(4096), b""): 
            h.update(chunk)
    return h.hexdigest()


def date_str(f: str = "%Y-%m-%d") -> str:
    """
    Function to get the current date and time as a string.

    Args:
        f: The format in which the date and time are to be returned. Defaults to '%Y-%m-%d' (Year-Month-Day)

    Returns:
        The current date and time as a string.
    """
    return datetime.now().strftime(f)


def days_diff(d1: datetime, d2: datetime) -> int:
    """
    Function to calculate the number of days between two dates.

    Args:
        d1: The first date.
        d2: The second date.

    Returns:
        The number of days between d1 and d2.
    """
    return (d2 - d1).days


def create_dir(p: str):
    """
    Function to create a directory if it does not already exist.

    Args:
        p: The path of the directory to be created.
    """
    if not os.path.exists(p): 
        os.makedirs(p)


def factorial(n: int) -> int:
    """
    Function to calculate the factorial of a given number.

    Args:
        n: The number whose factorial is to be calculated.

    Returns:
        The factorial of n.
    """
    return 1 if n == 0 else n * factorial(n-1)


def is_prime(num: int) -> bool:
    """
    Function to check if a number is prime.

    Args:
        num: The number to be checked.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: 
            return False
    return True


def merge_sort(lst):
    """
    Function to sort a list using the merge sort algorithm.

    Args:
        lst: The list to be sorted.

    Returns:
        The sorted list.
    """
    if len(lst) <= 1: 
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)    


def merge(left, right):
    """
    Helper function for merge sort which merges two sorted lists.

    Args:
        left: The first sorted list.
        right: The second sorted list.

    Returns:
        A merged list that is also sorted.
    """
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def fibonacci_memo(n, memo={}):
    """
    Function to generate the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to be generated.
        memo: A dictionary used for memoization. (default is empty dict)

    Returns:
        The nth Fibonacci number.
    """
    if n in memo: 
        return memo[n]
    if n <= 2: 
        return 1
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]


def find_longest_substring(s):
    """
    Function to find the longest substring of a string with no repeating characters.

    Args:
        s: The string in which to find the substring.

    Returns:
        The longest substring of s with no repeating characters.
    """
    used = {}
    start, maxlen, substr_start = 0, 0, 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            if i - start + 1 > maxlen:
                maxlen = i - start + 1
                substr_start = start
        used[c] = i
    return s[substr_start:substr_start + maxlen]


def rle_encode(s):
    """
    Function to encode a string using Run-Length Encoding.

    Args:
        s: The string to be encoded.

    Returns:
        The Run-Length Encoded string.
    """
    count, last, result = 1, s[0], ''
    for char in s[1:]:
        if char == last:
            count += 1
        else:
           result += last + str(count)
           count = 1
        last = char
    result += last + str(count)
    return result


def rle_decode(s):
    """
    Function to decode a Run-Length Encoded string.

    Args:
        s: The Run-Length Encoded string to be decoded.

    Returns:
        The decoded string.
    """
    result, i = '', 0
    while i < len(s):
        char = s[i]
        count = ''
        i += 1
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        result += char * int(count)
    return result
   

if __name__ == "__main__":
    print(capitalize_first("hello"))