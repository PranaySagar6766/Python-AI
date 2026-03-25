def vowels(n):
    count = 0
    for ch in n.lower():
        if ch in "aeiou":
            count += 1
    return count

print(vowels("Hello World"))