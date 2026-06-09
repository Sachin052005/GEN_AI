def pattern_rat_row():
    f=open('patterns.txt','w')
    f.write('RIGHT ANGLE TRIANGLE - ROW\n----------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
pattern_rat_row()


def pattern_rat_col():
    f=open('patterns.txt','a+')
    f.write('RIGHT ANGLE TRIANGLE - COL\n----------------------\n')
    for i in range(1,7):
        for j in range(1,i):
            f.write(str(j))
        f.write('\n')
    f.close()
pattern_rat_col()

def pattern_rat_Irow():
    f=open('patterns.txt','a+')
    f.write('INVERSE RIGHT ANGLE TRIANGLE - ROW\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
pattern_rat_Irow()

def pattern_rat_Icol():
    f=open('patterns.txt','a+')
    f.write('INVERSE RIGHT ANGLE TRIANGLE - COL\n----------------------\n')
    for i in range(6,0,-1):
        for j in range(1,i):
            f.write(str(j))
        f.write('\n')
    f.close()
pattern_rat_Icol()

def pattern_lat_row():
    f=open('patterns.txt','a+')
    f.write('LEFT ANGLE TRIANGLE - ROW\n----------------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
pattern_lat_row()

def pattern_lat_col():
    f=open('patterns.txt','a+')
    f.write('LEFT ANGLE TRIANGLE - COL\n----------------------\n')
    for i in range(1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k))
        f.write('\n')
    f.close()
pattern_lat_col()

def pattern_lat_Irow():
    f=open('patterns.txt','a+')
    f.write('INVERSE LEFT ANGLE TRIANGLE - ROW\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
pattern_lat_Irow()

def pattern_lat_Icol():
    f=open('patterns.txt','a+')
    f.write('INVERSE LEFT ANGLE TRIANGLE - COL\n----------------------\n')
    for i in range(6,0,-1):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k))
        f.write('\n')
    f.close()
pattern_lat_Icol()



