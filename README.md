# CMPS 2200  Recitation 02

**Name:** Jamari Ross


In this recitation, we will investigate recurrences.
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [X] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [X] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [X] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [X] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

|     n |   f(n) = 1 |   f(n) = n | f(n) = log n |
|-------|------------|------------|--------------|
|    10 |         15 |         36 |       19.966 |
|    20 |         31 |         92 |       44.253 |
|    50 |         63 |        276 |      107.311 |
|   100 |        127 |        652 |      221.265 |
|  1000 |       1023 |       9120 |     1896.421 |
|  5000 |       8191 |      61728 |    12497.283 |
| 10000 |      16383 |     133456 |    25007.854 |

- [X] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

When $c < \log_b a$, $n^c$ is dominated by $a⋅W(n/b)$ and grows at a rate of O(n^(log_b a)) because $n^c$ doesn't grow as fast as the function's recursive calls. When $c > \log_b a$, $n^c$ dominates and grows at a rate of $O(n^c)$. When they're equal, the terms balance out and grow at a rate of $O(n^clog n)$

Comparing: f(n) = n VS f(n) = n^2
|     n |    W_1 |       W_2 |
|-------|--------|-----------|
|    10 |     36 |       174 |
|    20 |     92 |       748 |
|    50 |    276 |      4790 |
|   100 |    652 |     19580 |
|  1000 |   9120 |   1990744 |
|  5000 |  61728 |  49957880 |
| 10000 | 133456 | 199915760 |

Comparing: f(n) = n VS f(n) = n^0.5
|     n |       W_1 |       W_2 |
|-------|-----------|-----------|
|    10 |       174 |    21.291 |
|    20 |       748 |    47.055 |
|    50 |      4790 |   110.236 |
|   100 |     19580 |   230.472 |
|  1000 |   1990744 |  2075.117 |
|  5000 |  49957880 | 14251.208 |
| 10000 | 199915760 | 28602.416 |
- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should.

**TODO: your answer goes here**
