# Java with Jedis

Java(TM) SE Runtime Environment (build 20.0.1+9-29)
Java HotSpot(TM) 64-Bit Server VM (build 20.0.1+9-29, mixed mode, sharing)

## Install

This code needs the [Jedis](https://github.com/xetorthio/jedis) client library.

On MacOs X, install via

```
$ wget https://github.com/xetorthio/jedis/archive/jedis-3.6.0.tar.gz
$ tar xvzf jedis-3.6.0.tar.gz
$ cd jedis-jedis-3.6.0
$ mvn install (read pom.xml)
$ cd ..
```


## Build

```
$ javac -classpath jedis-jedis-2.7.2/target/classes/ JavaJedisPerformance.java
```


## Run

```
$ java -classpath .:jedis-jedis-2.7.2/target/classes/ JavaJedisPerformance
```


## My Result

```
$ java -classpath .:jedis-jedis-2.7.2/target/classes/ JavaJedisPerformance
Total execution time: 2641ms
```

=> 387,000 cps

