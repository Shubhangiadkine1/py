# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

# for i in range(3):
#     for j in range(5):
#         print("*",end="")
#     print()


# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
     

n = 5 

for i in range(n):
    for j in range(i):
        if i == 0 or i == n or j == 0 or j == n-1:
            print("*",end="")
        else:
            print(" ", end="")
    print()