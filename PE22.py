names = [name.replace('"', "") for name in sorted(open("names.txt").readlines()[0].split(","))]
print(sum(sum([(ord(letter) - 64) * (names.index(name) + 1) for letter in name]) for name in names))