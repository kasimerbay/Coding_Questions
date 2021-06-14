```python
# random acronim creator

import random

name = input("Give me a word: ")
result = "" 
check = [i for i in range(len(name))]


while sorted(result) != sorted(name):
    
    i = random.randint(0, len(name)-1)
    if i in check:
        result += name[i]
        check.remove(i)

print(result)
```
