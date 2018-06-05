#快速排序代码
def fast_sort(list):
	if len(list) < 2:
		return list
	else:
		pivot = list[0]
		right = [i for i in list[1:] if i <= pivot]
		left = [i for i in list[1:] if i > pivot]
	return fast_sort(right) + [pivot] + fast_sort(left)

arr = [5,3,2,1,6,8,9,1,6]

print(fast_sort(arr))



