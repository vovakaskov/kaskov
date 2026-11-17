nums = [1, 2, 2, 3, 3, 3]

freq = {}
for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)  
