m = [1,1,2,2,3,3,3,4,4,4,4]
uniq_m = list(set(m))
print (m)
 
p=[1,1,2,2,3,3,4,4,5,6,6,7,8,8]
set(p)
 
m = [1,1,2,2,3,3,3,4,4,4,4]
uniq_list=[]
for companies in m:
    if companies not in uniq_list:
        uniq_list.append(companies)
    else:
        continue
print(uniq_list)