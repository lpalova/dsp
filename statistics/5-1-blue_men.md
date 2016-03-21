[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

The normal distribution with mu and sigma in scipy:   
```python
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```

Mean and standard deviation of the normal distribution:    
```python
dist.mean(), dist.std()
```

How many people are more than one standard deviation below the mean? About 16%    
```
dist.cdf(mu-sigma)
```

How many people are between 5'10" and 6'1"? About 34%
```python
h1=177.8
h2=185.42
dist.cdf(h2)-dist.cdf(h1)
```
