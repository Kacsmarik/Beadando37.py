import math
def pytagoras_harmas(n):
    res=[]
    for b in range(n):
        for a in range(1, b):
            c=math.sqrt(a*a+b*b)
            print(("a:",a,"b",b,"c",c))
            if c%1==0:
                res.append((a,b,int(c)))
    return  res

def haromszog_terulet(tuple):
    a=tuple[0]
    b= tuple[1]
    c= tuple[2]
    s=(a+b+c)/2
    terulet=(s*(s-a)-(s-b)*(s-c))**0.5
    return terulet


numbers=[]
t=0
while True:
    inputs= input("szamok '*' végjelig: ")
    if inputs== "*" and t<3:
        print("Nem adtál meg elég számot.")
        break
    if inputs == "*" and t>=3:
        break
    numbers.append(int(inputs))
    t+=1

max=sorted(numbers)[-1]

minden_harmas=pytagoras_harmas(max)

print("összes hármas:",minden_harmas)

temp_list=[]
rest=numbers

for i in range(len(minden_harmas)):
    for j in minden_harmas[i]:
        if j in numbers:
            print("asd",j)
            temp_list.append(j)
            rest.remove(j)

print("templist",temp_list)
print("rest",rest)

tuples=[]
for i in range(0,len(temp_list),3):
    tuples.append(tuple(temp_list[i:i+3]))

for i in tuples:
    if len(i) !=3:
        tuples.remove(i)
areas= {}
for i in tuples:
    areas[i]=haromszog_terulet(i)
print("areas",areas)

s_list = []

for i in tuples:
    s1=0
    s2=0
    s3=0
    s1+=rest.count(i[0])
    s2+=rest.count(i[1])
    s3+=rest.count(i[2])
    s_list.append((s1,s2,s3))

mennyi_elofordulas=[]
for i in range(len(s_list)):
    mennyi_elofordulas.append(min(s_list[i]))

with open("beadandomegoldas_output.txt","w",encoding='UTF-8') as out_file:
    for i in range(len(tuples)):
        print("Számhármasok:",tuples[i],"Előfordulások száma:",mennyi_elofordulas[i]+1,"Területe:",areas[tuples[i]],file=out_file)

