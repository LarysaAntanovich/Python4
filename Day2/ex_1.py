zdanie = "encyklopedia"
print(zdanie[4])
print(zdanie[-3])
print(zdanie[2:8])
print(zdanie[:7])
print(zdanie[1:7:2])
print(zdanie[::-1])
print(zdanie[8:])
zdanie ="antanovich"
print(zdanie[:10])


list = [[1,2,3], [4,5,6],[7,8,9]]
print(list[1][2])
print(list[1:3])
print(list[1:])
print(list[1])
print(list[2][1])


list = ["Jen","Feb","Mar"]
for x in list:
    print(x)
list = "Jen\nFeb\nMar"
print(list)

text = "Python is a fantastic snake"
how_many_chars = len(text)

list_of_indexes = range(0,how_many_chars,3)
for idx in list_of_indexes:
    print(text[idx], end="")
    print("\n\n")
    print("\n\n")
    print("\n\n")

month = ["Jen", "Feb", "Mar"]

for index, value in enumerate(month):
    print(f"Na indexie {index}: wartosc: {value}")

text = "Python is a fantastic snake"


x = text[::3]
print(x)

text = "Python is a fantastic snake"

x = text[::4]
print(x)

text = "Python is a fantastic snake"

