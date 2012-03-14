def average(a,b):
    return (a+b)/2

print "1: %s" % average(2,2)

av_lam = lambda a,b: (a+b)/2

print "2: %s" % av_lam(2,2)

av_list = lambda list: sum(list)/len(list)

print "3: %s" % av_list([1,2,3,4,5])

def make_adder(x):
    def fn(a):
        return x+a
    return fn 

print "4 & 5: %s" % make_adder(10)(5)


