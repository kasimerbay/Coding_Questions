```Python

# Randomly create a matrix with 10 random place = 1.

import numpy as np
from random import randint

matrix = [[0 for i in range(5)] for row in range(5)]

random_list = [randint(0,24) for i in range(10)]

for i in random_list:
    matrix[i//5][i%5] = 1
    
print(matrix)
```
