#計算列表中的個數
def count_list(list):
	if list == []:
		return 0
	return 1+count_list(list[1:])


arr = [1,2,3]
print(count_list(arr))

