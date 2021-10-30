import pymysql
import random
import json
def fuc1(x):
    y=x*x
    return y
def fuc2(x):
    y=-(x*x)
    return y
def fakedata():
    # f=open("G:/situate/static/fakedata.json","w+")
    baselon=116.350591
    baselat=39.963096
    increlon=0.0001
    increlat=0.0001
    dic=[]
    tmp=0
    lit=20
    for i in range(0,lit):
        if i<lit/4:
            increlon=i/10000*6
            increlat=fuc1(i)/10000
            tup=(baselon+increlon,baselat+increlat)
            if i==lit/4-1:
                baselon=baselon+increlon
                tmp=baselat+increlat
        elif i<lit/2 and i>=lit/4:
            increlon=(5-i)/10000*6
            increlat=fuc2(10-i)/10000+0.0025
            tup=(baselon+increlon,tmp+increlat)
            if i==lit/2-1:
                baselon=baselon+increlon
                tmp=tmp+increlat
        elif i>=lit/2 and i<lit/4*3:
            increlon=(10-i)/10000*6
            increlat=fuc2(10-i)/10000
            tup=(baselon+increlon,tmp+increlat)
            if i==lit/4*3-1:
                baselon=baselon+increlon
                tmp=tmp+increlat
        else:
            increlon=(i-15)/10000*6
            increlat=fuc1(20-i)/10000-0.0025
            tup=(baselon+increlon,tmp+increlat)
        dic.append(tup)
    dic2={}
    dic2['data']=dic
    dic2=json.dumps(dic2,indent=4)
    return dic2
dic=fakedata()
print(dic)