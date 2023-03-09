


kk = []


class matrix:
    def __init__(self, *args):
        if len(args) == 1:
        	if not isinstance(matrix, (list)):
                raise notValidInput("Invalid matrix input")
            matrix = args[0]
            self.check_data(matrix)
            self.data = self.build_mat(matrix)
        elif len(args) == 2:
        	if not isinstance(matrix, (tuple)):
                raise notValidInput("Invalid matrix input")
            rows, cols = args
            self.data = self.build_empty_mat(rows, cols)
        else:
            raise notValidInput("Invalid matrix input")

        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def check_data(self, matrix):
        if not all(isinstance(row, (list)) for row in matrix):
            raise notValidInput("Invalid matrix input")

    def build_mat(self, matrix):
        return [list(row) for row in matrix]

    def build_empty_mat(self, rows, cols):
        return [[None] * cols for noting in range(rows)]

	class notValidInput(Exception):
	    pass

    ###########################operations###########################

