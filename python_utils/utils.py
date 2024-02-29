```python
import os, json, hashlib
from datetime import datetime

def capitalize_first(s: str) -> str:
    """Capitalize the first letter of a string."""
    return s and s[0].upper() + s[1:]

def reverse_string(s: str) -> str:
    """Reverse the order of characters in a string."""
    return s[::-1]

def read_json(f: str) -> dict:
    """Read a JSON file and return its contents as a dictionary."""
    with open(f, 'r') as _f: return json.load(_f)

def write_json(f: str, c: dict):
    """Write a dictionary to a file in JSON format."""
    with open(f, 'w') as _f: json.dump(c, _f)

def checksum(f: str, a: str = 'sha256') -> str:
    """Calculate the checksum of a file using a specified algorithm (default is SHA-256)."""
    h = hashlib.new(a)
    with open(f, 'rb') as _f:
        for chunk in iter(lambda: _f.read(4096), b""): h.update(chunk)
    return h.hexdigest()

def date_str(f: str = "%Y-%m-%d") -> str:
    """Return the current date formatted as a string, default to "%Y-%m-%d"."""
    return datetime.now().strftime(f)

def days_diff(d1: datetime, d2: datetime) -> int:
    """Return the number of days between two datetime objects."""
    return (d2 - d1).days

def create_dir(p: str):
    """Create a directory at the specified path if it does not already exist."""
    if not os.path.exists(p): os.makedirs(p)

def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    return 1 if n == 0 else n * factorial(n-1)

def is_prime(num: int) -> bool:
    """Determine if a number is prime."""
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def merge_sort(lst):
    """Perform merge sort on a list."""
    if len(lst) <= 1: return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists."""
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
    """Calculate the nth Fibonacci number using memoization to enhance performance."""
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def find_longest_substring(s):
    """Find the length of the longest substring without repeating characters."""
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
    """Encode a string using Run-Length Encoding (RLE)."""
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
    """Decode a string encoded with Run-Length Encoding (RLE)."""
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
```