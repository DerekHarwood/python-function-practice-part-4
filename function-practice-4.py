from inspect import trace


def max_num(a, b, c):
    return max([a, b, c])

print(max_num(3, 5, 20)) 

def max_num_arb(*args):
    return max(args)

print(max_num_arb(3, 5, 20, 22, 5558, 5634563564)) 

def mult_list(Lst):
    if len(Lst) == 0:
        return 0
    prod = Lst[0]
    if len(Lst) > 1:
        for i in Lst[1:]:
            prod = prod * i
    return prod

print(mult_list([1, 2, 3])) 
print(mult_list([1, 2, 3, 4]))
print(mult_list([0, 2, 3, 4]))
print(mult_list([]))  

def rev_string(my_str):
    return my_str[::-1]

print(rev_string("This should be reversed"))

def num_within(x, a, b):
    return x in range(a, b + 1)

print(num_within(5, 4, 20))
print(num_within(909998098, 4, 20))

triangle = [[1], [1,1]]
def pascal(depth):
    if depth < 1:
        print("invalid depth")
    elif depth == 1:
        print([0])
    else:
        row_number = 2
        while len(triangle) < depth:
            row = []
            row_prev = triangle[row_number - 1]  
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1 

        for row in triangle:
            print(row)    

pascal(2)

triangle = [[1], [1,1]]
pascal(5)

triangle = [[1], [1,1]]
pascal(10)