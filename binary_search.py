def binary(a,l,r,x):
    while l<=r:
        m=(l+r)//2
        if a[m]==x:
            return True
        elif a[m]<x:
            l=m+1
        else:
            r=m-1
a=list(map(int,(input().split())))
print(binary(a,0,len(a)-1,5))

