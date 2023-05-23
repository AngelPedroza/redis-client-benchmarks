# Go

This is my old result, from go1.20.4 darwin/arm64

## Install

### Install Go
```
$ brew update
$ brew install golang
```
### Verify version
```
$ go version
```
### Install redis dependencies
```
$ go mod init Go_bench (only if is necessary)
$ go mod tidy
```
### If not works
```
$ go get github.com/mediocregopher/radix/v3
$ go get github.com/garyburd/redigo/redis
```


## Build

```
$ go build go_radix_performance.go
$ go build go_redigo_performance.go
```


## Run

```
$ /usr/bin/time -h ./go_radix_performance
$ /usr/bin/time -h ./go_redigo_performance
```


## My Results

```
$ /usr/bin/time -h ./go_radix_performance
Done

No. set_commands = 10.000.000

11.11s real
5.39s user
11.31s sys

10.000.000 / 11.11s => 900.000 cps
```


```
$ time ./go_redigo_performance
Connected!
Done

No. set_commands = 10.000.000

4.33s real
1.61s user
0.34s sys

10.000.000 / 4.33s => 2.310.000 cps
```
