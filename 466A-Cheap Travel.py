n, m, a, b = map(int, input().split())

# 1. All rides with single tickets
option1 = n * a

# 2. All rides with m-ticket only (even if we buy more rides than needed)
import math
option2 = math.ceil(n / m) * b

# 3. Mix: as many m-tickets as possible + remaining with single tickets
option3 = (n // m) * b + (n % m) * a

# Minimum of the three options
print(min(option1, option2, option3))
