with open("python2.txt", "w") as f:
    f.write(", �� � ���� �� ����������.")

with open("python.txt", "r") as f:
    text = f.read()

with open("python2.txt", "r") as f:
    text1 = f.read()

print(text + text1)