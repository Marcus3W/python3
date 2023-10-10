import time


def heavy_work():
    for i in range(10000000):
        pass

start_time = time.time()
heavy_work()
end_time = time.time()
print(f'Duration: {end_time - start_time}')
