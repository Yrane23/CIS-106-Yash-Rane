a, b = 1, 1
for _ in range(20):
    print(a, end=' ')
    a, b = b, a + b
print()