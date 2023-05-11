#Write your code below this line 👇

# def prime_checker(number):
#     no = 0
#     for i in range(2, number - 1):
#         if number % i == 0:
#             no += 1
                
#     if no == 0:
#         print('It\'s a prime number')
#     else:
#         print('It\'s not a prime number.')



# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '-', '\'', '_', '/', '@', '#', '&', '$', '(', ')', '[', ']', '{', '}', '.', '!', ',', '?', ':', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '-', '\'', '_', '/', '@', '#', '&', '$', '(', ')', '[', ']', '{', '}', '.', '!', ',', '?', ':']


for i in range(1, len(alphabet)):
    print(f'{i + len(alphabet)} % {len(alphabet)} = {(i + len(alphabet)) % len(alphabet)}')