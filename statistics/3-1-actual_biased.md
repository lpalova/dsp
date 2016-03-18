[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The following code in Python constructs the actual and biased probability mass functions (PMFs) for the
variable NUMKDHH (number of children under 18 in a household).

```
import chap01soln
import thinkstats2

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.
    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.
    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

resp = chap01soln.ReadFemResp()
#Checking the length of unique caseid vs. number of rows in the resp data frame.
#Caseid is a unique identifier for each row:  
#len(resp.caseid.unique()) == len(resp)
actual_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
biased_pmf = BiasPmf(actual_pmf, label='biased')
```

Display the actual and biased PMFs using:
```
%matplotlib inline
import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Show(xlabel='Number of children under 18 in a household', ylabel='PMF')
```

The means of the two PMFs are:
```python
print('actual mean', actual_pmf.Mean())
#('actual mean', 1.0242051550438309)
print('biased mean', biased_pmf.Mean())
#('biased mean', 2.4036791006642821)
```
