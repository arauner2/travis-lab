import some_functions

def test_add_two_numbers():
	assert some_functions.add_two_numbers(1,2) == 3

def test_multiply_two_numbers():
	assert some_functions.multiply_two_numbers(0,3) == 0

def test_divide_first_by_second_is_None():
	assert some_functions.divide_first_by_second(9,0) is None

def test_divide_first_by_second():
	assert some_functions.divide_first_by_second(9,3) == 3
