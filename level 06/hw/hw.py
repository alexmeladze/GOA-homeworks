# for i in range(1, 20):
#     print(i)


# for i in range(0, 50, 2):
#     print(i)


# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print(total)



# i = 10

# while i >= 1:
#     print(i)
#     i -= 1


# password = "python123"

# while password != "python123":
#     password = input("Enter password: ")

# print("Access granted")



# number = int(input("Enter a number: "))
# count = 0

# if number < 0:
#     number = -number

# while number > 0:
#     number = number // 10
#     count = count + 1

# print(count)




# n = int(input("Enter a number: "))
# result = 1

# for i in range(1, n + 1):
#     result = result * i

# print(result)



# word = input("Enter a word: ")

# for letter in word:
#     print(letter)






# total = 0
# count = 0

# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     total = total + number
#     count = count + 1

# if count > 0:
#     print(total / count)
# else:
#     print(0)






number = 7
guess = 0

while guess != number:
    guess = int(input("Guess: "))
    if guess != number:
        print("Try again")

print("You guessed it!")