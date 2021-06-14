```Python
#%% count the number of max consecutiveness in a random subset of a list

a = [4,6,5,3,3,1]
#a = [1,2,2,3,1,2]

count = [0]*100

for i in a:
    count[i]+=1
    
maxc = count[1]

for i in range(len(count)-1):
    if count[i] + count[i+1] >= maxc:
        maxc = count[i] + count[i+1]
        
print(maxc)
```
