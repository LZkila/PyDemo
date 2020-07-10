# 递归
def fact(x):
    if x < 0:
        return 0
    if x <= 1:
        return 1 
    return x * fact(x - 1)

# 尾递归
def tail_fact2(x, a):
    return a if x == 1 else tail_fact2(x - 1, a * x)

def tail_fact(x):
    if (x < 0):
        return 0
    return 0 if x == 0 else tail_fact2(x, 1) 

if __name__ == '__main__':
    print(tail_fact(5))
