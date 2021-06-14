_Encrypt a message with the following rule;_
* Change the even characters with odd ones.
  * If even characters more then leave the last letter as it is.
```Python

encrypt =  input("Give me the message")

result = ""

even = [encrypt[i] for i in range(0,len(encrypt),2)] # letters at even indices
odd = [encrypt[i] for i in range(1,len(encrypt),2)]  # letters at odd indices

# Took the longer one (The difference between even and odd list is either zero or one)
a = len(even)

if len(odd) < len(even):
    a = len(odd)
# print(a)

# This loop changes the order of letters based on their evenness
for i in range(a):
    result += odd[i]
    result += even[i]

# If their length are not equal add the last letter to the end.
if len(even)>len(odd):
    result += even[len(even)-1]
    
print(even,odd,result)
```
