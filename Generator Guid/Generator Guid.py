from uuid import uuid4
from pyperclip import copy
print('Результаты будут скопированы в буфер обмена: ')
generated = []

amount = int(input("Сколько нужно GUID? "))
for i in range(amount):
    generated.append(uuid4())

copy("\n".join(str(g) for g in generated))