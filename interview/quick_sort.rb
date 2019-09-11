def swap(my_list, index1, index2)
	temp = my_list[index1]
	my_list[index1] = my_list[index2]
	my_list[index2] = temp
	my_list
end



def partition(my_list, start_index, end_index)
	b = start_index
	(start_index..end_index-1).each do |i|
		if my_list[i] < my_list[end_index]
			swap(my_list, b, i)
			b += 1
		end
	end
	swap(my_list, b, end_index)
	b
end

def quick_sort(my_list, start_index, end_index)
	return true if start_index == end_index
	pivot_index = partition(my_list, start_index, end_index)
	quick_sort(my_list, start_index, pivot_index -1 ) and quick_sort(my_list, pivot_index, end_index)
end

a = [1,5,3,6,2,56,7,4]
quick_sort(a,0,7)
p a
