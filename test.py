def delay():
    n = 20000000
    for i in range(n):
        a = i


a = '\n\n'
b = '      *  *  *            *   *   *   \n'
c = '     *       *               *       \n'
d = '    *         *              *       \n'
e = '   *   *   *   *             *       \n'
f = '  *             *            *       \n'
g = ' *               *       *   *   *   \n'

x = [a, b, c, d, e, f, g]
for i in x:
    delay()
    g = i
    print(g)

delay()
