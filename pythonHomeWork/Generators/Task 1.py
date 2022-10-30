def s(a):
    for i in a:
        if i.isalpha():
            yield i
w = s('ajb#bj0 0')
for i in w:
    print(w)