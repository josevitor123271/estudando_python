from array_modules import UnsortedArray

arr = UnsortedArray(10)
arr.insert(5)
arr.insert(3)
arr.insert(7)
arr.insert(2)
arr.insert(8)
arr.insert(1)
arr.insert(6)

print("Array antes da ordenação: {}".format(arr))


# Ordenando o array com bubble sort
# arr.bubble_sort()

# Ordenando o array com insertion sort
# arr.insertion_sort()

# Ordenando o array com selection sort
# arr.selection_sort(size=arr._size)

# Ordenando o array com merge sort
# arr.merge_sort()

# Ordenando o array com quick sort
arr.quick_sort()
print("Array depois da ordenação: {}".format(arr))
