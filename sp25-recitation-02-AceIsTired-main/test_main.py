from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 5, 2) == 1500
	assert simple_work_calc(50, 6, 2) == 4500
	assert simple_work_calc(60, 7, 2) == 12600

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(40, 4, 2, lambda n: n) == 1600
	assert work_calc(50, 5, 2, lambda n: n) == 31250
	assert work_calc(60, 6, 2, lambda n: n) == 129600


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	def work_fn1(n):
		return work_calc(n, 2, 2, lambda n: n**1)

	# create work_fn2
	def work_fn2(n):
		return work_calc(n, 2, 2, lambda n: n**2)

	print(compare_work(work_fn1, work_fn2))


def test_compare_span():

	span1 = lambda n: span_calc(n, 2, 2, lambda n: n**1)

	span2 = lambda n: span_calc(n, 2, 2, lambda n: n**2)

	print(compare_span(span1, span2))