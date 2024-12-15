import random

d = {}
# 0-100
ch_choise = ['back', 'front']


for i in range(100):
     ch = random.choice(ch_choise)
     if ch not in d:
        d.setdefault(ch, 0)
        d[ch] += 1
     else:
        d[ch] += 1
print(d)