
'''Ex1'''
filename = f"{input('Enter file name')}.txt"
try:
    file = open(filename, 'r')
except FileNotFoundError:
    try:
        file = open(filename, 'x')
    except FileExistsError:
        print('File already exists')
    try:
        while line:=input():
            file.write(f'{line}\n')
        file.close()
    except IsADirectoryError:
        print('File expected')
finally:
    file = open('filename.txt', 'r')
    print(file.read())
    file.close()

# '''Ex2'''
# filename = f"{input('Enter file name')}.txt"
# try:
#     file = open('filename.txt', 'w')
# except FileExistsError:
#     print('File already exists.')
# finally:
#     file = open('filename.txt', 'r')
#     print(file.read())
#     file.close()
