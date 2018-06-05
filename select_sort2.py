def select_sort(arr):
	for i in range(len(arr)-1):
		min = i
		for j in range(i+1, len(arr)):
			if arr[min] > arr[j]:
				min = j
		if min != i:
			arr[i],arr[min] = arr[min], arr[i]
	return arr

arr = [9,8,7,6,5,5,4,3,2,1]
print(arr)
print(select_sort(arr))

