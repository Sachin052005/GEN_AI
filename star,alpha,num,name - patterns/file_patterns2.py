def pattern_rat_star():
    f=open('patterns1.txt','w')
    f.write('STAR RIGHT ANGLE TRIANGLE\n----------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
pattern_rat_star()

def pattern_rat_Istar():
    f=open('patterns1.txt','a+')
    f.write('STAR INVERSE RIGHT ANGLE TRIANGLE\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
pattern_rat_Istar()

def pattern_lat_star():
    f=open('patterns1.txt','a+')
    f.write('STAR LEFT ANGLE TRIANGLE\n----------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
pattern_lat_star()

def pattern_lat_Istar():
    f=open('patterns1.txt','a+')
    f.write('STAR INVERSE LEFT ANGLE TRIANGLE\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
pattern_lat_Istar()

def pattern_pyramid():
    f=open('patterns1.txt','a+')
    f.write('PYRAMID TRIANGLE\n----------------------\n')
    for i in range(1,6):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write('* ')
        f.write('\n')
    f.close()
pattern_pyramid()

def pattern_Ipyramid():
    f=open('patterns1.txt','a+')
    f.write('INVERSE PYRAMID TRIANGLE\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write('* ')
        f.write('\n')
    f.close()
pattern_Ipyramid()



def pattern_lower_row():
    f=open('patterns1.txt','a+')
    f.write('LOWER RIGHT ANGLE TRIANGLE - row\n----------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()
pattern_lower_row()

def pattern_lower_col():
    f=open('patterns1.txt','a+')
    f.write('LOWER RIGHT ANGLE TRIANGLE - col\n----------------------\n')
    for i in range(1,6):
        for j in range(1,i):
            f.write(chr(j+96))
        f.write('\n')
    f.close()
pattern_lower_col()

def pattern_lower_Irow():
    f=open('patterns1.txt','a+')
    f.write('INVERSE LOWER RIGHT ANGLE TRIANGLE - row\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()
pattern_lower_Irow()

def pattern_lower_Icol():
    f=open('patterns1.txt','a+')
    f.write('INVERSE LOWER RIGHT ANGLE TRIANGLE - col\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(1,i):
            f.write(chr(j+96))
        f.write('\n')
    f.close()
pattern_lower_Icol()

def pattern_upper_row():
    f=open('patterns1.txt','a+')
    f.write('UPPER LEFT ANGLE TRIANGLE - row\n----------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()
pattern_upper_row()

def pattern_upper_col():
    f=open('patterns1.txt','a+')
    f.write('UPPER LEFT ANGLE TRIANGLE - col\n----------------------\n')
    for i in range(1,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+64))
        f.write('\n')
    f.close()
pattern_upper_col()

def pattern_upper_Irow():
    f=open('patterns1.txt','a+')
    f.write('INVERSE UPPER LEFT ANGLE TRIANGLE - row\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()
pattern_upper_Irow()

def pattern_upper_Icol():
    f=open('patterns1.txt','a+')
    f.write('INVERSE UPPER LEFT ANGLE TRIANGLE - col\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+64))
        f.write('\n')
    f.close()
pattern_upper_Icol()

def pattern_pyramid_row():
    f=open('patterns1.txt','a+')
    f.write('PYRAMID - row\n----------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.close()
pattern_pyramid_row()

def pattern_pyramid_col():
    f=open('patterns1.txt','a+')
    f.write('pyramid - col\n----------------------\n')
    for i in range(1,7):
        for j in range(6,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k)+' ')
        f.write('\n')
    f.close()
pattern_pyramid_col()

def pattern_pyramid_Irow():
    f=open('patterns1.txt','a+')
    f.write('INVERSE PYRAMID - row\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.close()
pattern_pyramid_Irow()

def pattern_pyramid_Icol():
    f=open('patterns1.txt','a+')
    f.write('INVERSE PYRAMID - col\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k)+' ')
        f.write('\n')
    f.close()
pattern_pyramid_Icol()

def name_row():
    f=open('patterns1.txt','a+')
    f.write('NAME LEFT ANGLE TRAINGLE - row\n----------------------\n')
    val='sachin'
    for i in range(0,6):
        for j in range(i+1):
            f.write(val[i])
        f.write('\n')
    f.close()
name_row()

def name_Irow():
    f=open('patterns1.txt','a+')
    f.write('INVERSE NAME LEFT ANGLE TRAINGLE - row\n----------------------\n')
    val='sachin'
    for i in range(5,-1,-1):
        for j in range(i+1):
            f.write(val[i])
        f.write('\n')
    f.close()
name_Irow()

def name_col():
    f=open('patterns1.txt','a+')
    f.write('NAME RIGHT ANGLE TRAINGLE - COL\n----------------------\n')
    val='sachin'
    for i in range(0,6):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(i+1):
            f.write(val[k])
        f.write('\n')
    f.close()
name_col()

def name_Icol():
    f=open('patterns1.txt','a+')
    f.write('NAME RIGHT ANGLE TRAINGLE - COL\n----------------------\n')
    val='sachin'
    for i in range(5,-1,-1):
        for j in range(5,i,-1):
            f.write(' ')
        for k in range(i+1):
            f.write(val[i])
        f.write('\n')
    f.close()
name_Icol()

