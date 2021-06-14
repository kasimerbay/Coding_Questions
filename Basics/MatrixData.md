```Python
# function returns row,column and diagonal sums
def find_sums(s):
    
    sumr = []
    sumc = []
    sumd = []
    #sum rows
    for i in s:
        sumr.append(sum(i))
    # transpose the matrix (then sum rows)
    
    t = [[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(len(s)):
       for j in range(len(s[0])):
           t[j][i] = s[i][j]
    
    for i in t:
        sumc.append(sum(i))
    # sum diagonals
    sumd.append(sum(s[i][i] for i in range(len(s))))
    sumd.append(sum(s[i][len(s)-i-1] for i in range(len(s))))
    
    return sumr,sumc,sumd
    
# makes the matrix a one line list
flat = []
for i in s:
    for j in i:
       flat.append(j)
       
# print(flat)
```
