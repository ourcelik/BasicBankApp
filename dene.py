def func(wx, lx):
    c = 0
    for w in wx:
        if len(w) % 2 == 1 and lx in w:
            c += 1
        return c


wx = ['burcu', 'buse', 'buket', 'beste', 'ali', 'burak',
      'mehmet', 'serkan', 'sercan', 'hakan', 'ahmet']

print(func(wx, 'e'))
