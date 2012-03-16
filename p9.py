import pythagorean

for m in range(200):
    for n in range(200):
        for k in range(10):
            if sum(pythagorean.make_triple(m, n, k)) == 1000:
                pythtup = pythagorean.make_triple(m, n, k)
                print pythtup
                print pythtup[0] * pythtup[1] * pythtup[2]  


