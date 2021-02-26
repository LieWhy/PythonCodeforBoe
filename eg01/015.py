import sys

list = [1, 2, 34, 5]

it = iter(list)
while True:
    try:
        print(next(it))
    except:
        sys.exit()
