#! python2.7

def unicodify(s):
    u = unicode(s, 'utf-8')
    print(u)

unicodify('Hello!')