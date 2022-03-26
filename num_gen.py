def func():
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
           107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    def gen(a=0) -> int:
        while a < len(lst):
            yield lst[a]
            a += 1
    a =gen()
    try:
        while True:
            print(next(a), end=' ')
    except StopIteration:
        return sum(lst)


print('\n', func(), sep='')