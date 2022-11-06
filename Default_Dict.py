no = input().split(" ")

i_n = []

for ele in no :
    t = int(ele)
    i_n.append(t)
    
n = i_n[0]
m  = i_n[1]

a_1 = []
a_2 = []
for i in range(n):
    a_1.append(input())
    
for i in range(m):
    a_2.append(input())


for i in range(len(a_2)):
    count = 0
    po = []
    if a_2[i] in a_1 :
        for g in range(len(a_1)):
            if a_1[g] == a_2[i] :
                po.append(g+1) 
            else :
                pass    
        d  = ""
        for j in po :
            s = str(j)
            d = d + s + " "
        print(d)
    else : 
        print(-1) 
            

