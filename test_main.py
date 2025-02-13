from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	# 3 more cases
	assert simple_work_calc(40, 2, 2) == 224
	assert simple_work_calc(50, 2, 2) == 276
	assert simple_work_calc(60, 3, 2) == 960

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	# 3 more cases
	assert work_calc(40, 4, 2, lambda n: n) == 1600
	assert work_calc(50, 5, 2, lambda n: n) == 31250
	assert work_calc(60, 6, 2, lambda n: n) == 129600


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	test1 = lambda n: work_calc(n, 2, 2, lambda n: n**.5)

	# create work_fn2
	test2 = lambda n: work_calc(n, 2, 2, lambda n: n)

	# 3rd test for question 4
	test3 = lambda n: work_calc(n, 2, 2, lambda n: n**2)

	t1 = compare_work(test1, test2)
	t2 = compare_work(test2, test3)

	print("Comparing c < log_b a vs. c = log_b a")
	print_results(t1)
	print("Comparing c = log_b a vs. c > log_b a")
	print_results(t2)

	# It was VERY hard to figure out why things werent working properly, if these could be
	#included in the next lab handout, it would be much appreciated.
	assert t1 is not None
	assert t2 is not None


def test_compare_span():

	span1 = lambda n: span_calc(n, 2, 2, lambda n: math.log(n))

	span2 = lambda n: span_calc(n, 2, 2, lambda n: n)

	span3 = lambda n: span_calc(n, 2, 2, lambda n: 1)

	c1 = compare_span(span1, span2)
	c2 = compare_span(span2, span3)

	print("Comparing Log^2 vs Log")
	print_results(c1)
	print("Comparing Log vs Linear")
	print_results(c2)

	assert c1 is not None
	assert c2 is not None