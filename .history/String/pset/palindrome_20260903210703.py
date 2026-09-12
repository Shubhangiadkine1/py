# text = input("Enter a number or word")
# if text == text[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")


# a = "12321"
# if a == a[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
count = 0
for num in range(1,101):
    if str(num) == str(num)[::-1]:
        print(num)
        count +=1
    print(count)
