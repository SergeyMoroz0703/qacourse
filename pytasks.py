# 1. Define a function, that takes string as argument and prints "Heelo, %arg%!"

# def greet(name):
#     if len(name) > 0 and type(name) == str:
#         print('Hello {}!'.format(name))
# greet('Mentor')

#2.Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list
#  of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

# def sum(list):
#     summa = 0
#     try:
#         for i in list:
#             summa = summa + i
#         print(summa)
#         return summa
#     except TypeError:
#         print('Just digit should be in list')
#
# def multiply(list):
#     mult = 1
#     for i in list:
#         if i == 0:
#             print (i)
#             return i
#         else:
#             mult = mult * i
#     print(mult)
#     return mult
#
# sum([1,2,3,4])
# multiply([1,2,3,4])


#3.Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return
# the string "gnitset ma I".

# def reverse(data):
#     i=1
#     checklist = []
#     try:
#         while i <= len(data):
#             symbol = data[len(data)-i]
#             checklist.append(symbol)
#             i=i+1
#         print(''.join(checklist))
#     except TypeError as e:
#         print('Error: {}! \nShould be the string inside!'.format(e))
#
# reverse('gay')
