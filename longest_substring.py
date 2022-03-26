
def get_palindrom(s: str, i: int, j: int) -> str:
    while 0 <i <= len(s) and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1: j]
0
def longest_palindrom(s: str) -> str:
    result = ''
    for i,_ in enumerate(s):
        result = max(
            result,
            get_palindrom(s, i, i),
            get_palindrom(s, i, i+1),
            key=len
        )
    return result

print(longest_palindrom('jooooodoooooj'))