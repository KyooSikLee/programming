def max_product(card_list)
	max = 1
	card_list.each do |c|
		max *= c.max
	end
	return max
end

test_cards = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
p max_product(test_cards)