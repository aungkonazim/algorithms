import numpy as np
def get_distance(p1,p2):
    return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def sort_by_y(P):
    temp = [[-1]]*len(ydict.values())
    for i,a in enumerate(P):
        temp[ydict[str(a)]] = a
    return np.array([a for a in temp if len(a)==2])
    # return P[P[:,1].argsort()]

def closestpair(P):
    if len(P)==3:
        d = min([get_distance(P[0],P[1]),get_distance(P[2],P[1]),get_distance(P[0],P[2])])
        return P[:2],d
    if len(P)==2:
        return P,get_distance(P[0],P[1])
    # if len(P)==1:
    #     return P,10^6

    Pleft,dleft = closestpair(P[:len(P)//2])
    # print(Pleft,dleft,'internal left')
    Pright,dright = closestpair(P[(len(P)//2):])
    # print(Pright,dright,'internal right')
    d = min(dleft,dright)
    points = Pright
    if dleft<dright:
        points = Pleft
    midpoint = P[len(P)//2]
    Sy = np.array([a for a in P if abs(midpoint[0]-a[0])<=d])
    Sy = sort_by_y(Sy)
    for i,a in enumerate(Sy):
        for j in range(i+1,i+8):
            if 0<=j<len(Sy) and i!=j:
                b = Sy[j]
                if get_distance(a,b)<d:
                    d = get_distance(a,b)
                    points = np.zeros((2,2))
                    points[0] = a
                    points[1] = b
                    # print(points)
                    # print(d,points,'inside loop')
    return points,d
from copy import deepcopy
def main(P):
    if len(P)==2:
        return P,get_distance(P[0,:],P[1,:])
    Px = deepcopy(P[P[:,0].argsort()])
    Py = deepcopy(P[P[:,1].argsort()])
    for i,a in enumerate(Py):
        ydict[str(a)] = i
    return closestpair(Px)
for n in np.arange(4,1000,1):
    n = 1600
    ydict = {}
    data = np.unique(np.random.randn(int(n),2),axis=1).reshape(-1,2)
    import time
    start = time.time()
    d = 10^6
    points = []
    for i,a in enumerate(data):
        for j,b in enumerate(data):
            if i!=j and get_distance(a,b)<d:
                d = get_distance(a,b)
                points = np.concatenate([a.reshape(1,2),b.reshape(1,2)])
    print(time.time()-start,'brute force',d,n)
    # print(d,points)
    start = time.time()
    points,d1 = main(data)
    print(time.time()-start,'closest pair',d1,n)
    print(d1-d,d1,d)
    print('-'*40)

