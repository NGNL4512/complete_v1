# -*- coding: utf-8 -*-
import os
import numpy as np
"""
Created on Sun Oct 20 00:09:07 2019

@author: top
"""
#文章音檔比對
def totalPK(mood,normal):
    totalscore=[0,0,0,0,0]
    addtotalscore=0
    normalpk=normal[0]*1.5
    normalpk1=normal[0]*0.75
    if(mood[0]>normalpk):
        totalscore[0]=totalscore[0]+1
    elif(mood[0]<normalpk1):
        totalscore[1]=totalscore[1]+1
        totalscore[2]=totalscore[2]+1
        totalscore[3]=totalscore[3]+1
    normalpk=normal[1]*1.5
    normalpk1=normal[1]*0.65
    if(mood[1]>normalpk):
        totalscore[0]=totalscore[0]+1
        totalscore[3]=totalscore[3]+1
    elif(mood[1]<normalpk1):
        totalscore[1]=totalscore[1]+1
        totalscore[2]=totalscore[2]+1
    normalpk=normal[2]*1.25
    normalpk1=normal[2]*0.8
    if(mood[2]>normalpk):
        totalscore[0]=totalscore[0]+1
        totalscore[2]=totalscore[2]+1
    elif(mood[2]<normalpk1):
        totalscore[1]=totalscore[1]+1
        totalscore[3]=totalscore[3]+1
    #print("文章情緒分數",totalscore[0],totalscore[1],totalscore[2],totalscore[3])
    for i in range(0,5):
        addtotalscore=addtotalscore+totalscore[i]
    if(addtotalscore==0):
        return totalscore
    else:
        for i in range(0,5):
            totalscore[i]=totalscore[i]*100/addtotalscore
        return totalscore

#斷句音檔比對    
def PK(mood,normal):
    score=[0,0,0,0,0]
    addscore=0
    scarepk=normal[3]*1.35
    scarepk1=normal[3]*1.2
    scarepk2=normal[3]*0.8
    scarepk3=normal[3]*0.6
    if(mood[3]>scarepk):
        score[0]=score[0]+2
    elif(scarepk1<mood[3]<=scarepk):
        score[0]=score[0]+1
    elif(scarepk3<mood[3]<=scarepk2):
        score[1]=score[1]+1
        score[2]=score[2]+1
        score[3]=score[3]+1
    elif(mood[3]<=scarepk3):
        score[1]=score[1]+2
        score[2]=score[2]+2
        score[3]=score[3]+2
    scarepk=normal[4]*1.5
    scarepk1=normal[4]*1.25
    scarepk2=normal[4]*0.85
    scarepk3=normal[4]*0.75
    if(mood[4]>scarepk):
        score[0]=score[0]+2
        score[3]=score[3]+2
    elif(scarepk1<mood[4]<=scarepk):
        score[0]=score[0]+1
        score[3]=score[3]+1
    elif(scarepk3<mood[4]<=scarepk2):
        score[1]=score[1]+1
        score[2]=score[2]+1
    elif(mood[4]<=scarepk3):
        score[1]=score[1]+2
        score[2]=score[2]+2
    scarepk=normal[5]*1.2
    scarepk1=normal[5]*1.1
    scarepk2=normal[5]*0.8
    scarepk3=normal[5]*0.65
    if(mood[5]>scarepk):
        score[0]=score[0]+2
        score[2]=score[2]+2
    elif(scarepk1<mood[5]<=scarepk):
        score[0]=score[0]+2
        score[2]=score[2]+2
    elif(scarepk3<mood[5]<=scarepk2):
        score[1]=score[1]+1
        score[3]=score[3]+1
    elif(mood[5]<=scarepk3):
        score[1]=score[1]+2
        score[3]=score[3]+2
    scarepk=normal[6]*2
    if(mood[6]>scarepk):
        score[1]=score[1]+1
        score[3]=score[3]+1
    #print("斷句情緒分數",score[0],score[1],score[2],score[3])        
    for i in range(0,5):
        addscore=addscore+score[i]
    if(addscore==0):
        return score
    else:
        for i in range(0,5):
            score[i]=score[i]*100/addscore
        return score

def final(totalscore,score):
    finalscore=[0,0,0,0,0]
    for i in range(0,5):
        finalscore[i]=(totalscore[i]+score[i])/2
    return finalscore

def errorcount(totalscore,score):
    error=0
    for i in range(0,5):
        if(totalscore[i]-score[i]>0):
            error=error+totalscore[i]-score[i]
        else:
            error=error+score[i]-totalscore[i]
    error=error/200
    return error

#存檔
def text_cw(name, msg):
    desktop_path = ".\\images\\"
    folder = os.path.exists(desktop_path)
    #判斷結果
    if not folder:
        #如果不存在，則建立新目錄
        os.makedirs(desktop_path)
        print('-----建立成功-----')
    #elif(t==0):
        #shutil.rmtree(desktop_path)
        #os.makedirs(desktop_path)
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w',encoding='UTF-8')
    for es in range(6):
        file.write(msg[es])
        file.write('\n')
    file.close()

#讀情緒數值
f = open('./images/1/all/mood.txt','r',encoding='utf-8')
mood = []
line = f.readlines

for line in f:
    line = ''.join(line).strip('\n')
    mood.append(line)
    
mood[0]=float(mood[0][7:])
mood[1]=float(mood[1][6:])
mood[2]=float(mood[2][5:])
mood[3]=float(mood[3][7:])
mood[4]=float(mood[4][8:])
mood[5]=float(mood[5][5:])
mood[6]=float(mood[6][7:])

for i in range(len(mood)):  
    print(mood[i])

f.close()

#讀常模數值
f = open('./images/a.txt','r',encoding='utf-8')
normal = []
line = f.readlines

for line in f:
    line = ''.join(line).strip('\n')
    normal.append(line)
    
normal[0]=float(normal[0][7:])
normal[1]=float(normal[1][8:])
normal[2]=float(normal[2][5:])
normal[3]=float(normal[3][7:])
normal[4]=float(normal[4][8:])
normal[5]=float(normal[5][5:])
normal[6]=float(normal[6][7:])
    
for i in range(len(normal)):
    print(normal[i])
    
f.close()


totalscore=totalPK(mood,normal)
#print("文章情緒分數比例",totalscore[0],totalscore[1],totalscore[2],totalscore[3],totalscore[4])

score=PK(mood,normal)
#print("斷句情緒分數比例",score[0],score[1],score[2],score[3],score[4])

finalscore=final(totalscore,score)
print("生氣比例:"+str(finalscore[0]))
print("悲傷比例:"+str(finalscore[1]))
print("焦慮比例:"+str(finalscore[2]))
print("害怕比例:"+str(finalscore[3]))
print("憂鬱比例:"+str(finalscore[4]))

error=errorcount(totalscore,score)
print("誤差值",error)

aa=np.array(["生氣比例:"+str(finalscore[0])
            ,"悲傷比例:"+str(finalscore[1])
            ,"焦慮比例:"+str(finalscore[2])
            ,"害怕比例:"+str(finalscore[3])
            ,"憂鬱比例:"+str(finalscore[4])
            ,"誤差值:"+str(error)])

text_cw("b",aa)

