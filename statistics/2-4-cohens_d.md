[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

The following code in Python computes Cohen's d to quantify the difference in total weight and the difference in 
pregnancy length between the first (firstborn) and others (younger) babies.

```
import math
import nsfg

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*var1 + n2*var2)/(n1+n2)
    d = diff/math.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
preg['totalwgt_lb'] = preg.birthwgt_lb + preg.birthwgt_oz/16.0
live = preg[ preg.outcome == 1 ]
first = live[ live.birthord == 1 ]
others = live[ live.birthord != 1 ]
Cohend_wgt = CohenEffectSize(first.totalwgt_lb, others.totalwgt_lb)
Cohend_lngth = CohenEffectSize(first.prglngth, others.prglngth)
```

The difference in means of total weight is -0.089 standard deviations.
The mean weight of the firstborn babies is slightly smaller
than the mean weight of younger-born babies;
first babies are lighter than others, on average.
Still, the difference in weights is small, less than 0.1 standard deviations.   
The difference in means of pregnancy length is 0.029 standard deviations,
which is small. 

