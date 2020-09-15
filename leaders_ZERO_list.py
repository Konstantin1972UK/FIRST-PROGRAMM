import pickle

with open('LEADERS COLORS.pkl', 'wb') as f:
    l = []
    for i in range(10):
        l.append(['', ''])
    pickle.dump(l, f)
with open('LEADERS COLORS.pkl', 'rb') as f:
    a=pickle.load(f)
    print(a)