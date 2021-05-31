import turtle as t

with open ('new.txt', 'r') as f:
    key = f.readlines()
    val = list(map(int, key))
		
t.shape('turtle')
size = len(val)

for i in range(0, size - 1, 2):
    t.forward(val[i])
    t.right(val[i + 1])

t.forward(val[-1])

