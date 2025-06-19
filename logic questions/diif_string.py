from collections import Counter

def maxDifference(s):
    freq = Counter(s)
    maxm = 0
    minm = len(s)
    has_odd = False
    has_even = False
    
    for count in freq.values():
        if count % 2 == 1:
            has_odd = True
            if count > maxm:
                maxm = count
        else:
            has_even = True
            if count < minm:
                minm = count
    
    if not has_odd:
        return -minm  # or handle differently
    if not has_even:
        return maxm   # or handle differently
    
    return maxm - minm

# Example usage
print(maxDifference("aabbcc"))  # -2
print(maxDifference("aaa"))     # 3 (no even frequencies)
print(maxDifference("aabb"))    # 0 (no odd frequencies)