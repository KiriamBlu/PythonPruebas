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
		size = []
		if isinstance(nums, list):
			size.append(len(nums)), size.append(len(nums[0]))   
		else:
			size = nums
		print(size)
		return(size)

	def geteverything(self, nums):
		if isinstance(nums, list):
			tmp = nums.copy()
		else:
			len_r, len_c = nums[0], nums[1]
			tmp = []
			[tmp.append([0] * len_r) for y in range(len_c)]
		print(tmp)
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

##################################################################################################
mat = Matrix([[1, 1, 1],[0, 1, 0],[0, 1, 0]])