def solve(arr):
    from collections import Counter
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))
