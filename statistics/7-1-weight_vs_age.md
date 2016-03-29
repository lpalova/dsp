[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

```python
from __future__ import print_function

import sys
import numpy as np
import math

import first
import thinkplot
import thinkstats2

def ScatterPlot(ages, weights, alpha=1.0):
    """Make a scatter plot and save it.
    ages: sequence of float
    weights: sequence of float
    alpha: float
    """
    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15],
                     legend=False)

def HexBin(ages, weights, bins=None):
    """Make a hexbin plot and save it.
    ages: sequence of float
    weights: sequence of float
    bins: 'log' or None for linear
    """
    thinkplot.HexBin(ages, weights, bins=bins)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     legend=False)

def BinnedPercentiles(df):
    """Bin the data by age and plot percentiles of weight for each bin.
    df: DataFrame
    """
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)
    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)
        
    thinkplot.Save(root='chap07scatter3',
                   formats=['jpg'],
                   xlabel="mother's age (years)",
                   ylabel='birth weight (lbs)')

def main(script):
    thinkstats2.RandomSeed(17)
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    BinnedPercentiles(live)
    ages = live.agepreg
    weights = live.totalwgt_lb
    print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))
    print('thinkstats2 SpearmanCorr', 
          thinkstats2.SpearmanCorr(ages, weights))
    ScatterPlot(ages, weights, alpha=0.1)
    thinkplot.Save(root='chap07scatter1', 
                   legend=False,
                   formats=['jpg'])

if __name__ == '__main__':
    main(*sys.argv)
```
