with open("python.txt", "w") as f:
    f.write("� ����� � �������� ����� �����")

with open("python.txt", "r") as f:
    text = f.read(7)
    print(text)