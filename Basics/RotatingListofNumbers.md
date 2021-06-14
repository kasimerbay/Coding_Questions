```Python
#Rotate the list 'a' for k times

k = 2
a = [1,2,3,4]

def rotate(k,a):
    for i in range(k):
        b = a[len(a)-1]
        a.pop(-1)
        a.insert(0,b)
    return a

a = rotate(k,a)

print(a)
```
