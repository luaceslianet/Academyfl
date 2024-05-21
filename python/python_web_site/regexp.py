import re


txt = "I like very much Spain. Spain is a beautiful country. "
x = re.sub("Spain", "France", txt, 2)
print(x)
