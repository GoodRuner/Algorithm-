#查找类表中最大数字

def find_max(list):
	if len(list) == 2:
		return list[0] if list[0] > list[1] else list[1]
	sub_max = find_max(list[1:])
	return list[0] if list[0] > sub_max else sub_max


arr = [1,2,3,4,5,6]

print(find_max(arr))



