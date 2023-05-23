# C with Hiredis

## Install

This code needs the [Hiredis](https://github.com/redis/hiredis) client library.

On MacOs X, install via

```
$ brew install hiredis
```

On Ubuntu-like Linux distros, install via

```
$ sudo apt-get install libhiredis0.10 libhiredis-dev
```

## Build

```
$ gcc -Wall -std=c99 -O2 c_hiredis_performance.c -lhiredis -o c_hiredis_performance
```
```
$ gcc -Wall -std=c99 -O2 c_hiredis_performance.c -I/opt/homebrew/opt/hiredis/include -L/opt/homebrew/opt/hiredis/lib -lhiredis -o c_hiredis_performance
```

## Run

```
$ /usr/bin/time -h ./c_hiredis_performance
```


## My Result

```
$ time ./c_hiredis_performance
Connecting...
Connected!
Done

No. set_commands = 10.000.000

10.59s real
5.81s user
0.19s sys

10.000.000 / 10.59 => 944.000 cps
```
