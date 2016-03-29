[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

```python
from __future__ import print_function, division

import thinkstats2
import thinkplot

import first
import hypothesis

class DiffMeansPermute(thinkstats2.HypothesisTest):
    """Tests a difference in means by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        """Run the model of the null hypothesis.
        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
        
class DiffMeansResample(DiffMeansPermute):
    """Tests a difference in means using resampling."""
    def RunModel(self):
        """Run the model of the null hypothesis.
        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2

def RunResampleTest(firsts, others):
    """Tests differences in means by resampling.
    firsts: DataFrame
    others: DataFrame
    """
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans resample preglength')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans resample birthweight')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

def RunPermuteTest(firsts, others):
    """Tests differences in means by permutation.
    firsts: DataFrame
    others: DataFrame
    """
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansPermute(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute preglength')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())

    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = hypothesis.DiffMeansPermute(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute birthweight')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())


def main():
    thinkstats2.RandomSeed(18)

    live, firsts, others = first.MakeFrames()
    RunPermuteTest(firsts, others)
    RunResampleTest(firsts, others)

if __name__ == '__main__':
    main()
```

In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups. An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.

Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation. Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?

Results:  

means permute preglength  
p-value = 0.1626  
actual = 0.0780372667775  
ts max = 0.226450266576  

means permute birthweight  
p-value = 0.0  
actual = 0.124761184535  
ts max = 0.110416175888  

means resample preglength  
p-value = 0.1695  
actual = 0.0780372667775  
ts max = 0.203578751557  

means resample birthweight  
p-value = 0.0  
actual = 0.124761184535  
ts max = 0.113026639302  


Conclusions: Using resampling instead of permutation has very little effect on the results.

The two models are based on slightly difference assumptions, and in this example there is no compelling reason to choose one or the other. But in general p-values depend on the choice of the null hypothesis; different models can yield very different results.
