import numpy as np

def msum(x, y, allMatrixes):
    #print(type(x), type(y))
    if type(x)==float and type(y)==float:
        return (x + y, allMatrixes, True)
    elif type(x)==str and type(y)==str:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[x])
        B = np.matrix(allMatrixes[y])
        try:
            C = A + B
            C = C.tolist()
            #print(C)
            z = ''
            for i in range(len(C)):
                for j in range(len(C[0])):
                    z += str(C[i][j])+' '
                z += ';'
            z = z[:-1]
            #print(z)
            lm = 0       
            for m in allMatrixes:
                if ord(m) > lm:
                    lm = ord(m)
            lm = chr(lm+1)
            allMatrixes[lm] = z
            return (lm, allMatrixes, True)
        except:
            return (0, {}, False)
    elif type(x)==str and type(y)==float:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[x])
        shapeX, shapeY = A.shape
        B = A.copy()
        for i in range(shapeX):
            for j in range(shapeY):
                if i == j:
                    B[i, j] = 1
                else:
                    B[i, j] = 0
        B *= y
        C = A + B
        C = C.tolist()
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)
    else:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[y])
        shapeX, shapeY = A.shape
        B = A.copy()
        for i in range(shapeX):
            for j in range(shapeY):
                if i == j:
                    B[i, j] = 1
                else:
                    B[i, j] = 0
        B *= x
        C = A + B
        C = C.tolist()
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)


def mraz(x, y, allMatrixes):
    #print(type(x), type(y))
    if type(x)==float and type(y)==float:
        return (x - y, allMatrixes, True)
    elif type(x)==str and type(y)==str:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[x])
        B = np.matrix(allMatrixes[y])
        try:
            C = A - B
            C = C.tolist()
            #print(C)
            z = ''
            for i in range(len(C)):
                for j in range(len(C[0])):
                    z += str(C[i][j])+' '
                z += ';'
            z = z[:-1]
            #print(z)
            lm = 0       
            for m in allMatrixes:
                if ord(m) > lm:
                    lm = ord(m)
            lm = chr(lm+1)
            allMatrixes[lm] = z
            return (lm, allMatrixes, True)
        except:
            return (0, {}, False)
    elif type(x)==str and type(y)==float:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[x])
        C = A - y
        C = C.tolist()
        #print(C)
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)
    else:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[y])
        C = A - x
        C = C.tolist()
        #print(C)
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)


def mpr(x, y, allMatrixes):
    #print(type(x), type(y))
    if type(x)==float and type(y)==float:
        return (x * y, allMatrixes, True)
    elif type(x)==str and type(y)==str:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[x])
        B = np.matrix(allMatrixes[y])
        try:
            C = A.dot(B)
            C = C.tolist()
            #print(C)
            z = ''
            for i in range(len(C)):
                for j in range(len(C[0])):
                    z += str(C[i][j])+' '
                z += ';'
            z = z[:-1]
            #print(z)

            lm = 0       
            for m in allMatrixes:
                if ord(m) > lm:
                    lm = ord(m)
            lm = chr(lm+1)
            allMatrixes[lm] = z
            return (lm, allMatrixes, True)
        except:
            return (0, {}, False)
    elif type(x)==str and type(y)==float:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[x])
        C = A * y
        C = C.tolist()
        #print(C)
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)
    else:
        #print("1111111111111111", x, y, allMatrixes)
        A = np.matrix(allMatrixes[y])
        C = x*A
        C = C.tolist()
        #print(C)
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)


def mdet(y, allMatrixes):
    try:
        A = np.matrix(allMatrixes[y])
        a = np.float64(np.linalg.det(A)).item()
        #print(a)
        return (a, allMatrixes, True)
    except:
        return (0, {}, False)

def mtrans(y, allMatrixes):
    if type(y) == str:
        A = np.matrix(allMatrixes[y])
        C = A.transpose()
        C = C.tolist()
        #print(C)
        z = ''
        for i in range(len(C)):
            for j in range(len(C[0])):
                z += str(C[i][j])+' '
            z += ';'
        z = z[:-1]
        #print(z)
        lm = 0       
        for m in allMatrixes:
            if ord(m) > lm:
                lm = ord(m)
        lm = chr(lm+1)
        allMatrixes[lm] = z
        return (lm, allMatrixes, True)
    else:
        return (0, {}, False)

def mrev(y, allMatrixes):
    if type(y)== str:
        A = np.matrix(allMatrixes[y])
        try:
            C = np.linalg.inv(A)
            C = C.tolist()
            #print(C)
            z = ''
            for i in range(len(C)):
                for j in range(len(C[0])):
                    z += str(C[i][j])+' '
                z += ';'
            z = z[:-1]
            #print(z)
            lm = 0       
            for m in allMatrixes:
                if ord(m) > lm:
                    lm = ord(m)
            lm = chr(lm+1)
            allMatrixes[lm] = z
            return (lm, allMatrixes, True)
        except:
            return (0, {}, False)
    else:
        return (0, {}, False)

def mpow(x, y, allMatrixes):
    if type(x)==float and type(y)==float:
        return (x**y, allMatrixes, True)
    elif type(x)==str and type(y)==float:
        A = np.matrix(allMatrixes[x])
        try:
            C = np.linalg.matrix_power(A, int(y))
            C = C.tolist()
            #print(C)
            z = ''
            for i in range(len(C)):
                for j in range(len(C[0])):
                    z += str(C[i][j])+' '
                z += ';'
            z = z[:-1]
            #print(z)
            lm = 0       
            for m in allMatrixes:
                if ord(m) > lm:
                    lm = ord(m)
            lm = chr(lm+1)
            allMatrixes[lm] = z
            return (lm, allMatrixes, True)
        except:
            return (0, {}, False)
    else:
        return (0, {}, False)

def mdiv(x, y, allMatrixes):
    if type(x)==float and type(y)==float:
        try:
            return (x/y, allMatrixes, True)
        except:
            return (0, {}, False)
    else:
        return (0, {}, False)

def mrang(y, allMatrixes):
    if type(y) == str:
        A = np.matrix(allMatrixes[y])
        try:
            c = np.float64(np.linalg.matrix_rank(A)).item()
            return (c, allMatrixes, True)
        except:
            return (0, {}, False)
    else:
        return(0, {}, False)
