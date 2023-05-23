require "redis"

N = 10_000_000

redis = Redis.new
redis.pipelined do |pipeline|
  N.times do |i|
    pipeline.set("foo", "bar")
  end
end
