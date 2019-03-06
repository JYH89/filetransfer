#-*- coding:utf-8 –*-
import datetime
import os
import re

from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from model import *
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

UPLOAD_FOLDER = os.path.dirname(__file__)

@app.route('/')
def hello_world():
    return render_template('uploadfile.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('fname')
    # 检查文件对象是否存在
    if file:
        # 去除文件名中不合法的内容
        filename = secure_filename(file.filename)
        # 将文件保存在本地UPLOAD_FOLDER目录下
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        patternos = r"HSMX_YEB_"
        patterntyzf = r"bank"
        patterntyzf1 = r"yunbank"
        if(re.match(patternos,filename)):
            saveosfile(filename)
        if(re.match(patterntyzf,filename) or re.match(patterntyzf1,filename)):
            savetyzffile(filename)
        result = Liqsubject.query.all()
        return render_template('result.html',result=result)
    else:  # 文件不合法
        return '上传失败'

#保存文件内容到osfile表
def saveosfile(filename):
    f =open(os.path.join(UPLOAD_FOLDER, filename)) #  返回一个文件对象  
    line = f.readline()#读取清算文件  
    datanum=int(line.replace("\n",""))
    uploadtime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    osfile = Osfile(vc_filename=filename, vc_uploadtime=uploadtime, vc_datanum=datanum)
    db.session.add(osfile)
    db.session.commit()
    while line and datanum>0:
        print(line, end = '')
        line = f.readline()
        detail=line.replace("\n","").encode('gbk')
        occurdate=detail[0:8]
        center=detail[8:17]
        custname=detail[17:77].decode('gbk')
        tradeacco=detail[77:97]
        fundacco=detail[97:109]
        fundcode=detail[109:115]
        occurbala=detail[115:131]
        occurflag=detail[131:133]
        inbankno=detail[133:136]
        inacconame=detail[136:236].decode('gbk')
        inbankname=detail[236:296].decode('gbk')
        inbankacco=detail[296:324]
        requestno=detail[324:348]
        moneytype=detail[348:351]
        netno=detail[351:360]
        capitalmode=detail[360:362]
        if len(capitalmode.decode().rstrip())==2:
            branchbank = detail[362:374]
            bankno = detail[374:377]
            machinedate = detail[377:391]
            custtype = detail[391:392]
            fixbusinflag = detail[392:394]
            bankstate = detail[394:395]
            targetserial = detail[395:419]
            targetfundcode = detail[419:425]
            origincapitalmode = detail[425:429]
            originserial = detail[429:451]
            custno = detail[451:463]
            origioccurflag = detail[463:465]
            banknetdate = detail[465:473]
            saleno = detail[473:481]
            tradesource = detail[481:494]
            interfacetype = detail[494:495]
            provinceno = detail[495:498]
            cityno = detail[498:502]
            reservefield = detail[502:596]
        else:
            branchbank = detail[361:373]
            bankno = detail[373:376]
            machinedate = detail[376:390]
            custtype = detail[390:391]
            fixbusinflag = detail[391:393]
            bankstate = detail[393:414]
            targetserial = detail[394:418]
            targetfundcode = detail[418:424]
            origincapitalmode = detail[424:428]
            originserial = detail[428:450]
            custno = detail[450:462]
            origioccurflag = detail[462:464]
            banknetdate = detail[464:472]
            saleno = detail[472:480]
            tradesource = detail[480:493]
            interfacetype = detail[493:494]
            provinceno = detail[494:497]
            cityno = detail[497:501]
            reservefield = detail[501:595]
        liqsubject =  Liqsubject(vc_occurdate=occurdate,
                                vc_center=center,
                                vc_custname=custname,
                                vc_tradeacco=tradeacco,
                                vc_fundacco=fundacco,
                                vc_fundcode=fundcode,
                                vc_occurbala=occurbala,
                                vc_occurflag=occurflag,
                                vc_inbankno=inbankno,
                                vc_inacconame=inacconame,
                                vc_inbankname=inbankname,
                                vc_inbankacco=inbankacco,
                                vc_requestno=requestno,
                                vc_moneytype=moneytype,
                                vc_netno=netno,
                                vc_capitalmode=capitalmode,
                                vc_branchbank=branchbank,
                                vc_bankno=bankno,
                                vc_machinedate=machinedate,
                                vc_custtype=custtype,
                                vc_fixbusinflag=fixbusinflag,
                                vc_bankstate=bankstate,
                                vc_targetserial=targetserial,
                                vc_targetfundcode=targetfundcode,
                                vc_origincapitalmode=origincapitalmode,
                                vc_originserial=originserial,
                                vc_custno=custno,
                                vc_origioccurflag=origioccurflag,
                                vc_banknetdate=banknetdate,
                                vc_saleno=saleno,
                                vc_tradesource=tradesource,
                                vc_interfacetype=interfacetype,
                                vc_provinceno=provinceno,
                                vc_cityno=cityno,
                                vc_reservefield=reservefield)
        liqsubject.osfile_id=osfile.id
        db.session.add(liqsubject)
        db.session.commit()
        datanum=datanum-1
    f.close()
    return datanum

#保存文件内容到bankcode表
def savetyzffile(filename):
    f =open(os.path.join(UPLOAD_FOLDER, filename)) #  返回一个文件对象  
    for line in f:
        line=line.replace('\n','')
        line=line.replace('("','*')
        line=line.replace('","', '*')
        line=line.replace('"),','')
        strlist=line.split('*')
        bankcode = Bankcode(bankengcode=strlist[0], banknumcode=strlist[1], bankname=strlist[2])
        db.session.add(bankcode)
        db.session.commit()
    return None

if __name__ == '__main__':
    db.create_all()    # 创建当前应用中声明的所有模型类对应的数据表，db.drop_all()是删除表
    app.run(debug=True)