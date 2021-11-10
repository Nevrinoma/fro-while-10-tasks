##   Zadanije 1
#
#p=0
#for i in range(15):
#    A=0
#    while type(A)!=float:
#        try:
#            A=float(input("Sisesta "+str(i+1)+" arv >>> "))
#        except ValueError:
#            print("Vale sümbol, proovi uuesti!")
#    if A==round(A):
#        p+=1
#        print(str(A)+" >>> on täisarve")
#    else:
#        print(str(A)+" >>> ei ole täisarve")
#print(str(p)+" >>> Täisarvud")
##   Zadanije 4
#
#for k in range(10,21,1):
#    print(k**2)
##   Zadanije 7
#
#from random import *
#A=randint(10,100)
#B=randint(100,1000)
#print("A >>> "+str(A))
#print("B >>> "+str(B))
#K=int(input("K >>> "))
#for i in range(A,B+1):
#    if i%K==0: print(i)
##   Zadanije 6
# 
#from random import *
#p=0
#n=0
#N=randint(1,10)
#for i in range(N):
#    arv=int(input("Sisesta arv >>> "))
#    if arv>0:
#        p+=1
#    elif arv<0:
#        n+=1
#print("Negativsed >>> "+str(n))
#print("Positivsed >>> "+str(p))
#print("Nullid >>> "+str(N-n-p))
## Zadanije 9
#
#p=1.03
#S=float(input("Введите сумму евро которые хотите положить под 3 % залог >>> "))
#N=int(input("Введите на какое количество лет вы хотите положить свои деньги >>> "))
#for year in range(1,N+1):
#    S*=p
#    print(f"За {year}  год у вас получиться >>> {round(S,2)}")
#
## Zadanije 3
#
#proiz=1
#for i in range(8):
#    arv=float(input("Введите число >>> "))
#    if arv>0:
#        proiz*=arv
#print(proiz)
#
## Zadanije 13
#
#k=0
#S=0
#for i in range(100,1001):
#    if i%7==0:
#        print(i)
#        k+=1
#        S+=i
#print(f"Kogus >>> {k}")
#print(f"Summa >>> {S}")
#
## Zadanije 15
#
#from random import*
#for rjad in range(randint(1,100)):
#    for line in range(10):
#      print(line,end=" ")
#    print()
#
## Zadanije 16/29
#
#for rjad in range(1,10):
#    for line in range(1,10):
#        if rjad==line:
#            print("x",end=" ")
#        elif line==1:
#            print("x",end=" ")
#        else:
#            print("0",end=" ")
#    print()
#
## Zadanije slon
#
#animal=input("Buy the elephant! ")
#while animal.title()!="Elephant":
#    animal=input("Everyone says "+animal+" but you must buy the elephant! ")
#print("Good job!")
#
## Zadanije 28
#
from random import*
print("- Mini Lotery! -".center(50,"$"))
number=" "
win=randint(1,11)
while number==win: