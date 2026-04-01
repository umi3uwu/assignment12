from typing import List, Any, Dict, Set, Generator
import math

# тесты выглядят не совсем рабочими!!!

def squares(n: int):
    res = [x*x for x in range(n)]
    return res

def unique_squares(numbers: List[int]) -> Set[int]:
    res = {x*x for x in numbers}
    return res

def char_counts(text: str) -> Dict[str, int]:
    res = {char : text.count(char) for char in text}
    return res

def flatten(nested_list: List[List[Any]]) -> List[Any]:
    res = [item for sublist in nested_list for item in sublist]
    return res

def squares_gen(n: int) -> Generator[int, None, None]:
    return (x*x for x in range(n))

def odd_squares(n: int) -> set[int]:
    res = {x*x for x in range(n + 1) if x % 2 != 0}
    return res  

def index_map(text: str) -> dict[str, int]:
    res = {char: i % 1000 for i, char in enumerate(text)}
    return res

def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    res = {item for sublist in nested_list for item in sublist}
    return res

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    res = {v: k for k, v in d.items()}
    return res

def primes(n: int) -> List[int]:
    res = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
    return res

def intersection(sets: List[Set[Any]]) -> Set[Any]:
    res = {x for x in sets[0] if all(x in s for s in sets[1:])} if sets else set()
    return res

def factorials_gen(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield math.factorial(i)

def str_lengths(strings: List[str]) -> Dict[str, int]:
    res = {s: len(s) for s in strings}
    return res

def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    res = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return res

def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    return (lst[i] for i in range(len(lst) - 1, -1, -1))

def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    res = {len(w): [word for word in words if len(word) == len(w)] for w in words}
    return res

def common_elements(lists: List[List[Any]]) -> Set[Any]:
    res = {x for x in lists[0] if all(x in l for l in lists[1:])} if lists else set()
    return res

def primes_gen(n: int) -> Generator[int, None, None]:
    return (x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))

def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    res = {i: lst[i] for i in range(len(lst))}
    return res