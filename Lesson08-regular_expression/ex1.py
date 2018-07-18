import re

text=input("Enter your name:")

pattern=r'(?P<Firstname>...) (?P<Lastname>....)'

match=re.search(pattern,text)

d=match.groupdict()
print(d)