def ignore(fn):
    def do():
        pass
    return do

@ignore
def test():
    return "HAHA"

print "1: %s" % test()

from functools import wraps
from time import time
def timed(fn):
    @wraps(fn)
    def do(*args, **kwargs):
        before = time()
        fn(*args, **kwargs)
        after = time()
        
        print "%s used %s s" % (fn.__name__, after-before)
    return do

from time import sleep
@timed
def timed_func():
    sleep(0)

print "2:"
timed_func()


def deprecated(fn):
    @wraps(fn)
    def do():
        print "\nNB! %s is deprecated" % fn.__name__
        fn()
    return do

@deprecated
def dep():
    print "This is old shit"

print "3: %s" % dep()

def memoize(fn):
    print "memoizing:"
    res = {}
    def do(arg):
        if arg in res:
           return res[arg] 
        else:
            res[arg] = fn(arg)
            return res[arg]
    return do

@memoize
def fib(a):
    if a in (0,1): return a
    return fib(a-1) + fib(a-2)

print fib(100)
