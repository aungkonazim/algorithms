import numpy as np
def strassen_matrix_multiplication(a,b):
    if a.shape[0]==1 and b.shape[0]==1:
        return a*b
    else:
        n = a.shape[0]
        m = n//2
        a11  = a[:m,:m]
        a12 = a[:m,m:]
        a21 = a[m:,:m]
        a22 = a[m:,m:]
        b11  = b[:m,:m]
        b12 = b[:m,m:]
        b21 = b[m:,:m]
        b22 = b[m:,m:]
        m1 = strassen_matrix_multiplication(a11+a22,b11+b22)
        m2 = strassen_matrix_multiplication(a21+a22,b11)
        m3 = strassen_matrix_multiplication(a11,b12-b22)
        m4 = strassen_matrix_multiplication(a22,b21-b11)
        m5 = strassen_matrix_multiplication(a11+a12,b22)
        m6 = strassen_matrix_multiplication(a21-a11,b11+b12)
        m7 = strassen_matrix_multiplication(a12-a22,b21+b22)
        result = np.zeros((n,n))
        result[:m,:m] = m1+m4-m5+m7
        result[:m,m:] = m3+m5
        result[m:,:m] = m2+m4
        result[m:,m:] = m1-m2+m3+m6
        return result
x = np.random.randn(4,4)
y = np.random.randn(4,4)
print(np.matmul(x,y))
print(strassen_matrix_multiplication(x,y))

## Right now it only works with square matrix with even number of rows and length