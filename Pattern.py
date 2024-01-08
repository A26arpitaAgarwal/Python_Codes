rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
# * 

# * * 

# * * * 

# * * * * 

# * * * * * 

# * * * * * * 

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

# 1 

# 1 2 

# 1 2 3 

# 1 2 3 4 


rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("\n")
# A 

# B B 

# C C C 

# D D D D 

# E E E E E 


rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()
    #         * 
    #       * * * 
    #     * * * * * 
    #   * * * * * * * 
    # * * * * * * * * * 


rows = int(input("Enter number of rows: "))
k = 1
for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            k = 1
        else:
            k = k * (i - j)//j
        print(k, end = " ")
    print()
# Enter number of rows: 8
#        1 
#       1 1 
#      1 2 1 
#     1 3 3 1 
#    1 4 6 4 1 
#   1 5 10 10 5 1 
#  1 6 15 20 15 6 1 
# 1 7 21 35 35 21 7 1 

rows = int(input("Enter number of rows: "))
k = 0
count=0
count1=0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

# Enter number of rows: 5
#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 
