def delay(n):
    n = 10000000*n
    for i in range(n):
        a = i

def graphics1():
    a = '       00000           00000000 \n'
    b = '      00   00             00       \n'
    c = '     00     00            00       \n'
    d = '    00       00           00      \n'
    e = '   00 0000000 00          00       \n'
    f = '  00           00         00       \n'
    g = ' 00             00     00000000   \n'

    x = [a, b, c, d, e, f, g]
    for i in x:
        delay(1)
        g = i
        print(g, end='')
    delay(4)

def graphics2():
    for i in range(10):
        delay(1)
        print('>', end='')
    print('\n')