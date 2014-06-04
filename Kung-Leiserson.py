from prettytable import PrettyTable
from Cell import Cell

MEM_SQUARE_LEN = 10
BOUNDARY_TO_IGNORE = 1
SCAN_AREA_LEN = MEM_SQUARE_LEN - BOUNDARY_TO_IGNORE

a_matrix = 	[[1, 2, 3],
			 [4, 5, 6],
			 [7, 8, 9]]

a_matrix_p = [[0, 0, 9, 0, 0],
			  [0, 6, 0, 0, 0],
			  [3, 0, 0, 8, 0],
			  [0, 0, 5, 0, 0],
			  [0, 2, 0, 0, 7],
			  [0, 0, 0, 4, 0],
			  [0, 0, 1, 0, 0]]

b_matrix =	[[1, 3, 5],
			 [7, 9, 1],
			 [1, 2, 3]]

b_matrix_p = [[0, 0, 3, 0, 0, 0, 0],
			  [0, 2, 0, 0, 1, 0, 0],
			  [1, 0, 0, 9, 0, 0, 5],
			  [0, 0, 7, 0, 0, 3, 0],
			  [0, 0, 0, 0, 1, 0, 0]]



step = 0

systolic = [[Cell() for _ in range(MEM_SQUARE_LEN)] for _ in range(MEM_SQUARE_LEN)]

def get_systolic_point(i, j):
	if ((i < 0) or (j < 0)):
		return Cell(0, 0, 0, 0, 0, 0)
	if ((i >= MEM_SQUARE_LEN) or (j >= MEM_SQUARE_LEN)):
		return Cell(0, 0, 0, 0, 0, 0)
	else:
		return systolic[i][j]

def print_interesting_square():
	for y in range(5, 10):
		line = ""
		for x in range(5, 10):
			line = line + (str(systolic[x][y]._c_out) + " ")
		print line + "\n"

def print_all_square():
	table = PrettyTable(["", "1","2","3","4","5","6","7","8","9","10"])
	table.padding_width = 1
	for y in range(0, 10):
		line = [y+1]
		for x in range(0, 10):
			line.append(str(systolic[x][y]._c_out) + "|" + str(systolic[x][y]._a_out) + "|" + str(systolic[x][y]._b_out) + " ")
		table.add_row(line)
	print table

for x in range(5, 10):
	for y in range(0, 7):
		systolic[x][y]._a_out = a_matrix_p[y][x-5]

for x in range(0, 7):
	for y in range(5, 10):
		systolic[x][y]._b_out = b_matrix_p[y-5][x]

print_all_square()

while(raw_input("continue?")!="quit"):
	step += 1
	print "step " + str(step)
	systolic_new = [[Cell() for _ in range(MEM_SQUARE_LEN)] for _ in range(MEM_SQUARE_LEN)]
	for x in range(1, 10):
		for y in range(1, 10):
			systolic_new[x][y]._a_in = get_systolic_point(x, y-1)._a_out
			systolic_new[x][y]._b_in = get_systolic_point(x-1, y)._b_out
			systolic_new[x][y]._c_in = get_systolic_point(x+1, y+1)._c_out
			systolic_new[x][y]._a_out = systolic_new[x][y]._a_in
			systolic_new[x][y]._b_out = systolic_new[x][y]._b_in
			systolic_new[x][y]._c_out = systolic_new[x][y]._c_in + systolic[x][y]._a_in * systolic[x][y]._b_in
	#print_interesting_square()
	systolic = systolic_new
	print_all_square()

