assert i == 0
assert i == 0 and 1 <= 0 + 1 # Z
assert 1 <= i + 1 # Herschrijven met 2 in 1

assert True
assert 0 == 0 and 0 == 0 and 0 == 0 # Z

# Wet Max1: x <= y ==> max(x, y) == y
# Wet Max2: y <= x ==> nax(x, y) == x

assert True and x < y
assert x <= y # Z op 2
assert y == max(x, y) # Max2 op 1

# Wet NotLt: not x < y ==> y <= x

assert True and not x < y
assert y <= x # NotLt op 2
assert x == max(x, y) # Max1 op 1

assert 0 <= n and i == 0
assert i <= n # Herschrijven met 2 in 1

# Wet LeAntisym: x <= y and y <= x ==> x == y

assert i <= n and not i < n
assert i <= n and n <= i # NotLt op 2
assert i == n # LeAntisym op 1 en 2

assert i <= n and i < n
assert i + 1 <= n # Z op 2

assert i <= n and i < n and n - i == oude_variant
assert i + 1 <= n and n - i == oude_variant # Z op 2
assert i + 1 <= n and 0 <= n - (i + 1) and n - i == oude_variant # Z op 1
assert i + 1 <= n and 0 <= n - (i + 1) and n - (i + 1) < n - i and n - i == oude_variant # Z
assert i + 1 <= n and 0 <= n - (i + 1) < oude_variant # Herschrijven met 4 in 3

# Wet If1: A ==> (E1 if A else E2) == E1
# Wet If2: not A ==> (E1 if A else E2) == E2

assert (y == max(x, y) if x < y else x == max(x, y)) and x < y
assert (y == max(x, y) if x < y else x == max(x, y)) and (y == max(x, y) if x < y else x == max(x, y)) == (y == max(x, y)) # If1 op 2
assert y == max(x, y) # Herschrijven met 2 in 1
