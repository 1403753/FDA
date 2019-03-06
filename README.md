
**Please note**: You cannot use any external packages or native libraries
*except* where specifically mentioned. Be careful with when importing 
packages!

## Part 1 - Python (30 points)

The first part of this assignment is intended to get you up and running with
Python. We have provided a repository on [gitlab](). Please use the file 
`l1p1.py` in this file to write your code.

In the repository we have also provided some test cases which you can use
to test your code. You'll need to install some packages first though. So set
up a virtual environment for yourself and run `pip install -r requirements.txt`
to install the pacakges you'll need. Then you can run one of the tests like
so:

```
./test_assignment.sh
```

### Question 1 (10 points)

Write a function to sort a list of integers. You can write any algorithm you
want including, quicksort, merge sort, bubble sort, or random sort. However,
you need to write the code yourself. Python and numpy both provide library
methods for sorting lists but you cannot use them. 

Here are some examples:
```
>>> sort_list([1,2,3])
[1,2,3]
>>> sort_list([5,4,3,2])
[2,3,4,5]
```

### Question 2 (10 points)

This question is inspired by one of the divisibility tricks in a recent
[numberphile video](https://www.youtube.com/watch?v=yi-s-TTpLxY&t=178s).
This time we're going to play around with number theory. The task here is to
write a function that, given an integer and a single integer digit, returns
an integer that inserts the digit in the integer such that the new integer is
divisible by 7. The digits of the original integer must remain in the same
order. If this is not possible then the function should throw an exception
with message "not possible"

Examples:

```
>>> div7(123, 4)
4123
>>> div7(39, 2)

```

Examples of incorrect output:

```
# not divisible by 7
>>> div7(123,4)
1234

# cannot reorder digits in first argument
>>> div7(124, 3)
4123
```

### Question 3 (10 points)

Note the import of numpy within the function. Don't alter this line, you can
only use numpy in this particular function. Here the task is to extend the
cubic function $y = a_1 x^3 + a_2 x^2 + a_3 x + a_4$ to handle multi-variate
arguments. In other words, rather than having a scalar $x$ and a vector of
coefficients, $a$. You will now have a vector of inputs for $x$ and a matrix
of coefficients, $a$. Each column of $a$ is the coefficients for the $i$th
element of the vector $x$. This function should still return a scalar value.

Examples:

```
>>> cubic(np.array([1,2,3,4]), np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
???
```

## Part 2 - Regression analysis (70 points)

For this part we’re going to explore which factors contribute to the happiness
score (the column called "happiness_score") for various countries (csv file).
The idea is to predict the happiness score based on 13 factors. For these parts
submit a single file of your python code called l1p2.ipynb. Please clearly
comment the file so we can understand which parts of the code are associated
with which project. For the writeup, also submit a pdf called l1p2.pdf. The
Jupyter notebook file should produce this pdf. See below for directions on how
to do this. It is your responsibility to ensure that this can be run on the
grader's computer. We will use a python distribution set up with scikit-learn,
numpy, pandas, and matplotlib.

### Q2.1 (20 points)

First we want to get an overview of the data. Write a report that contains the
following parts:

1. Use matplotlib to make a scatterplot of each variable against the 
   happiness score.
2. Explain the trends you see in each of the plots. Explain if you see any 
   trend and what kind of trend you see (linear, quadratic, logrithmic, etc). 
   (one sentence for each plot should be sufficient)
3. before doing the later parts of the assignment, explain which factors you 
   think are important for predicting the happiness index and why. (one paragraph)

### Q2.2 (50 points)

Now it’s time to build a model of the data. For this you should use the
[KernelRidge](http://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge)
module from scipy.

For the evaulation report both the $R^2$ value as well as the 5-fold cross
validation results for each model.

1. Check for any missing values in the dataset. Any missing values will cause
   an error when you try to build a model.
2. Come up with a way (and modify the dataset programmatically). **DO NOT
   change the CSV file itself**. It's important to document your work use code
   as much as possible so that your results are reproducable. We will diff the
   csv file submitted against our copy and it cannot differ.
3. Build a linear model and evaluate it (HINT: linear kernel)
4. Build a polynomial model and evaluate it (HINT: polynomial kernel)
5. Build a Gaussian model and evaluate it (HINT: Gaussian/RBF kernel)
6. Compare the 3 different models:
    * which degree of polynomial provided the best fit?
    * which values of gamma and alpha for the fitting procedure gave the 
      best fit?
    * write which model is the best fit to the data and why 
      (1 paragraph will be sufficient)

### Converting a Jupyter notebook to pdf

Jupyter comes with a function called [nbconvert]() that can convert Juyter
notebooks to a variety of formats. To convert your notebook to pdf you'll also
need LaTeX and [pandoc](https://pandoc.org/) installed. Once you've done this
you can convert the notebook from the command line:

```
>>> jupyter nbconvert --to pdf l1p2.ipynb
```

### Procedure and Submission

Please submit a ZIP-document with your answers to [Moodle](). Use the following
naming scheme for your submission: “lastname_matrikelnumber_A1.zip”. The naming
of the files is important. If you do not follow the submission instructions,
then you will receive a grade of 0 for the lab.

### Late submission

Late Submissions are NOT possible. Any assignment submitted late will receive zero points.

[Academic Honesty](http://vda.univie.ac.at/Teaching/FDA/19s/academicHonesty.html)

