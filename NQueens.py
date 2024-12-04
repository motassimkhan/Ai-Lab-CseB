def N_Queen(N):
    col = set()
    posDiag = set()
    negDiag = set()
    
    res = []
    board = [[" _ "] * N for i in range (N)]
    
    def backtrack(r):
        if r == N:
            copy = [''.join(res) for res in board]
            res.append(copy)
            return copy
        for c in range (N):
            if c in col or (c+r) in posDiag or (c-r) in negDiag:
                continue
            
            col.add(c)
            posDiag.add(c+r)
            negDiag.add(c-r)
            board[r][c] = ' Q '
            
            backtrack(r+1)
            
            col.remove(c)
            posDiag.remove(c+r)
            negDiag.remove(c-r)
            board[r][c] = " _ "
            
    backtrack(0)
    return res

n = int(input("Enter Queen : "))
result = N_Queen(n)
for i in result:
    for j in i:
        print(j)
    print()