assert 0 <= n and i == 0
assert i <= n # Herschrijven met 2 in 1

assert i == 0
assert i == 0 and 1 <= 0 + 1 # Z
assert 1 <= i + 1 # Herschrijven met 1 in 2

assert i <= n and i < n
assert i + 1 <= n # Z op 2

assert i <= n and i < n and n - i == oude_variant
assert i + 1 <= n and n - i == oude_variant # Z op 2
assert i + 1 <= n and 0 <= n - (i + 1) and n - i == oude_variant # Z op 1
assert i + 1 <= n and 0 <= n - (i + 1) and n - (i + 1) < n - i and n - i == oude_variant # Z
assert i + 1 <= n and 0 <= n - (i + 1) < oude_variant # Herschrijven met 4 in 3

# Wet Max1: y <= x ==> max(x, y) == x
# Wet Max2: x <= y ==> max(x, y) == y

assert True and x < y
assert x <= y # Z op 2
assert y == max(x, y) # Max2 op 1

assert True and not x < y
assert y <= x # Z op 2
assert x == max(x, y) # Max1 op 1

# Wet LeAntisym: x <= y and y <= x ==> x == y

assert i <= n and not i < n
assert i <= n and n <= i # Z op 2
assert i == n # LeAntisym op 1 en 2

# Wet If1: A ==> (E1 if A else E2) == E1
# Wet If2: not A ==> (E1 if A else E2) == E2

assert (y == max(x, y) if x < y else x == max(x, y)) and x < y
assert (y == max(x, y) if x < y else x == max(x, y)) and (y == max(x, y) if x < y else x == max(x, y)) == (y == max(x, y)) # If1 op 2
assert y == max(x, y) # Herschrijven met 2 in 1

assert (y == max(x, y) if x < y else x == max(x, y)) and x < y
assert y == max(x, y) # Herschrijven met If1 op 2 in 1

assert y == max(x, y) and x < y
assert y == max(x, y) if x < y else x == max(x, y) # Herschrijven met If1 op 2 in 1

# Wet MaxList1: 1 <= len(xs) ==> max(xs[:1]) == xs[0]
# Wet MaxList2: 1 <= i < len(xs) ==> max(xs[:i + 1]) == max(max(xs[:i]), xs[i])

assert 1 <= len(xs)
assert 1 <= 1 <= len(xs) # Z
assert 1 <= 1 <= len(xs) and xs[0] == max(xs[:1]) # MaxList1 op 2

assert 1 <= i <= len(xs) and max_ == max(xs[:i]) and i < len(xs) and max_ < xs[i]
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and max_ <= xs[i] # Z op 5
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and max(xs[:i]) <= xs[i] # Herschrijven met 3 in 4
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and xs[i] == max(max(xs[:i]), xs[i]) # Max2 op 4
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and xs[i] == max(xs[:i + 1]) # Herschrijven met MaxList2 op 1 en 2 in 4
assert 1 <= i and i + 1 <= len(xs) and xs[i] == max(xs[:i + 1]) # Z op 2
assert 1 <= i + 1 <= len(xs) and xs[i] == max(xs[:i + 1]) # Z op 1

assert 1 <= i <= len(xs) and max_ == max(xs[:i]) and i < len(xs) and not max_ < xs[i]
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and xs[i] <= max_ # Z op 5
assert 1 <= i < len(xs) and max_ == max(xs[:i]) and xs[i] <= max(xs[:i]) # Herschrijven met 3 in 4
assert 1 <= i < len(xs) and max_ == max(max(xs[:i]), xs[i]) # Herschrijven met Max1 op 4 in 3
assert 1 <= i < len(xs) and max_ == max(xs[:i + 1]) # Herschrijven met MaxList2 op 1 en 2 in 3
assert 1 <= i + 1 and i < len(xs) and max_ == max(xs[:i + 1]) # Z op 1
assert 1 <= i + 1 <= len(xs) and max_ == max(xs[:i + 1]) # Z op 2

# Wet SliceFull: xs[:len(xs)] == xs

assert 1 <= i <= len(xs) and max_ == max(xs[:i]) and not i < len(xs)
assert len(xs) <= i and i <= len(xs) and max_ == max(xs[:i]) # Z op 4
assert i == len(xs) and max_ == max(xs[:i]) # LeAntisym op 1 en 2
assert max_ == max(xs[:len(xs)]) # Herschrijven met 1 in 2
assert max_ == max(xs) # Herschrijven met SliceFull in 1

# Wet LeNeqLt: x <= y and x != y ==> x < y

assert i <= n and i != n and n - i == oude_variant
assert i < n and n - i == oude_variant # LeNeqLt op 1 en 2
assert i + 1 <= n and n - i == oude_variant # Z op 1
assert i + 1 <= n and 0 <= n - (i + 1) and n - i == oude_variant # Z op 1
assert i + 1 <= n and 0 <= n - (i + 1) < n - i and n - i == oude_variant # Z
assert i + 1 <= n and 0 <= n - (i + 1) < oude_variant # Herschrijven met 4 in 3

assert i <= n and not i != n
assert i == n # Z op 2
