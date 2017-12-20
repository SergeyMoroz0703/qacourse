
import random

try:
    DIGIT = int(input('Please enter the matrix order'))
except:
    print('Enter a valid integer number')
    DIGIT = int(input('Please enter the matrix order'))
#' ⛵ '
def make_field():

    matrix = [[' ⛵ ' for y in range(DIGIT)] for z in range(DIGIT)]

    return matrix


def pc_ship():
    x = random.randrange(1,DIGIT+1)
    y = random.randrange(1,DIGIT+1)
    pc_list = []
    pc_list.append(x)
    pc_list.append(y)


    return pc_list


def u_choice(phrase):
    x_u, y_u = input(str(phrase)).split(' ')
    u_list = []
    u_list.append(int(x_u))
    u_list.append(int(y_u))
    return u_list



def game():
    for i in make_field():
        print(i)
    try_matrix = make_field()
    pc_list = pc_ship()
    print(pc_list)
    u_list = u_choice('Please input two index kill pc machine? ')
    if int(pc_list[0]) == int(u_list[0]) and int(pc_list[1]) == int(u_list[1]):
        print('You win!')
        try_matrix[u_list[0] - 1][u_list[1] - 1] = 'bah!'
        for i in try_matrix:
            print(i)
    else:
        chanse = True
        try_matrix[u_list[0]-1][u_list[1]-1] = ' - '
        for i in try_matrix:
            print(i)
        while chanse:
            u_list = u_choice('Try another one! ')
            if int(pc_list[0]) == int(u_list[0]) and int(pc_list[1]) == int(u_list[1]):
                print('You win!')
                chanse = False
                try_matrix[u_list[0]-1][u_list[1]-1]='bah!'
                for i in try_matrix:
                    print(i)
            else:
                try_matrix[u_list[0]-1][u_list[1]-1] = ' - '
                for i in try_matrix:
                    print(i)
                chanse = True



game()