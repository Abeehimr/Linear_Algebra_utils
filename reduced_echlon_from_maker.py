
def matrix_print(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(f"{mat[i][j]:8.3f}",end="")
        print()

def switch(mat , a , b):
    mat[a] , mat[b] = mat[b] , mat[a]
    print(f"R{a+1}<-->R{b+1}\n")

def multiply(mat,row,factor):
    mat[row] = [ i*factor for i in mat[row]]
    print(f"{factor:8.3f} x R{row+1}\n")

def add(mat,a , b , factor):
    mat[a] = [mat[a][i] + mat[b][i]*factor for i in range(len(mat[0]))]
    print(f"R{a+1} + {factor:8.3f} x R{b+1}\n")


def non_zero_row(mat,row,col,rows):
    for i in range(row+1,rows):
        if mat[i][col] != 0:
            return i
    return -1

def solve(mat):
    print("\n\n")
    rows , cols = len(mat) , len(mat[0])
    i,j = 0,0
    while (j < cols and i < rows):
        # make it 1 or move on if we cannot
        if mat[i][j] == 0:
            replce = non_zero_row(mat,i,j,rows)
            if replce == -1:
                j+= 1
                continue
            else:
                switch(mat,i,replce)
                matrix_print(mat)
                print("\n\n")
        if mat[i][j] != 1:
            multiply(mat,i, 1/mat[i][j])
            matrix_print(mat)
            print("\n\n")
        #make 0 up and down
        for x in range(rows):
            if mat[x][j] != 0 and x != i:
                add(mat,x,i,-mat[x][j])
        j += 1
        i += 1
        matrix_print(mat)
        print("\n\n")



def main():
    rows = int(input("enter no of rows:\n"))
    cols = int(input("enter no of columns:\n"))
    matrix = []
    for _ in range(rows):
        while True:
            l = input("enter whole row (space separated):\n").strip().split()
            if len(l) == cols:
                break
            print("the no fo columns did not match the specified length")
        matrix.append(list(map(float,l)))


    solve(matrix)
if __name__ == "__main__": main()