```python
import os, json, hashlib
from datetime import datetime

def capitalize_first(s: str) -> str:
    """
    将字符串的第一个字母大写
    参数:
        s (str): 要处理的字符串
    返回值:
        str: 大写第一个字母的字符串
    """
    return s and s[0].upper() + s[1:]

def reverse_string(s: str) -> str:
    """
    反转字符串
    参数:
        s (str): 要反转的字符串
    返回值:
        str: 反转后的字符串
    """
    return s[::-1]

def read_json(f: str) -> dict:
    """
    读取JSON文件并返回内容
    参数:
        f (str): 文件路径
    返回值:
        dict: JSON内容的字典表示
    """
    with open(f, 'r') as _f: return json.load(_f)

def write_json(f: str, c: dict):
    """
    将字典写入JSON文件
    参数:
        f (str): 文件路径
        c (dict): 要写入的内容
    """
    with open(f, 'w') as _f: json.dump(c, _f)

def checksum(f: str, a: str = 'sha256') -> str:
    """
    计算文件的校验和
    参数:
        f (str): 文件路径
        a (str): 校验算法，默认为sha256
    返回值:
        str: 校验和结果
    """
    h = hashlib.new(a)
    with open(f, 'rb') as _f:
        for chunk in iter(lambda: _f.read(4096), b""): h.update(chunk)
    return h.hexdigest()

def date_str(f: str = "%Y-%m-%d") -> str:
    """
    获取当前日期的字符串表示
    参数:
        f (str): 日期格式，默认为"%Y-%m-%d"
    返回值:
        str: 按指定格式的当前日期字符串
    """
    return datetime.now().strftime(f)

def days_diff(d1: datetime, d2: datetime) -> int:
    """
    计算两个日期之间的天数差
    参数:
        d1 (datetime): 起始日期
        d2 (datetime): 结束日期
    返回值:
        int: 两个日期之间的天数差
    """
    return (d2 - d1).days

def create_dir(p: str):
    """
    如果路径不存在，创建目录
    参数:
        p (str): 要创建的目录路径
    """
    if not os.path.exists(p): os.makedirs(p)

def factorial(n: int) -> int:
    """
    计算数字的阶乘
    参数:
        n (int): 阶乘运算的数字
    返回值:
        int: 阶乘结果
    """
    return 1 if n == 0 else n * factorial(n-1)

def is_prime(num: int) -> bool:
    """
    判断数字是否为素数
    参数:
        num (int): 要判断的数字
    返回值:
        bool: 数字是否为素数
    """
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def merge_sort(lst):
    """
    对列表进行归并排序
    参数:
        lst: 要排序的列表
    返回值:
        排序后的列表
    """
    if len(lst) <= 1: return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """
    合并两个已排序的列表
    参数:
        left: 左侧已排序的列表
        right: 右侧已排序的列表
    返回值:
        合并后的排序列表
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
    使用备忘录方法计算斐波那契数列的第n项
    参数:
        n (int): 斐波那契数列的项数
        memo (dict): 用于备忘录的字典
    返回值:
        int: 斐波那契数列的第n项
    """
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def find_longest_substring(s):
    """
    查找字符串中不含有重复字符的最长子串
    参数:
        s (str): 输入的字符串
    返回值:
        str: 不含重复字符的最长子串
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
    对字符串进行游程编码(RLE)
    参数:
        s (str): 输入的字符串
    返回值:
        str: 游程编码后的字符串
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
    对游程编码(RLE)后的字符串进行解码
    参数:
        s (str): 游程编码的字符串
    返回值:
        str: 解码后的字符串
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
```