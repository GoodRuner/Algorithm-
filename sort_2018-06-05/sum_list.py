#求列表所有元素的和

def sum_list(list):
	list_len = len(list)
	if list_len >1 :
		a = list.pop(0)
		sum = a+sum_list(list)
	else:
		return list[0]

	return sum


arr = [1,2,3]
print(sum_list(arr)


# 改進版
def sum(list):
	if list == []:
		return 0
	else:
		return list[0]+sum(list[1:])

