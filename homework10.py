def get_matrix(n, m, value):
    matrix = []
    for a in range(n):
        s = []
        matrix.append(s)
        for b in range(m):
            s.append(value)
    return matrix


print(get_matrix(5, 4, 12))
