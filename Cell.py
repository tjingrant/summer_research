class Cell(object):
	_a_in = 0
	_b_in = 0
	_c_in = 0
	_a_out = 0
	_b_out = 0
	_c_out = 0

	def __init__(self, a_in=0, b_in=0, c_in=0, a_out=0, b_out=0, c_out=0):
		self._a_in = a_in
		self._b_in = b_in
		self._c_in = c_in
		self._a_out = a_out
		self._b_out = b_out
		self._c_out = c_out