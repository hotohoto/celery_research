from tasks import add
print(add(4, 4))
result = add.delay(4, 4)
print(result.get(timeout=1))
