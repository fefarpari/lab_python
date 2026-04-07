#write
f=open("one.txt","w")
f.write("hello student.\n")
f.write("welcome yo python file handling.\n")
f.write("learning is fun.\n")
f.close()

#write old dta erased
f=open("one.txt","w")
f.write=("new content only.\n")
f.close()

#append
f=open("one.txt","a")
f.write("this line ia added at the end.\n")
f.close()

#writelines
f=open("one.txt","w")
lines=[
"python programming\n",
"file handling \n",
"error handling.\n",
"expection handling.\n"
]
f.writelines(lines)
f.close()