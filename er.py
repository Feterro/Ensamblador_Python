import re

cadena = "1775"
patron = re.compile('^[0-9]+')


print(patron.match(cadena))


dicc = {"mbeja": 7, "abejja":8}
print(dicc)
print(sorted(dicc))
