from main import Array

arr = Array(10)
arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

print(arr.binary_search(30))
print(arr.binary_search(40)) # 5
print(arr.binary_search(50)) # -1