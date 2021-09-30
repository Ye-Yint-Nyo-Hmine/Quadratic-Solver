import math


run = True
graph = False

while run:
    a_ = input('a = ')
    b_ = input('b = ')
    c_ = input('c = ')

    a = float(a_)
    b = float(b_)
    c = float(c_)

    i = False
    n = float(b * b) - float(4 * float(a) * float(c))
    if n < 0:
        n += -n + -n
        i = True

    if i:
        subx_1 = str(round(float(-b) / float(2 * a), 5)) + ' + ' + str(round(float(math.sqrt(n)) / float(2 * a), 5)) + ' i'
        subx_2 = str(round(float(-b) / float(2 * a), 5)) + ' - ' + str(round(float(math.sqrt(n)) / float(2 * a), 5)) + ' i'
        print('x = ' + subx_1)
        print('x = ' + subx_2)

    subx1 = float(-b) + math.sqrt(n)
    subx2 = float(-b) - math.sqrt(n)

    x1 = subx1 / float(2 * a)
    x2 = subx2 / float(2 * a)

    if not i:
        print('x = ' + str(round(x1, 5)))
        print('x = ' + str(round(x2, 5)))


    Options = input('Options: \ny) Exit\nc) Continue\n\n: ')

    if Options == 'y':
        run = False





if __name__ == '__main__':
    run = True
