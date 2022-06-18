import matplotlib .pyplot as plt
import psutil as p

names = {}
count = 0

for process in p.process_iter():
    count = count + 1
    if count <= 6:
        name = process.name()
        usage = p.cpu_percent()
        print("Name: " + str(name) + " Usage: " + str(usage))
        names.update({name:usage})
        
keymax = max(names, key=names.get)
print(keymax)
keymin = min(names, key=names.get)
print(keymin)
name_list = [keymax, keymin]
print(name_list)

app = names.values()
maxapp = max(app)
minapp = min(app)
maxMinlist = [maxapp, minapp]
print(maxMinlist)

plt.figure(figsize=(15,7))
plt.xlabel("Apps")
plt.ylabel("Usage")
plt.bar(names, maxMinlist, width=0.7, color=("blue", "red"))
plt.show()