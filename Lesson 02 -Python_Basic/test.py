import re

text=input("enter:")

pattern=r"[a-z]{3}"

match=re.search(pattern,text)

print(match)