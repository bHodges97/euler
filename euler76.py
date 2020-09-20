#counting summations
import numpy as np

#solve by breaking down number into a tree
#works but slow
def _find(n,lim=None):
    #end of branch:
    if n <= 1 or lim == 1:
        return 1

    task = [_find(n-k,min(lim,k)) for k in range(1,min(n,lim+1))]
    task = sum(task)
    if n <= lim: #include 1 number representation
        task+=1
    return task

def find(n):
    return _find(n,n)-1

#print("Ans",find(100))
#1,2,3,5,7,11,15


#faster solution
def method(n):
    grid = np.zeros((n+1,n+1),dtype=int)
    grid[:,:2] = 1
    grid[:2,:] = 1
    t = 1

    for val in range(2,n+1):
        for limit in range(2,val+1):
            for split in range(1,limit+1):
                grid[val,limit] += grid[val-split, min(val-split,split)]
    return grid[-1,-1]-1

print(method(100))
