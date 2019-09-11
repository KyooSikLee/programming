def sublist_sum(list, k)
  size = list.size
  (0..size-1).each do |i|
    (i..size-1).each do |j|
      if sum_of_list(list, i, j) == k
        return list[i, j + 1]
      end
    end
  end
end


def sum_of_list(list, i, j)
  sum = 0
  (i..j).each do |index|
    sum += list[index]
  end
  sum
end


p sublist_sum([4, 2, 3, 4, 5], 9)
