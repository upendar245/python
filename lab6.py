#!/python3/bin/python3
def do_twice(f,m):
    f(m)
    f(m)
    
def print_spam(test):
    print(test)


def print_twice(bruce):
    print(bruce)
    print(bruce)    
do_twice(print_spam,'hello')
