"""
pattern 2
   *
  **
 ***
****
"""
row = 4
col = 4
for i in range(row):
    for j in range(row - i - 1):
        print(end=" ")
    for k in range(i + 1):
        print("*", end="")
    print()

