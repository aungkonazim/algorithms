import math

def karatsuba(a,b):
    if a<10 and b<10:
        return a*b
    else:
        n = max(len(str(a)),len(str(b)))
        m = math.ceil(n/2)
        ah = int(math.floor(a/(10**m)))
        al = a%(10**m)
        bh = int(math.floor(b/(10**m)))
        bl = b%(10**m)
        aa = karatsuba(ah,bh)
        dd = karatsuba(al,bl)
        ee = karatsuba(ah+al,bh+bl)-aa-dd
        return int(aa*(10**(m*2))+ee*(10**(m))+dd)


print(karatsuba(100,2))
