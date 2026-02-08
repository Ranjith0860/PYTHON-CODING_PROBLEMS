s = input("enter a string without space : ").upper()
res = 0

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# validation
for ch in s:
    if ch not in roman:
        print("❌ enter correct roman")
        break
else:
    # ✅ runs ONLY if no break happened
    for a, b in zip(s, s[1:]):
        if roman[a] < roman[b]:
            res -= roman[a]
        else:
            res += roman[a]

    res += roman[s[-1]]
    print("✅ Integer value:", res)
    
# XII     → 12
# XXVII   → 27
# XLII    → 42
# LVIII   → 58
# MCMIV   → 1904
# MCMXCIV → 1994
# MMXXIV  → 2024

