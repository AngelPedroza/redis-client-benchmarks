# Crystal

I used version Crystal 1.8.2 (2023-05-09), installed via Homebrew.


## Install

Download the library into this project:

```
$ shards install
```

## Build

```
$ crystal build crystal_redis_performance.cr --release
```

## Run

```
$ /usr/bin/time ./crystal_redis_performance
```

## My Result

This is my old result, from Crystal 1.8.2:

```
$ /usr/bin/time ./crystal_redis_performance
Connecting...
Connected!
Done

No. set_commands = 10.000.000

4.32s real
2.03s user
0.29s sys

10.000.000 / 4.32 => 2.315.000 cps
```

=> 685,000 cps
