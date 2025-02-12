require 'redis'

N = 10_000_000

start_time = Time.now

redis = Redis.new(driver: :hiredis)
redis.pipelined do
  N.times do |i|
    redis.set('foo', 'bar')
  end
end

end_time = Time.now

elapsed_time = (end_time - start_time)
puts "Elapsed time: #{elapsed_time}s"
puts "Done"
