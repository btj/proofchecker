assert i == 0
assert i == 0 and 1 <= 0 + 1 # Tautologie
assert 1 <= i + 1 # Herschrijven met 2 in 1

assert True
assert 0 == 0 and 0 == 0 and 0 == 0 # Tautologie

wet('Max1', 'y <= x ==> max(x, y) == y')
wet('Max2', 'x <= y ==> max(x, y) == x')

assert True and x < y
assert x <= y # Z op 2
assert y == max(x, y) # Max2 op 1

wet('Not-Lt', 'not x < y ==> y <= x')

assert True and not x < y
assert y <= x # Not-Lt op 2
assert x == max(x, y) # Max1 op 1

assert 0 <= n and i == 0
assert i <= n # Herschrijven met 2 in 1

wet('Le-Antisym', 'x <= y and y <= x ==> x == y')

assert i <= n and not i < n
assert i <= n and n <= i # Not-Lt op 2
assert 
