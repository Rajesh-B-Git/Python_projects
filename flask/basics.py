# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x-1)


# print(f(3))

# def fun(x):
#     x += 1
#     return x


# x = 2
# x = fun(x+1)
# print(x)


# dict = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dict['one']

# for k in range(len(dict)):
#     v = dict[v]

# print(v)

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2) + 1))

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)


# dict = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list)-1):
#     dict[my_list[i]] = (my_list[i],)
# for i in sorted(dict.keys()):
#     k = dict[i]
#     print(k[0])

# my_list = ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))

def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))
