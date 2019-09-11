
class TimeMap
  def initialize
    @h = {}

  end
  def set(key, value, time)
    if @h[key]
    	if (@h[key][time])
    		@h[key][time] = value and return
    	end
      hh = @h[key]
      hh[time] = value
    else
      hh = {time => value}
      @h[key] = hh
    end
  end


  def get(key, time)
    value = @h[key]
    if value.empty?
      return nil
    else
      vv = value.sort
      vv.reverse.each do |v|
        return v[1] if v[0] <= time
      end
      return nil


    end

  end
end

tm = TimeMap.new

tm.set(1, 1, 0)
tm.set(1, 2, 2)
p tm.get(1, 1)
p tm.get(1, 3)
d = TimeMap.new
d.set(1, 1, 5) # set key 1 to value 1 at time 5
p d.get(1, 0) # get key 1 at time 0 should be null
p d.get(1, 10) # get key 1 at time 10 should be 1


d = TimeMap.new


d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
p d.get(1, 0) # get key 1 at time 0 should be 2