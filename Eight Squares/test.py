import heapq

a = list(map(str, [2, 5, 3, 9, 7, 1]))
heapq.heapify(a)
print(a)
k = heapq.heappop(a)
print(k, a)
heapq.heappush(a, "a")
print(a)
heapq.n
