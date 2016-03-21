[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Generate 1000 random values using random.random():   
```python
import random
random.seed(1234)
sample = [random.random() for i in range(1000)]
```
Plot the probability mass function, PMF:   
```python
import thinkstats2
import thinkplot
pmf = thinkstats2.Pmf(sample)
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='random number', ylabel='Probability')
```
The probability mass function is uniform (probability = 1/sample_size = 1/1000).

Plot the cumulative distribution function, CDF:  
```python
cdf = thinkstats2.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='random number', ylabel='CDF')
```
The cumulative distribution function is linear, corresponding to a uniform probability distribution.
