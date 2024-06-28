# Linear_Algebra_utils
this repo contains some Linear_Algebra utilities that i needed at some time. 


<details>
  <summary><h1>reduced_echlon_from_maker</h1></summary>
This Python script performs basic matrix row operations and solves a given matrix using Gaussian elimination. The script includes functions to print matrices, switch rows, multiply rows by a scalar, and add rows together. It also includes functionality to find non-zero rows and a main function to take user input and solve the matrix.

## Functions

### `matrix_print(mat)`
Prints the matrix with formatted entries.

### `switch(mat, a, b)`
Switches row `a` and row `b` in the matrix `mat`.

### `multiply(mat, row, factor)`
Multiplies row `row` of the matrix `mat` by a scalar `factor`.

### `add(mat, a, b, factor)`
Adds `factor` times row `b` to row `a` in the matrix `mat`.

### `non_zero_row(mat, row, col, rows)`
Finds the first non-zero row below the current row in a specified column.

### `solve(mat)`
Solves the matrix `mat` using Gaussian elimination, printing each step.

### `main()`
Takes user input for the number of rows and columns, as well as the matrix elements, and solves the matrix.

## Usage

Run the script, and it will prompt for the number of rows and columns of the matrix. Enter the elements of each row, and the script will perform Gaussian elimination, displaying each step of the process.

```python
if __name__ == "__main__":
    main()
```
</details>
