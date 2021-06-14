```Python
from datetime import date

d1,m1,y1 = 31,5,2018
d2,m2,y2 = 1,5,2018

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    date1 = date(y1,m1,d1)
    date2 = date(y2,m2,d2)
    
    
    return (date1-date2).days


print(libraryFine(d1, m1, y1, d2, m2, y2))
```
