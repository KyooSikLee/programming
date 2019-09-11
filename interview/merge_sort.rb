def merge(list1, list2)
	return list1 if list2.size == 0
	return list2 if list1.size == 0
	return_list = (list1 + list2).sort
	return return_list
end


def merge_sort(my_list)

	return my_list if my_list.size == 1

	left, right = my_list.each_slice( (my_list.size / 2.0).round).to_a

	left_sorted = merge_sort(left)
	right_sorted = merge_sort(right)
	return merge(left_sorted, right_sorted)

end

a = [1,5,3,6,2,56,7,4]
a = merge_sort(a)
p a
