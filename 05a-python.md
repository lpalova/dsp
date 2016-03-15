# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Both lists and tuples are sequences of values; e.g. animals_list = ['bat', 'cat', 'rat'], animals_tuple = ('bat', 'cat', 'rat').   
Lists are mutable, that is, you can change values of a list. For example, animals_list[2] = 'mouse' assigns a new value for the 2nd element of the list. The result is an updated animals_list = ['bat', 'cat', 'mouse'].    
Tuples are immutable, that is, you cannot change values of a tuple. Assignment animals_tuple[2] = 'mouse' would not work and python would throw an error message, such as: TypeError: 'tuple' object does not support item assignment.   
Because tuples are immutable, they can be used as keys in dictionaries. Keys in dictionaries must be an immutable type like string, tuple.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

List is an ordered collection of values. Set is an unordered collection of unique elements. Both lists and sets could be viewed as collections of elements. The difference is that a list is an ordered collection (could be accessed via its ith element, animals_list[i]), while a set is an unordered collection (you could add or remove elements, but you cannot access elements via an index = there is no order). That said, the user has precise control over where in the list each element is inserted. For example, animals_list[2] = "mouse". The same is not true for a set. The user can add or remove elements in a list or a set:     
animals_list = ["bat", "cat", "rat"], animals_list.append("mouse"), animals_list.remove("mouse")    
animals_set = {"bat", "cat", "rat"}, animals_set.add("mouse"), animals_set.remove("mouse")     
The implementation of a list is either an ArrayList or a LinkedList. The implementation of an unordered set is either a HashSet or a TreeSet. Therefore finding an element in a set is typically faster than finding an element in a list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda". It is often used in conjunction with typical functional concepts like filter(), map() and reduce(). This piece of code shows the difference between a normal function definition ("f") and a lambda function ("g"):   
>>> def f (x): return x**2   
>>> print f(8)    
64    
>>> g = lambda x: x**2    
>>> print g(8)    
64   
Note that the lambda definition does not include a "return" statement -- it always contains an expression which is returned. Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all.   
*Examples - filter, map, reduce:*   
>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]      
>>> print filter(lambda x: x % 3 == 0, foo)    
[18, 9, 24, 12, 27]   
>>> print map(lambda x: x * 2 + 10, foo)    
[14, 46, 28, 54, 44, 58, 26, 34, 64]   
>>> print reduce(lambda x, y: x + y, foo)     
139    
In the first example, filter() calls our lambda function for each element of the list, and returns a new list that contains only those elements for which the function returned "True". In this case, we get a list of all elements that are multiples of 3. The expression x % 3 == 0 computes the remainder of x divided by 3 and compares the result with 0 (which is true if x is evenly divisible by 3).     
In the second example, map() is used to convert our list. The given function is called for every element in the original list, and a new list is created which contains the return values from our lambda function. In this case, it computes 2 * x + 10 for every element.   
Finally, reduce() is somewhat special. The "worker function" for this one must accept two arguments (we've called them x and y here), not just one. The function is called with the first two elements from the list, then with the result of that call and the third element, and so on, until all of the list elements have been handled. This means that our function is called n-1 times if the list contains n elements. The return value of the last call is the result of the reduce() construct. In the above example, it simply adds the arguments, so we get the sum of all elements. (Note: since Python 2.3 there's a built-in function sum()that does the same thing more efficiently.)    
Cited from: http://www.secnetix.de/olli/Python/lambda_functions.hawk    
*Example - sorted:*
student_tuples = [   
        ('john', 'A', 15),   
        ('jane', 'B', 12),   
        ('dave', 'B', 10),   
]   
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age    
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]   
Cited from: https://wiki.python.org/moin/HowTo/Sorting

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





