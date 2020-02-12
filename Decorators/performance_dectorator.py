from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        time1 = time()
        final_result = fn(*args, **kwargs)
        time2 = time()
        print(f'took {time2-time1}')
        return final_result
    return wrapper


@performance
def time_it_took():
    for i in range(100000):
        pass


time_it_took()
