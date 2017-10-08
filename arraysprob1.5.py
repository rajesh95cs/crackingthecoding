a = []
a = input("enter the string: ")

compressed = []
count = 1
for i  in range(1,len(a)):
    if(a[i-1] != a[i]):
        compressed.append(a[i-1])
        compressed.append(count)
        count = 1
    else:
        count += 1

compressed.append(a[i])
compressed.append(count)
str1 = ''.join(a)
str2 = ''.join(str(e) for e in compressed)

if(len(a)>len(compressed)):
    print("the commpressed string is ",str2)
else:
    print("the original string is smaller ",str1)
