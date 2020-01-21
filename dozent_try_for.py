l = ["1", "2", "x", "y", "3"]
el = []
# falsch, fängt nur den ersten fehler ab
try:
    for i in l:
        float(i)
except Exception as e:
        el.append((i, e))

print(el)

# fängt jeden fehler ab:
el = []
for i in l:
    try:
        float(i)
    except Exception as e:
        el.append((i, e))

print(el)

for i in range(len(l)):
    try:
        l[i] = float(l[i])
    except:
        l[i] = 0.0
    
print(l)
