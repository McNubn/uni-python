currentBook = {'title':'The Fellowship of the Ring','author':'JRR Tolkien','price':9.99}
print(currentBook)
print(currentBook["author"])
currentBook["ISBN"] = 93458353

for x in currentBook.values():
    print(x)