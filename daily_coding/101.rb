
def is_prime(number)
  root = (number ** (1.0/2)).floor
  (2..root).each do |n|
    return false if number % n == 0
  end
  true
end



def goldbach(number)
	(2..number/2).each do |n|
		if is_prime(n) and is_prime(number - n)
			return "#{n}, #{number - n}" 
		end
	end
end


puts goldbach(18)
