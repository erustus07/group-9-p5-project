import heapq
def min_filters_needed(A):
    total_pollution = sum(A)
    target_pollution= total_pollution / 2
    max_heap = []
    for pollution in A:
        heapq.heappush(max_heap, -pollution)

    filters_count = 0 
    reduced_pollution = 0


    while reduced_pollution < target_pollution:
        max_pollution = -heapq.heappop(max_heap)
        reduced_pollution += max_pollution / 2
        heapq.heappush(max_heap, -(max_pollution / 2))
    filters_count += 1
    return filters_count

# Test cases
if __name__ == "__main__":
    print(min_filters_needed([5, 19, 8, 1])) 
    print(min_filters_needed([10, 10]))