import os, json, hashlib
from datetime import datetime

def capitalize_first(s: str) -> str:
    return s and s[0].upper() + s[1:]

def reverse_string(s: str) -> str:
    return s[::-1]

def read_json(f: str) -> dict:
    with open(f, 'r') as _f: return json.load(_f)

def write_json(f: str, c: dict):
    with open(f, 'w') as _f: json.dump(c, _f)

def checksum(f: str, a: str = 'sha256') -> str:
    h = hashlib.new(a)
    with open(f, 'rb') as _f:
        for chunk in iter(lambda: _f.read(4096), b""): h.update(chunk)
    return h.hexdigest()

def date_str(f: str = "%Y-%m-%d") -> str:
    return datetime.now().strftime(f)

def days_diff(d1: datetime, d2: datetime) -> int:
    return (d2 - d1).days

def create_dir(p: str):
    if not os.path.exists(p): os.makedirs(p)

def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n-1)

def is_prime(num: int) -> bool:
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def merge_sort(lst):
    if len(lst) <= 1: return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
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
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def find_longest_substring(s):
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
