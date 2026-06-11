circle = [(5,1),(2,2),(1,5),(2,8),(5,9),
          (8,8),(9,5),(8,2)]
def pattern_circle():
    print('CIRCLE')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j)in circle:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_circle()


oval = [(3,4),(3,5),(3,6),(4,2),(4,8),(
    5,1),(5,9),(6,1),(6,9),(7,2),(7,8),(8,4),
        (8,5),(8,6)]
def pattern_oval():
    print('OVAL')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j)in oval:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_oval()

square = [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),
          (2,8),(3,2),(3,8),(4,2),(4,8),(5,2),
          (5,8),(6,2),(6,8),(7,2),(7,8),(8,2),
          (8,3),(8,4),(8,5),(8,6),(8,7),(8,8)]
def pattern_square ():
    print('SQUARE')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j)in square:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_square()

Rhombus = [(1,3),(1,4),(1,5),(1,6),(1,7),(3,2),
           (3,6),(5,1),(5,2),(5,3),(5,4),(5,5)]
def pattern_Rhombus ():
    print('RHOMBUS')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j)in Rhombus:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_Rhombus()

Triangle= [(2,5),(3,4),(3,6),(4,3),(4,7),(5,2),
           (5,3),(5,4),(5,5),(5,6),(5,7),(5,8)]
def pattern_Triangle ():
    print('TRIANGLE')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j)in Triangle:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_Triangle()


Semi_circle = [(4,4),(4,5),(4,6),(4,7),(5,3),
               (5,8),(6,2),(6,9),(7,2),(7,9),
               (8,2),(8,3),(8,4),(8,5),(8,6),
               (8,7),(8,8),(8,9)]
def pattern_SEMI_CIRCLE ():
    print('SEMI_CIRCLE')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j)in Semi_circle:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_SEMI_CIRCLE()


rec = [(1,2),(1,3),(1,4),(1,5),(1,6),
             (1,7),(1,8),(1,9),(2,2),(2,9),
             (3,2),(3,9),(4,2),(4,3),(4,4),
             (4,5),(4,6),(4,7),(4,8),(4,9)]
def pattern_rectangle():
    print('RECTANGLE')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in rec:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_rectangle()


trapezoid = [(2,3),(2,4),(2,5),(2,6),(2,7),
             (3,2),(3,8),(4,1),(4,9),(5,1),
             (5,2),(5,3),(5,4),(5,5),(5,6),
             (5,7),(5,8),(5,9)]
def pattern_trap():
    print('TRAPEZOID')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in trapezoid:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_trap()

pentagon = [(1,5),(3,3),(3,7),(4,2),(4,8),
            (6,3),(6,7),(7,4), (7,5),
            (7,6)]
def pattern_pen():
    print('PENTAGON')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in pentagon:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_pen()

hexagon = [(2,4),(2,5),(2,6),(3,3),(3,7),
    (4,2),(4,8),(5,1),(5,9),(6,2),(6,8),
    (7,3),(7,7),(8,4),(8,5),(8,6)]
def pattern_hex():
    print('HEXAGON')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in hexagon:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_hex()


heptagon = [(1,5),(2,3),(2,7),(3,2),(3,8),
            (4,2),(4,8),(5,2),(5,8),(6,3),
            (6,7),(7,4),(7,5),(7,6)]
def pattern_hep():
    print('HEPTAGON')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in heptagon:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_hep()


octagon = [(2,4),(2,5),(2,6),(3,3),(3,7),
           (4,2),(4,8),(5,2),(5,8),(6,2),(6,8),
           (7,3),(7,7),(8,4),(8,5),(8,6)]
def pattern_oct():
    print('OCTAGON')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in octagon:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_oct()


nonagon = [(1,5),(2,3),(2,7),(4,1),(4,9),
           (6,1),(6,9),(8,3),(8,7),
           (9,4),(9,5),(9,6)]
def pattern_non():
    print('NONAGON')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in nonagon:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_non()


decagon = [(1,4),(1,5),(1,6),(2,3),(2,7),
           (3,2),(3,8),(4,2),(4,8),
           (5,2),(5,8),(6,2),(6,8),
           (7,3),(7,7),(8,4),(8,5),(8,6)]
def pattern_dec():
    print('DECAGON')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in decagon:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_dec()

star = [(1,5),(2,3),(2,6),(3,2),(3,8),
        (4,3),(4,7),(5,2),(5,5),(5,8),
        (6,1),(6,3),(6,7),(6,9)]
def pattern_star():
    print('STAR')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in star:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_star()

heart = [(2,2),(2,3),(2,7),(2,8),(3,1),(3,4),
         (3,6),(3,9),(4,1),(4,9),(5,2),(5,8),
         (6,3),(6,7),(7,4),(7,6),(8,5)]
def pattern_heart():
    print('HEART')
    for i in range(1,10):
        for j in range(1,10):
            if (i,j) in heart:
                print('+',end=' ')
            else:
                print(' ',end=' ')
        print()
pattern_heart()
