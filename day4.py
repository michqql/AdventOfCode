puzzle = list()

with open('input_day4.txt', 'r') as file:
    for line in file:
        char_array = [char for char in line if char in 'XMAS']
        puzzle.append(char_array)
        
# Part 2
def CheckMAS(x, y):
    if puzzle[x][y] == 'A':
        tr_to_bl = (puzzle[x+1][y+1] == 'S' and puzzle[x-1][y-1] == 'M') or (puzzle[x+1][y+1] == 'M' and puzzle[x-1][y-1] == 'S')
        br_to_tl = (puzzle[x-1][y+1] == 'S' and puzzle[x+1][y-1] == 'M') or (puzzle[x-1][y+1] == 'M' and puzzle[x+1][y-1] == 'S')
        return tr_to_bl and br_to_tl
    
mas_occurance = 0

# Loop through the 2d array puzzle, and check for MAS
for i in range(1, len(puzzle) - 1):
    for j in range(1, len(puzzle[0]) - 1):
        if CheckMAS(i, j):
            mas_occurance += 1

print(mas_occurance)


# Part 1
# def CheckXMAS(x, y):
#     # Check in all directions, from x and y within the 2d array puzzle,
#     # to match for the string XMAS
#     xmas_count = 0
#     if puzzle[x][y] == 'X':
#         if x + 3 < len(puzzle) and puzzle[x+1][y] == 'M' and puzzle[x+2][y] == 'A' and puzzle[x+3][y] == 'S':
#             xmas_count += 1
#         if x - 3 >= 0 and puzzle[x-1][y] == 'M' and puzzle[x-2][y] == 'A' and puzzle[x-3][y] == 'S':
#             xmas_count += 1
#         if y + 3 < len(puzzle[0]) and puzzle[x][y+1] == 'M' and puzzle[x][y+2] == 'A' and puzzle[x][y+3] == 'S':
#             xmas_count += 1
#         if y - 3 >= 0 and puzzle[x][y-1] == 'M' and puzzle[x][y-2] == 'A' and puzzle[x][y-3] == 'S':
#             xmas_count += 1
#         if x + 3 < len(puzzle) and y + 3 < len(puzzle[0]) and puzzle[x+1][y+1] == 'M' and puzzle[x+2][y+2] == 'A' and puzzle[x+3][y+3] == 'S':
#             xmas_count += 1
#         if x - 3 >= 0 and y - 3 >= 0 and puzzle[x-1][y-1] == 'M' and puzzle[x-2][y-2] == 'A' and puzzle[x-3][y-3] == 'S':
#             xmas_count += 1
#         if x + 3 < len(puzzle) and y - 3 >= 0 and puzzle[x+1][y-1] == 'M' and puzzle[x+2][y-2] == 'A' and puzzle[x+3][y-3] == 'S':
#             xmas_count += 1
#         if x - 3 >= 0 and y + 3 < len(puzzle[0]) and puzzle[x-1][y+1] == 'M' and puzzle[x-2][y+2] == 'A' and puzzle[x-3][y+3] == 'S':
#             xmas_count += 1

#     return xmas_count

# xmas_occurance = 0

# # Loop through the 2d array puzzle, and check for XMAS
# for i in range(len(puzzle)):
#     for j in range(len(puzzle[0])):
#         xmas_occurance += CheckXMAS(i, j)

# print(xmas_occurance)