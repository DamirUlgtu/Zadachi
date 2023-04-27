lst = ['cool', 'lock', 'cook']
letters = set(lst[0])
for word in lst[1:]:
    letters = letters.intersection(set(word))
    result = sorted(list(letters))

print(''.join(result))