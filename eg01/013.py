import sys
list = [1,2,34,78]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
