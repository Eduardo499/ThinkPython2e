# 1

def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)


# 2

def do_twice(f, a):
    f(a)
    f(a)


do_twice(print, 'Hello')


# 3

def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('Spam')

# 4

do_twice(print_twice, 'spam')


# 5

def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)


do_four(print, 'flood')
