from __future__ import annotations
from sys import stderr

class Matrix():
	def __init__ (self, *mat):
		if len(mat) != 1:
			raise ValueError("Mutiple mat no code dude")
		self.checking_data(*mat)
		self.shape = self.getshape(*mat)
		self.mat = self.geteverything(*mat)

######################################Basic_Structure####################################################

	def getshape(self, nums):
		if isinstance(nums, list):
			n_line, n_col = len(nums), len(nums[0])
			return(n_line, n_col)
		else:
			size = nums
			return(size)

	def geteverything(self, nums):
		if isinstance(nums, list):
			tmp = nums.copy()
		else:
			len_r, len_c = nums[0], nums[1]
			tmp = []
			[tmp.append([0] * len_r) for y in range(len_c)]
		#print(tmp)
		return(tmp)

	def checking_data(self, nums):
		if not isinstance(nums, (tuple, list)):
			raise ValueError("Not good type of mat")
		if isinstance(nums, (tuple)):
			if not isinstance(nums[0], (int, float)) or not isinstance(nums[1], (int, float)):
				raise TypeError("Unexpected type within shape numsument")
		if isinstance(nums, (list)):
			if any([not isinstance(l, list) for l in nums]):
 				raise TypeError("Unexpected type within the data argument.")
			for x in range(0, len(nums)):
				if any([not isinstance(l, (int, float)) for l in nums[x]]):
					raise TypeError("Not number dude")
				if len(nums[x]) != len(nums[0]):
					raise TypeError("Not cuadratic")

########################################################################################################
######################################Operators#########################################################

	def __add__(self, mat2):
		if not isinstance(mat2, Matrix):
			raise OperatorError("Second arg is not Mat")
		if self.shape != mat2.shape:
			raise OperatorError("Different sizes")
		try:
			tmp = Matrix(self.shape)
			for x in range(self.shape[0]):
				for y in range(self. shape[1]):
					tmp.mat[x][y] = self.mat[x][y] + mat2.mat[x][y]
			return tmp	
		except:
			raise ArithmeticError("Something happend while adding")

	def __radd__(self, mat2):
		if not isinstance(mat2, Matrix):
			raise OperatorError("Second arg is not Mat")
		if self.shape != mat2.shape:
			raise OperatorError("Different sizes")
		try:
			tmp = Matrix(self.shape)
			for x in range(self.shape[0]):
				for y in range(self. shape[1]):
					tmp.mat[x][y] = self.mat[x][y] + mat2.mat[x][y]
			return tmp	
		except:
			raise ArithmeticError("Something happend while adding")

	def __sub__(self, mat2):
		if not isinstance(mat2, Matrix):
			raise OperatorError("Second arg is not Mat")
		if self.shape != mat2.shape:
			raise OperatorError("Different sizes")
		try:
			tmp = Matrix(self.shape)
			for x in range(self.shape[0]):
				for y in range(self. shape[1]):
					tmp.mat[x][y] = self.mat[x][y] - mat2.mat[x][y]
			return tmp	
		except:
			raise ArithmeticError("Something happend while adding")

	def __rsub__(self, mat2):
		if not isinstance(mat2, Matrix):
			raise OperatorError("Second arg is not Mat")
		if self.shape != mat2.shape:
			raise OperatorError("Different sizes")
		try:
			tmp = Matrix(self.shape)
			for x in range(self.shape[0]):
				for y in range(self. shape[1]):
					tmp.mat[x][y] = self.mat[x][y] - mat2.mat[x][y]
			return tmp	
		except:
			raise ArithmeticError("Something happend while adding")

	def __mul__(self, mat2):
		if not isinstance(mat2, (Matrix, int, float)):
			raise OperatorError("Second arg isnt good")
		try:
			if isinstance(mat2, (int, float)):
				tmp = Matrix(self.shape)
				for x in range(self.shape[0]):
					for y in range(self. shape[1]):
						tmp.mat[x][y] = self.mat[x][y] * mat2
			elif isinstance(mat2, Matrix):
				if self.shape[0] == mat2.shape[1]:
					tmp = Matrix((self.shape[0], mat2.shape[1]))
					for x in range(self.shape[0]):
						for y in range(mat2.shape[0]):
							for z in range(self.shape[1]):
								tmp.mat[x][y] += self.mat[x][z] * mat2.mat[z][y]
				else:
					raise ArithmeticError("Not posible multiplication")
			return tmp
		except:
			raise ArithmeticError("Something happend while multiplicating")

	def __truediv__(self, mat2):
		if isinstance(mat2, (Matrix)):
			raise OperatorError("There are non right ways to do this")
			try:
				if(mat2.shape == (1, 1)):
					tmp = Matrix(self.shape)
					for x in range(self.shape[0]):
						for y in range(self.shape[1]):
							tmp.mat[x][y] = self.mat[x][y] / mat2.mat[0][0]
					return tmp
			except:
				raise ArithmeticError("Something happend while trying to div")
		if isinstance(mat2, (int, float)) and mat2 == 0:
			raise ZeroDivisionError("This is a bad idea to divide by 0.")
		elif isinstance(mat2, (int, float)):
			try:
				tmp = Matrix(self.shape)
				for x in range(self.shape[0]):
					for y in range(self.shape[1]):
						tmp.mat[x][y] = self.mat[x][y] / mat2
				return tmp
			except:
				raise ArithmeticError("Something happend while trying to div")




######################################Tests##############################################################


mat = Matrix([[1, 1, 1],[0, 1, 0],[0, 1, 0]])
mat2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

mat3 = mat / 2
print(mat3.mat)


