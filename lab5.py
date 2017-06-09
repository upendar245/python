#!/python3/bin/python3
def print_twice(one):
    print(one)
    print(one)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

cat_twice('hello','hello')
