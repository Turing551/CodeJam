import sys

T = int(input())  # read a line with a single integer

def dive_into(matrix, r, c, visited, sol_so_far, cur_step, R, C):
    # print('visiting ', r, c)

    matrix[r][c] = cur_step
    sol_so_far.append((r,c))

    visited.append((r,c))
    if len(visited) == R * C:
        return True


    for next_r in range(0, R):
        for next_c in range(0, C):
            if (next_r,next_c) in visited:
                continue
            if next_r == r:
                continue
            if next_c == c:
                continue
            if r - c == next_r - next_c:
                continue
            if r + c == next_r + next_c:
                continue
            res = dive_into(matrix, next_r, next_c, visited, sol_so_far, cur_step+1, R, C)
            if res:
                return True

    sol_so_far.pop()
    visited.pop()
    return False

for cur_case in range(1, T + 1):
    line = sys.stdin.readline().strip()
    R, C = line.split()
    R = int(R)
    C = int(C)
    # print('R: ', R, ', C: ', C)
    matrix = [[0 for c in range(0, C)] for r in range(0, R)]
    # print(matrix)
    sol_so_far = []
    visited = []
    cur_step = 1
    # can only search 1/4 area
    res = False
    for r in range(0, R):
        if res:
            break
        for c in range(0, C):
            res = dive_into(matrix, r, c, visited, sol_so_far, cur_step, R, C)
            if res:
                break
    # print(sol_so_far)

    if len(sol_so_far) == 0:
        print("Case #%d: %s" % (cur_case, 'IMPOSSIBLE'))
        continue

    print("Case #%d: %s" % (cur_case, 'POSSIBLE'))

    for s in sol_so_far:
        print("%d %d" % (s[0]+1, s[1]+1))
