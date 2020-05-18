import time
print("\r")
print(" ------WELCOME TO THE RELATION WORLD-----")
print("==========================================")
print("\r")
n=input("enter your name...")
m=input("enter your crush name... ")
n=n.lower()
m=m.lower()
n=n.replace(' ','')
m=m.replace(' ','')
#print(m)
print("\r")
print("LET'S SEE!!!!")
print("\r")
l1=[]
l2=[]
b=['FRIENDS','LOVER','AFFECTION','MARRIAGE','ENEMY','SISTER/BROTHER']
h=len(n)
k=len(m)
l1=list(n)
#print(l1)
l2=list(m)
#print(l2)
for i in l1:
 for j in l2:
  if i==j:
    l2.remove(j)
    #print(l2)
    break
#print(l2)
#print(len(l2))
c=k-len(l2)
#print(c)
y=6
#print(h,k)
l=(h-c)+(k-c)
#print(l)
for i in range(5):
  b.remove(b[(l%y)-1])
  #print(b)
  if (l%y)-1!=-1:
    b=b[(l%y)-1:]+b[:(l%y)-1]
  y=y-1
print("\r")
for i in range(10,0,-1):
  time.sleep(1)
  print(i)
time.sleep(1)
print("\r")
print("here you goes.....")
time.sleep(1)
print("\r")
print("!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!!?!?!?!?!?!?!??!?!?!?!?!?")
print("\r")
print("the relation between you " +" and your crush " + str(m) + " is ---> "+ b[0])
print("\r")
print("!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!!?!?!?!?!?!?!??!?!?!?!?!?")
print("\r")


