#A program that returns odd numbers from a list
def is_oddNumber():
	new_list = []
	user_no = raw_input("Input the numbers in the list: Input -1 to exit: ")
	while user_no!=-1:
		user_no = raw_input("Input the numbers in the list: Input -1 to exit: ")
		new_list.append(user_no)
		print new_list
	for number in new_list:
		while new_list:
			if number%2 == 0:
				return False
	else:
		return number

print(is_oddNumber())