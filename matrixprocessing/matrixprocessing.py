def read_matrix(prompt=""):
    """Чтение матрицы с проверкой ввода"""
    while True:
        try:
            rows, cols = map(int, input(f"Enter size of matrix {prompt}: ").split())
            print(f"Enter matrix {prompt}:")
            matrix = []
            for _ in range(rows):
                row = list(map(float, input().split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
            return matrix
        except (ValueError, IndexError):
            print("Invalid input. Please enter rows and cols as two numbers, then correct matrix elements.")


def print_matrix(matrix):
    """Печать матрицы с округлением"""
    for row in matrix:
        print(' '.join(f"{x:.2f}" for x in row))


def add_matrices(a, b):
    """Сложение матриц"""
    return [[a[i][j] + b[i][j] for j in range(len(a[0])) for i in range(len(a))]


def multiply_scalar(matrix, scalar):
    """Умножение матрицы на скаляр"""
    return [[x * scalar for x in row] for row in matrix]


def multiply_matrices(a, b):
    """Умножение матриц"""
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(matrix, mode):
    """Транспонирование матрицы"""
    if mode == 1:  # Главная диагональ
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif mode == 2:  # Побочная диагональ
        return [[matrix[-j - 1][-i - 1] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif mode == 3:  # Вертикаль
        return [row[::-1] for row in matrix]
    elif mode == 4:  # Горизонталь
        return matrix[::-1]


def determinant(matrix):
    """Вычисление определителя"""
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1) ** j * matrix[0][j] * determinant(
        [row[:j] + row[j + 1:] for row in matrix[1:]])
               for j in range(len(matrix)))


def inverse(matrix):
    """Обратная матрица"""
    det = determinant(matrix)
    if det == 0:
        return None

    n = len(matrix)
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor_row.append((-1) ** (i + j) * determinant(minor))
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
    return [[x / det for x in row] for row in adjugate]


def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by scalar")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        choice = input("Your choice: ").strip()

        if choice == '0':
            break

        try:
            if choice == '1':
                a = read_matrix("A")
                b = read_matrix("B")
                if len(a) != len(b) or len(a[0]) != len(b[0]):
                    print("ERROR: Matrices must have the same dimensions")
                    continue
                print("Result:")
                print_matrix(add_matrices(a, b))

            elif choice == '2':
                matrix = read_matrix()
                scalar = float(input("Enter scalar: "))
                print("Result:")
                print_matrix(multiply_scalar(matrix, scalar))

            elif choice == '3':
                a = read_matrix("A")
                b = read_matrix("B")
                if len(a[0]) != len(b):
                    print("ERROR: Columns of A must match rows of B")
                    continue
                print("Result:")
                print_matrix(multiply_matrices(a, b))

            elif choice == '4':
                print("\n1. Main diagonal")
                print("2. Side diagonal")
                print("3. Vertical")
                print("4. Horizontal")
                mode = int(input("Your choice: "))
                if mode not in (1, 2, 3, 4):
                    print("Invalid choice")
                    continue
                matrix = read_matrix()
                print("Result:")
                print_matrix(transpose(matrix, mode))

            elif choice == '5':
                matrix = read_matrix()
                if len(matrix) != len(matrix[0]):
                    print("ERROR: Matrix must be square")
                    continue
                print(f"Determinant: {determinant(matrix):.2f}")

            elif choice == '6':
                matrix = read_matrix()
                if len(matrix) != len(matrix[0]):
                    print("ERROR: Matrix must be square")
                    continue
                inv = inverse(matrix)
                if inv is None:
                    print("Matrix doesn't have an inverse")
                else:
                    print("Inverse matrix:")
                    print_matrix(inv)

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()