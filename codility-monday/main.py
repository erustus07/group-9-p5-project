import heapq
def min_filters_needed(A):
    total_pollution = sum(A)
    target_pollution= total_pollution / 2
    max_heap = []
    for pollution in A:
        heapq.heappush(max_heap, -pollution)
    filters_count = 0 
    reduced_population = 0
    while reduced_pollution < target_pollution: