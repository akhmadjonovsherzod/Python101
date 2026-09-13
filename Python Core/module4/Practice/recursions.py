# def get_fibo(n):
#     n_fib = None
#
#     if n < 1:
#         n_fib = "N must be > 0"
#     elif n == 1:
#         n_fib = 0
#     elif n == 2:
#         n_fib = 1
#     else:
#         prev_2, prev_1 = 0, 1
#         for i in range(2, n):
#             n_fib = prev_1 + prev_2
#             prev_2 = prev_1
#             prev_1 = n_fib
#
#     return n_fib
#
# n_f = get_fibo(5)
#
# print(n_f)

def get_fibo_recursive(n):
    if n == 1:
        n_fib = 0
    elif n == 2:
        n_fib = 1
    else:
        n_fib = get_fibo_recursive(n - 2) + get_fibo_recursive(n - 1)

    return n_fib

n_f = get_fibo_recursive(5)

print(n_f)