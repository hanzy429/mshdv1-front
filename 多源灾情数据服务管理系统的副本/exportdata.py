import pymysql
import random
import json
import time
def exportdata():
    conn = pymysql.connect(host='112.126.83.24', port=3306, user='work', password='Eqgrp123!', db='eqe', charset='utf8')
    cursor = conn.cursor()
    sql="SELECT distinct lon,lat FROM eqe.tb_info where lon!=0 and lat!=0"
    cursor.execute(sql)
    result=cursor.fetchall()
    dic=[]
    # f=open("G:/situate/static/telecom.js","w+")
    # for i in result:
    #     tup=(i[0]+(random.randint(0,20)-10)*0.001,i[1]+(random.randint(0,20)-10)*0.001,random.randint(0,9))
    #     dic.append(tup)
    # dic2={}
    # dic2['data']=dic
    # dic2=json.dumps(dic2,indent=4)
    # f.write(dic2)
    # f.close()
    flag=random.randint(0,2)
    if flag==1:
        for i in result:
            tup=(i[0],i[1],random.randint(0,9))
            dic.append(tup)
    else:
        f=open("/usr/share/nginx/html/telecom.js","r")
        return(f.read())
    dic2={}
    dic2['data']=dic
    dic2=json.dumps(dic2,indent=4)
    cursor.close()
    conn.close()
    return dic2
dic2=exportdata()
print(dic2)
    
