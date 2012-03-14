res = [2**i for i in range(10)]

print "Oppgave 1: %s" % res

dic = {i: 2**i for i in range(10)}

print "2: %s" % dic


div = [i for i in range(100) if i%3==0 or i%7==0]

print "3: %s" % div

odd = [(i*j) for i in range(3,8) for j in range(10,15) if (i*j)%2!=0]

print "4: %s" % odd

dobbel = [[i*j for i in range(1, 11)] for j in range(1, 11)]

print "5: %s" % dobbel


