data = []

for i in range(10):
    data.append(int(input("Please input 10 numbers:")))

print(sorted(data))
print(sorted(data, reverse=True))
print("The maximal number is %d." % max(data))
print("The minimal number is %d." % min(data))
print("The avarage of these ten numbers is %.2f." % (sum(data)/len(data)))
