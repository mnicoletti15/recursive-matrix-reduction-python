import copy
##Matrices are represented by lists of lists: eg. [[1, 3], [1, 5]]
# 							is the matrix | 1  3 |
##										  | 1  5 |	
#


def get_index(A, i, j):
	return A[i-1][j-1]

def get_row(A, i):
	return A[i-1]

def get_col(A, j):
	B = []
	for row in A:
		B.append(row[j-1])
	return B

#returns A except deletes the first row and column
def Xij(A):
	B = []
	for row in A:
		B.append(row[1:])
	B.pop(0)
	return B

#returns A except without first column
def Xj(A):
	B = []
	for row in A:
		B.append(row[1:])
	return B

def row_swap(A, i1, i2):
	B = copy.deepcopy(A)
	B[i1-1] = get_row(A, i2)
	B[i2-1] = get_row(A, i1)
	return B


def swap_lead_zero(A):
	for i in range(2, len(A)):
		if get_index(A, i, 1) !=0:
			return echelon_form(row_swap(A, 1, i))
	return recursive_call2(A)


def recursive_call1(A):
	B = copy.deepcopy(A)
	C = Xij(A)
	U = echelon_form(C)
	U.insert(0, get_row(B, 1))
	for i in range(2, len(B)+1):
		U[i-1].insert(0, get_index(B, i, 1))
	return U


def recursive_call2(A):
	l = len(A)
	C = Xj(A)
	U = echelon_form(C)
	for i in range(l):
		U[i].insert(0, 0)
	return U

#a vector is a list

def add_vectors(a, b):
	c = []
	for i in range(len(a)):
		c.append(a[i]+b[i])
	return c

def mul_vector(c, a):
	return [c*i for i in a]

def delete_down(A):
	B = copy.deepcopy(A)
	for i in range(2, len(B)+1):
		if get_index(B, i, 0) != 0:
			mult = -get_index(B, i, 1)/get_index(B, 1, 1)
			B[i-1] = add_vectors(B[i-1], mul_vector(mult, B[0]))
	return B


def echelon_form(A):
	if len(A[0]) ==1 or len(A) == 1:
		return A
	else:
		if get_index(A, 1, 1) == 0:
			return swap_lead_zero(A)
		else:
			return recursive_call1(delete_down(A))


def is_leading_entry(A, i, j):
	row = get_row(A, i)
	col = get_col(A, j)
	if get_index(A, i, j)==0:
		return False
	for item in row[:j-1]:
		if item != 0:
			return False
	for item in col[i:]:
		if item != 0:
			return False
	return True



def rref(A):
	C = echelon_form(A)
	B = copy.deepcopy(C)
	for i in range(1, len(B)+1)[::-1]:
		for j in range(1, len(get_row(B, 1))+1)[::-1]:
			if is_leading_entry(C, i, j):
				B[i-1] = mul_vector(1/get_index(B, i, j), B[i-1])
				for q in range(1, i):
					mult = -get_index(B, q, j)
					v = mul_vector(mult, get_row(B, i))
					B[q-1] = add_vectors(v, B[q-1])
	return B



def print_matrix(A):
	for row in A:
		print(row)


A = [[-1, 0, -1, 4, 12, 30],\
     [4, -1, 0, -1, 10, 30],\
     [0, -1, 4, -1, 9, 70],\
     [-1, 4, -1, 0, 9, 60],\
     [1, -2, -3, 4, 5, 23]]
B = rref(A)
print_matrix(B)










