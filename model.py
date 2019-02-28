#-*-coding:utf-8-*-
#Author:raychou
from osfile import db
#保存文件信息的模型
class Osfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vc_filename=db.Column(db.String(50))
    vc_uploadtime=db.Column(db.String(14))
    vc_datanum=db.Column(db.String(30))
    def __init__(self, vc_filename, vc_uploadtime, vc_datanum):
        self.vc_filename = vc_filename
        self.vc_uploadtime = vc_uploadtime
        self.vc_datanum = vc_datanum

#定义保存清算文件明细的模型
class Liqsubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vc_occurdate = db.Column(db.String(8))
    vc_center = db.Column(db.String(9))
    vc_custname = db.Column(db.String(60))
    vc_tradeacco = db.Column(db.String(20))
    vc_fundacco = db.Column(db.String(12))
    vc_fundcode = db.Column(db.String(6))
    vc_occurbala = db.Column(db.String(16))
    vc_occurflag = db.Column(db.String(2))
    vc_inbankno = db.Column(db.String(3))
    vc_inacconame = db.Column(db.String(100))
    vc_inbankname = db.Column(db.String(60))
    vc_inbankacco = db.Column(db.String(28))
    vc_requestno = db.Column(db.String(24))
    vc_moneytype = db.Column(db.String(3))
    vc_netno = db.Column(db.String(9))
    vc_capitalmode = db.Column(db.String(2))
    vc_branchbank = db.Column(db.String(12))
    vc_bankno = db.Column(db.String(3))
    vc_machinedate = db.Column(db.String(14))
    vc_custtype = db.Column(db.String(1))
    vc_fixbusinflag = db.Column(db.String(2))
    vc_bankstate = db.Column(db.String(1))
    vc_targetserial = db.Column(db.String(24))
    vc_targetfundcode = db.Column(db.String(6))
    vc_origincapitalmode = db.Column(db.String(2))
    vc_originserial = db.Column(db.String(24))
    vc_custno = db.Column(db.String(12))
    vc_origioccurflag = db.Column(db.String(2))
    vc_banknetdate = db.Column(db.String(8))
    vc_saleno = db.Column(db.String(9))
    vc_tradesource = db.Column(db.String(12))
    vc_interfacetype = db.Column(db.String(1))
    vc_provinceno = db.Column(db.String(3))
    vc_cityno = db.Column(db.String(4))
    vc_reservefield = db.Column(db.String(94))
    osfile_id=db.Column(db.Integer,db.ForeignKey('osfile.id'))

    def __init__(self, vc_occurdate,vc_center,vc_custname,vc_tradeacco,vc_fundacco,vc_fundcode,vc_occurbala,vc_occurflag,vc_inbankno,vc_inacconame,vc_inbankname,vc_inbankacco,vc_requestno,vc_moneytype,vc_netno,vc_capitalmode,vc_branchbank,vc_bankno,vc_machinedate,vc_custtype,vc_fixbusinflag,vc_bankstate,vc_targetserial,vc_targetfundcode,vc_origincapitalmode,vc_originserial,vc_custno,vc_origioccurflag,vc_banknetdate,vc_saleno,vc_tradesource,vc_interfacetype,vc_provinceno,vc_cityno,vc_reservefield):
        self.vc_occurdate = vc_occurdate
        self.vc_center = vc_center
        self.vc_custname = vc_custname
        self.vc_tradeacco = vc_tradeacco
        self.vc_fundacco = vc_fundacco
        self.vc_fundcode = vc_fundcode
        self.vc_occurbala = vc_occurbala
        self.vc_occurflag = vc_occurflag
        self.vc_inbankno = vc_inbankno
        self.vc_inacconame = vc_inacconame
        self.vc_inbankname = vc_inbankname
        self.vc_inbankacco = vc_inbankacco
        self.vc_requestno = vc_requestno
        self.vc_moneytype = vc_moneytype
        self.vc_netno = vc_netno
        self.vc_capitalmode = vc_capitalmode
        self.vc_branchbank = vc_branchbank
        self.vc_bankno = vc_bankno
        self.vc_machinedate = vc_machinedate
        self.vc_custtype = vc_custtype
        self.vc_fixbusinflag = vc_fixbusinflag
        self.vc_bankstate = vc_bankstate
        self.vc_targetserial = vc_targetserial
        self.vc_targetfundcode = vc_targetfundcode
        self.vc_origincapitalmode = vc_origincapitalmode
        self.vc_originserial = vc_originserial
        self.vc_custno = vc_custno
        self.vc_origioccurflag = vc_origioccurflag
        self.vc_banknetdate = vc_banknetdate
        self.vc_saleno = vc_saleno
        self.vc_tradesource = vc_tradesource
        self.vc_interfacetype = vc_interfacetype
        self.vc_provinceno = vc_provinceno
        self.vc_cityno = vc_cityno
        self.vc_reservefield = vc_reservefield