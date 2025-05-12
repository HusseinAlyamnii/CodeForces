t = int(input())
for _ in range(t):
    position = input().strip()
    col = position[0]
    row = position[1]
    
    # Generate all squares in the same column, different rows
    for r in '12345678':
        if r != row:
            print(f"{col}{r}")
    
    # Generate all squares in the same row, different columns
    for c in 'abcdefgh':
        if c != col:
            print(f"{c}{row}")
