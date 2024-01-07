import time

def for_loop(rang: int, decimals: int) -> float:
    start_time_for_loop = time.perf_counter()
    my_list_for_loop = []
    n = 2
    for i in range(rang):
        n = i * n
        my_list_for_loop.append(n)
    return round(time.perf_counter() - start_time_for_loop, decimals)




def comprehension_loop(rang: int, decimals: int) -> float:
    start_time_comprehension_loop = time.perf_counter()
    n = 2
    my_list_comprehension_loop = [n * i for i in range(rang)]
    return round(time.perf_counter() - start_time_comprehension_loop, decimals)





print(for_loop(10, 20))
print(comprehension_loop(10, 20))