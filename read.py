#read
f=open("one.txt","r")
data=f.read()
print("file content",data)
f.close()

#readline
f=open("one.txt","r")
data=f.read(10)
print("first part",data)
f.close()

#read lines
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1",line1)
print("line 2",line2)
print("line 3",line3)
f.close()

#readlines
f=open("one.txt","r")
lines=f.readlines()
print("list of lines",lines)
print("number of lines",len(lines))
f.close()

#read specific line of character
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()