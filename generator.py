def countdown(i):
    while i > 0:
        yield i
        i -= 1

#for i in countdown(5):
#    print i,

generator = (i for i in range(10))

#for i in generator:
#    print i,


even = [i for i in range(20) if i%2==0]

print "1: %s" % even

even_gen = (i for i in range(20) if i%2==0)

print "2:"
for i in even_gen:
    print i,

from itertools import count
def all_even_numbers():
     c = count()
     while True:
        i = c.next()
        if(i%2==0):
            yield i

def allepartall():
    i = 0
    while True:
        if i%2 == 0:
            yield i
        i += 1

print "3:"
#for i in all_even_numbers():
#    print i,

all_even = (i for i in count() if i%2==0)

print "4:"

#for i in all_even:
#    print i,

print "Oppgave 5: %s " % [all_even.next() for i in xrange(20)]

def weird():
    c = count()
    while True:
        i = c.next()
        yield i
        yield -i

print "6:"

#for i in weird():
#    print i,

def fib():
    a,b = 1,1
    yield a
    while True:
        yield a
        a, b = a+b, a

a = fib()

for i in xrange(100000):
    res = a.next()

print "Oppgave 7: %s" % res
    
