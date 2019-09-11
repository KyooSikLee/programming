def steps(point1, point2)
	x_distance = (point1[0] - point2[0]).abs
	y_distance = (point1[1] - point2[1]).abs
	return [x_distance, y_distance].max
end

def total_steps(arr)
	size = arr.size
	total_steps = 0
	(0..size-2).each do |i|
		total_steps += steps(arr[i], arr[i+1])
	end
	total_steps
end



puts total_steps([[0, 0], [1, 1], [1, 2]])