import time

n = 3000
total = 0
time.perf_counter()

for i in range(n):
    for j in range(n):
        total += 1 if j >= n//2 else -1

print(f'elapsed time: {time.perf_counter()} seconds')
print(f'result: {total}')