def matrix(m,n,a,b):

  r = []; columns = []
  for i in range(0,m):
    r += [0]
  for j in range (0,n):
    columns += [0]
  for i in range (0,m):
    r[i] = columns
  print (r)

  g = []; t = []
  for i in range(0,a):
    g += [0]
  for i in range (0,b):
    t += [0]
  for i in range (0,a):
    g[i] = t
  print (g)

  for i in range(len(r)):
    for j in range(len(r[0])):
      r[i][j]=input('enter matrix')
  for i in range(len(g)):
    for j in range(len(g[0])):
      g[i][j]=int(input('enter matrix2'))
  print(r)
  print(g)
  result=[];u=[]
  for i in range(0,m):
    result += [0]
  for j in range (0,b):
    u += [0]
  for i in range (0,m):
    result[i] = u
    s=result
  for i in range(len(r)):
    for j in range(len(g[0])):
      s[i][j]=[0]
      for k in range(len(g)):
        s[i][j] += r[i][k]*g[k][j]
        
  print(s)
m = int(input('number ofrows, m = '))
n = int(input('number of columns, n = '))
a = int(input('number of rows for m2, a = '))
b = int(input('number of columns for m2, b = '))
matrix(m,n,a,b)
