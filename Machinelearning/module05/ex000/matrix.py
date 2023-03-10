
class matrix:
	
	##############################exceptions#####################################

	class notValidInput(Exception):
		pass

	#############################Constructor#####################################

	def __init__(self, matrix):
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

	def multMat(self, matrix):
		data = [[ self.data[y][x] + row[x] for x in range(self.n_cols)]  for row, y  in matrix]
		return matrix(data)

	##############################utils##################################

	def announce(self):
		for row in self.data:
			print(row)
		print("Matrix shape: {} x {}".format(self.n_rows, self.n_cols))



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
		if (self.n_cols != self.n_rows):
			raise notValidInput("left[m, n] * right[n, q]: Not valid product of matrix")
		var = self.multMat(other.data)
		return var

if __name__ == "__main__":
	try:
		m = matrix([[1, 1], [3, 4]])	
		m.announce()
		o = matrix((3, 3))
		o.announce()
		l = matrix([[2, 4], [5, 8]])
		l.announce()
		s = l + m
		s.announce()
		n = s - l
		n.announce()
		p = n * o
		p.announce()
	except (matrix.notValidInput) as out:
		print (out)
	
	
