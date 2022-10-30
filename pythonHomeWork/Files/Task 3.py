original = input("¬ведите им€ исходного файла:")
target = input("¬ведите им€ целевого файла:")

with open(original, "r") as f, open(target, "w") as d:
    data = f.readlines()
    for i in range(len(data)):
        d.write(f'{i}: {data[i]}')