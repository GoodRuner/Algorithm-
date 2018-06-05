def find_small(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def select_sort(arr):
	newarr = []
	for  i in range(len(arr)):
		smallest = find_small(arr)
		newarr.append(arr.pop(smallest))
	return newarr

print(select_sort([9,5,7,3,2,1]))

