import fileinput

#given = input("Provide a string: ")
given = str(fileinput.input())
uniqueChars = list(set(given))

odds = 0
result = 'YES'

for uchar in uniqueChars:
    if given.count(uchar) % 2 == 1:
        odds += 1
    if odds > 1:
        result = 'NO'
        break

print(result)