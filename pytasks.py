# 1. Define a function, that takes string as argument and prints "Heelo, %arg%!"

def greet(name):
    if len(name) > 0 and type(name) == str:
        return ('Hello {}!'.format(name))
    else:
        return ('Argument should be a string with len > 0')



#2.Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list
#  of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum(list):
    summa = 0
    try:
        for i in list:
            summa = summa + i
        return summa
    except TypeError:
        return ('Just digit should be in list')

def multiply(list):
    mult = 1
    for i in list:
        if i == 0:
            return i
        else:
            if type(i) != str:
                mult = mult * i
            else:
                return ('Just digit should be in list')

    return mult




#3.Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return
# the string "gnitset ma I".

def reverse(data):
    i=1
    result = []
    try:
        while i <= len(data):
            symbol = data[len(data)-i]
            result.append(symbol)
            i=i+1
        return (''.join(result))
    except TypeError as e:
        return ('Error: {}! \nShould be the string inside!'.format(e))


#4. Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
#  For example, is_palindrome("radar") should return True.

def is_palindrome(data):
    i = 1
    checklist = []
    try:
        while i <= len(data):
            symbol = data[len(data)-i]
            checklist.append(symbol)
            i=i+1
    except TypeError as e:
        return ('Error: {}! \nShould be the string inside!'.format(e))
    unword = ''.join(checklist)
    if data == unword:
        return True
    else:
        return False



# 5. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.

def histogram(data):
    if type(data) == list and len(data) > 0:
        for i in data:
            data[data.index(i)] = i*'*'+'\n'
        a = ''
        for i in data:
            a = a+i
        return a
    else:
        return ('Argument should be a list with len>0')




# 6.Define a function caesar_cipher that takes string and key(number), whuch returns encrypted string

def caesar_cipher(datastring, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alphabet[key:] + alphabet[:key]
    result = ''
    for i in datastring:
        result = result + new_alph[alphabet.index(i)]

    return (result)



# 7.define a function diaginal_reverse() that takes matrix and returns diagonal-reversed one:

#TODO 7 task

#8. Write a function game() number-guessing game, that takes 2 int parameters defining the range.
# Using random.randint(A, B) generate random int from the range.While user input isn't equal that number,
# print "Try again!". If user guess the number, congratulate him and exit. (use raw_input())

# import random
#
#
# def game(start, finish):
#     pc_cohice = random.randint(start, finish)
#     #print(pc_cohice)
#     user_choice = input('Please, enter the digit: ')
#     try:
#         if int(pc_cohice) == int(user_choice):
#             print('You win!')
#         else:
#             print('Fucking shit, you lose. Come back later!')
#     except ValueError:
#         print('Please enter the valid integer number!')
#         game(start,finish)
#
# game (3,7)

#9.Define a function, which takes a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
#Determine whether the generated string is balanced; that is, whether it consists entirely of pairs
#  of opening/closing brackets (in that order), none of which mis-nest.

# def determ(string):
#     a = '['
#     b = ']'
#     num_a = 0
#     num_b = 0
#     for i in string:
#         if i == a:
#             num_a = num_a+1
#         else:
#             num_b = num_b+1
#
#     counter = 0
#     if string[0] == a and string[len(string) - 1] == b and num_a == num_b:
#         for i in string:
#             if i == a:
#                 counter = counter + 1
#             else:
#                 counter = counter -1
#                 if counter < 0:
#                     print('NO OK')
#                     break
#                 else:
#                     pass
#     print(counter)
#     if counter >= 0:
#         print('OK')
#
# determ('[][][[]][[[]]]')

# 10. Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
# Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").


# def char_freq(string):
#     count_dict = {}
#     for i in string:
#         count_dict[i] = string.count(i)
#     print(count_dict)
#
# char_freq('abcdddcbaaa4')

#11. Write a function dec_to_bin() that takes decimal integer and outputs its binary representation.


# def dec_to_bin_rec(digit):
#     if digit >= 1:
#         dec_to_bin_rec(digit // 2)
#         number = int(digit % 2)
#         print(number, end='')
#     elif digit == 1:
#         print('1')
#
#
#
# dec_to_bin_rec(100)
#
# def dec_to_bin_v2(digit):
#     time_list = []
#     if digit == 1:
#         print('1')
#     else:
#         while digit >= 1:
#             number = digit % 2
#             #print(number)
#             time_list.append(str(number))
#             digit = digit // 2
#     print(''.join(time_list[::-1]))
#
#
#
#
#
# dec_to_bin_v2(100)

# 12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as an order of matrix, randomly
# generates index (x, y) and checks user input (2 integers).
# (tip: use var1, var2 = raw_input("Enter two numbers here: ").split())
# *Visualize the game.

# import random
# #
# #
# def ship(digit):
#
#     new_matrix = [['*' for y in range(digit)] for z in range(digit)]
#     matrix = [['*' for y in range(digit)] for z in range(digit)]
#     print('Lets START. This is your field!')
#     for i in matrix:
#         print(i)
#
#     x = random.randrange(1,digit+1)
#     y = random.randrange(1,digit+1)
#     print(x,y)
#     pc_matrix = matrix
#     pc_matrix[x-1][y-1] = 'X'
#     print('Compute made his choice...')
#
#
#     x_u, y_u = input('Please enter two index kill pc machine?! ').split(' ')
#     i = True
#     while i:#int(x) != int(x_u) and int(y) != int(y_u):
#         new_matrix[int(x_u) - 1][int(y_u) - 1] = '-'
#         for i in new_matrix:
#             print(i)
#         x_u, y_u = input('Please try again: ').split(' ')
#
#         if int(x) == int(x_u) and int(y) == int(y_u):
#             pc_matrix[x - 1][y - 1] = 'bah!'
#             print('You win!')
#             for i in pc_matrix:
#                 print(i)
#             i = False
#
#
#
#
# ship(3)

#Task_1
#print(greet('Mentor'))

#Task_2
# print(sum([1,0,2]))
# print(multiply([1,2,1]))

#Task_3
#print(reverse('Mentor'))

#Task_4
#print(is_palindrome('radar'))

#Task_5

# print(histogram([1,2,3]))

#Task_6

print(caesar_cipher('xyz', 25))


