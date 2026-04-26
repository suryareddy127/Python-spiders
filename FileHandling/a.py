fh=open("file1.txt","a")

# print(fh)
print(fh.tell())

fh.seek(8)
fh.write(" Bahubali")

print(fh.tell())

print