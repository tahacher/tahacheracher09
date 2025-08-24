from time import time
start = time()

#Python program to creat acronyms
word = "Artificiale Intelligence"
text = word.split()
a    = " "
for i in text:
    a = a+str(i[0]).upper()

print(a)

end = time()
execution_time = end - start
print("execution time: " , execution_time)