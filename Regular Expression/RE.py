import re
msg ="good morning. Have a good Day"

match= re.search(r'good', msg)

print(match)
match = bool(re.search(r'good', msg))
print(match)

match = re.search(r'good', msg)
if match:
    print(match.span())
    print(match.group())
else:
    print("no match")


date = '28-04-2003'
pattern = re.sub(r'\d{2}','01',date , count = 1)
print(pattern)


print(re.findall(r'good' , msg))




words = "sit wit chit shit that bit dat fat pit it fit unit"

print(bool(re.search(r'^sit' ,words)))
print(bool(re.search(r'unit$' ,words)))


pattern = r'\b[a-z]*it\b'
print(re.findall(pattern,words))








