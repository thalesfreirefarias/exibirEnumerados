produtos = [
"iphone",
"ipad",
"airpod",
"macbook"
]

for item in produtos:
  print(item)

for i in range(len(produtos)):
  print(i, produtos[i])

i =0
for item in produtos :
  print (i, item)
  i += 1 

for i, item in enumerate(produtos):
  print(i, item)