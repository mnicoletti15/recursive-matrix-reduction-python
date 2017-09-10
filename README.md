# recursive-matrix-reduction-python
algorithm that takes a matrix and row returns a row-recuced matrix.
My implementation of a matrix in python was simply a list of lists, where each sublist represents a row in the matrix.
The basic steps followed by the algorithm are as follows:
If the top left entry is 0, find a row with a nonzero entry in the first column and swap that row with the first row. If the first column has only zeros, then move to the right until a nonzero column is reached.
Then, by adding a multiple of the first row to the others, make all of the entries below the top leading entry 0. After this, repeat the process on the matrix obtained by deleting the first row and column of the current matrix.
If the matrix is reduced to either a single column or a single row, return the same matrix.
This project is not fully functional and has no UI at the moment.
