
class matrix:
	
	##############################exceptions#####################################

	class notValidInput(Exception):
		pass

	#############################Constructor#####################################

	def __init__(self, matrix):
		try:
			if len(matrix) != 1:
				if isinstance(matrix, (list)):
					self.check_data(matrix)
					self.data = self.build_mat(matrix)
					self.n_rows = len(self.data)
					self.n_cols = len(self.data[0])
				elif isinstance(matrix, (tuple)):
					self.n_rows, self.n_cols = matrix
					self.data = self.build_empty_mat(self.n_rows, self.n_cols)
				else:
					raise self.notValidInput("Invalid data input")
				self.shape = (self.n_rows, self.n_cols)
			else:
				raise self.notValidInput("Invalid matrix input too many arguments")
		except Exception as e:
			raise self.notValidInput("Invalid matrix input") from e



	def check_data(self, matrix):
		if not all(isinstance(row, (list)) and len(matrix[0]) == len(row)  for row in matrix):
			raise self.notValidInput("Invalid matrix input, or not quadratic")
		if not all(isinstance(val, (int, float)) for row in matrix for val in row):
			raise self.notValidInput("Not int intput one element not int")

	def build_mat(self, matrix):
		return [list(float(val) for val in row) for row in matrix]

	def build_empty_mat(self, n_rows, n_cols):
		return [[0] * n_cols for nothing in range(n_rows)]

	###########################Operations Methods##################################

	def addMat(left, right):
		result = matrix(left.data)
		for y in range(left.n_rows):
			for x in range(left.n_cols):
				result.data[y][x] += right[y][x]
		return result

	def subMat(left, right):
		result = matrix(left.data)
		for y in range(left.n_rows):
			for x in range(left.n_cols):
				result.data[y][x] -= right[y][x]
		return result

	def divMat(self, scalar):
		data = [[val / scalar for val in row] for row in self.data]
		return matrix(data)

	def multMat(self, right):
		if isinstance(right, list):
			e_mat = matrix(tuple([self.n_rows, len(right[0])]))
			for y, row in enumerate(right):
				e_mat.data[y] = [sum([self.data[y][k] * row[k] for k in range(self.n_cols)]) for x in range(len(right[0]))]
		elif isinstance(right, float):
			e_mat = matrix(tuple([self.n_rows, self.n_cols]))
			for y, row in enumerate(self.data):
				e_mat.data[y] = [self.data[y][x] * right for x in range(self.n_cols)]
			return e_mat	
		return e_mat

	##############################utils##################################

	def announce(self):
		for row in self.data:
			print(row)
		print(f"Matrix shape: {self.n_rows} x {self.n_cols}")

	def T(self):
		t_mat = [[ self.data[x][y]for x in range(self.n_rows)] for y in range(self.n_cols)]
		return matrix(t_mat)

	########################operator_overload###########################

	def __add__(self, right):
		if self.n_rows != right.n_rows or self.n_cols != right.n_cols:
			raise self.notValidInput("matrix not equal shape, sum not valid")
		var = self.addMat(right.data)
		return var

	def __radd__(self, right):
		if self.n_rows != right.n_rows or self.n_cols != right.n_cols:
			raise self.notValidInput("matrix not equal shape, sum not valid")
		var = self.addMat(right.data)
		return var

	def __sub__(self, right):
		if self.n_rows != right.n_rows or self.n_cols != right.n_cols:
			raise self.notValidInput("matrix not equal shape, sub not valid")
		var = self.subMat(right.data)
		return var

	def __rsub__(self, right):
		if self.n_rows != right.n_rows or self.n_cols != right.n_cols:
			raise self.notValidInput("matrix not equal shape, sub not valid")
		var = self.subMat(right.data)
		return var

	def __truediv__(self, scalar):
		if isinstance(scalar, matrix):
			if scalar.shape == (1, 1) and scalar.data[0][0] != 0:
				var = self.divMat(scalar.data[0][0])
			else:
				raise self.notValidInput("Illegal div by 0 or not scalar 'matix'")
		elif isinstance(scalar, (int, float)) and scalar == 0:
			raise self.notValidInput("Illegal div by 0")
		elif isinstance(scalar, (int, float)):
				var = self.divMat(float(scalar))
		else:
			raise self.notValidInput("Not valid input for div")
		return var

	def __rtruediv__(self, other):
		if isinstance(other, (matrix)):
			raise notValidInput("Can only divide matrix by matrix")
		inv_other = np.linalg.inv(other.data)
		result = np.matmul(self.data, inv_other)
		return matrix(result)


	def __mul__(self, other):
		if isinstance(other, matrix):
			if self.n_cols != other.n_rows:
				raise ValueError(f"Invalid matrix product: cannot multiply a {self.n_rows}x{self.n_cols} matrix with a {other.n_rows}x{other.n_cols} matrix")
			result = self.multMat(other.data)
		elif isinstance(other, (float, int)):
			result = self.multMat(float(other))
		return result

	def __rmul__(self, other):
		if isinstance(other, matrix):
			if other.n_cols != self.n_rows:
				raise ValueError(f"Invalid matrix product: cannot multiply a {other.n_rows}x{other.n_cols} matrix with a {self.n_rows}x{self.n_cols} matrix")
			result = other.multMat(self.data)
		elif isinstance(other, (float, int)):
			result = self.multMat(float(other))
		return result

	def __str__(self):
		output = ""
		for row in self.data:
			for value in row:
				output += "{:10.4f}".format(value)
			output += "\n"
		return output

	def __repr__(self):
		matrix_repr = '['
		for row in self.data:
			matrix_repr += '[' + ', '.join(str(val) for val in row) + '], '
		matrix_repr = matrix_repr.rstrip(', ') + ']'
		return f'Matrix({matrix_repr})'


	###############################################################################

if __name__ == "__main__":
	try:
		m = matrix([[1, 1], [3, 4]])	
		m.announce()
		o = matrix((2, 3))
		o.announce()
		l = matrix([[2, 4], [5, 8]])
		l.announce()
		s = l + m
		s.announce()
		n = s - l
		n.announce()
		p = n * 3
		print(p)
		pt = matrix([[0, 2, 4],[1, 3, 5]])
		print(pt)
		print(pt.T())
	except (matrix.notValidInput) as out:
		print (out)
	
	
