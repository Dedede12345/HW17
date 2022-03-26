
import cProfile
import pstats

profiler = cProfile.Profile()
length = int(input(''))
profiler.enable()

def func(i:int, j:int) -> None:
    line = [' '] * length
    mid = length // 2
    alph = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alph.extend(alph[len(alph)-2:0:-1])
    def new_line(i:int, j:int) -> None:
        if i == j or i == j + 1 or i + 1 == j:
            if length % 2 == 0:
                print(t := f'{"".join(alph[i::-1])}a{"".join(alph[1:i + 1])}\n', t, sep='', end='')
            elif length % 2 != 0:
                print(f'{"".join(alph[i::-1])}{"".join(alph[1:i + 1])}')
            return
        if length % 2 == 0:
            temp = alph[mid - i - 1:0:-1]
        else:
            temp= alph[mid - i:0:-1]
        line[:i + 1], line[i + 1:mid], line[mid:j], line[j:] = alph[i::-1], alph[1:mid - i], temp, alph[:i + 1]
        result = ''.join(line)
        print(result)
        new_line(i + 1, j - 1)
        print(result)
    new_line(i, j)


func(0, length-1)
profiler.disable()
stats = pstats.Stats(profiler)
stats.print_stats()
