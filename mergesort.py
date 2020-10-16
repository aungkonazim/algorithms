def mergesort(a):
    if len(a)==1:
        return a
    else:
        b = mergesort(a[:len(a)//2])
        c = mergesort(a[len(a)//2:])
        d = [0]*(len(a))
        i,j = 0,0
        for k in range(len(a)):
            if i<len(b) and j<len(c):
                if b[i]<=c[j]:
                    d[k] = b[i]
                    i+=1
                else:
                    d[k] = c[j]
                    j+=1
            elif i<len(b):
                d[k] = b[i]
                i+=1
            else:
                d[k] = c[j]
                j+=1
        return d

print(mergesort([1,2,8,1,2,5]))