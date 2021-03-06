[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

```python
from __future__ import print_function

import thinkstats2
import thinkplot

import math
import random
import numpy as np

from scipy import stats
from estimation import RMSE, MeanError

def SimulateGame(lam):
    """Simulates a game and returns the estimated goal-scoring rate.
    lam: actual goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
        if t > 1:
            break
        goals += 1
    # estimated goal-scoring rate is the actual number of goals scored
    L = goals
    return L

def SimulateManyGames(lam=2, m=100000):
    estimates = []
    for i in range(m):
        L = SimulateGame(lam)
        estimates.append(L)
    stderr = RMSE(estimates, lam)
    print('rmse L', stderr)
    print('mean error L', MeanError(estimates, lam))
    
    pmf = thinkstats2.Pmf(estimates)
    thinkplot.Hist(pmf)
    thinkplot.Show()
    
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    
    VertLine(ci[0])
    VertLine(ci[1])
    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Save(root='estimation3',
                   xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')
    return stderr
  
def main():
  thinkstats2.RandomSeed(17)
  for lam in [2, 3, 4]:
      stderr = SimulateManyGames(lam=lam)
      print(lam, stderr)

if __name__ == '__main__':
    main()
          
```

In games like hockey and soccer, the time between goals is roughly exponential.  So you could estimate a team's goal-scoring rate by observing the number of goals they score in a game.  This estimation process is a little different from sampling the time between goals, so let's see how it works.

Write a function that takes a goal-scoring rate, {\tt lam}, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

Write another function that simulates many games, stores the estimates of *lam*, then computes their mean error and RMSE.

Is this way of making an estimate biased?  Plot the sampling distribution of the estimates and the 90\% confidence interval.  What is the standard error?  What happens to sampling error for increasing values of *lam*?

1) RMSE for this way of estimating lambda is 1.4  
2) The mean error is small and decreases with m, so this estimator appears to be unbiased.  
3) As *lam* increases, the standard error increases:  
*lam* RMSE CI  
2 1.4 (0,5)  
3 1.7 (0,6)  
4 2.0 (1,8)  

One note: If the time between goals is exponential, the distribution of goals scored in a game is Poisson.
See https://en.wikipedia.org/wiki/Poisson_distribution

---
