from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	def work_fn1(n):
		return work_calc(n, 2, 2, lambda n: n**1)

	# create work_fn2
	def work_fn2(n):
		return work_calc(n, 2, 2, lambda n: n**2)

	def work_fn3(n):
		return work_calc(n, 2, 2, lambda n: n**.5)

	res = compare_work(work_fn1, work_fn2)
	print("Comparing: f(n) = n VS f(n) = n^2")
	print_results(res)
	res = compare_work(work_fn2, work_fn3)
	print("Comparing: f(n) = n VS f(n) = n^0.5")
	print_results(res)


def test_compare_span():
	def span_fn1(n):
		return span_calc(n, 2, 2, lambda n: n**1)

	# create work_fn2
	def span_fn2(n):
		return span_calc(n, 2, 2, lambda n: n**2)

	def span_fn3(n):
		return span_calc(n, 2, 2, lambda n: n**math.log(n))

	res = compare_span(span_fn1, span_fn2)
	print("Comparing spans: f(n) = n VS f(n) = n^2")
	print_results(res)

	res = compare_span(span_fn2, span_fn3)
	print("Comparing spans: f(n) = n VS f(n) = log n")
	print_results(res)

	assert True, "All tests passed"