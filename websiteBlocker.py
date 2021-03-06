import notify, database, os
# change hosts path according to your OS
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP
redirect = "127.0.0.1"

googleDomains = "google.com,google.ad,google.ae,google.com.af,google.com.ag,google.com.ai,google.al,google.am,google.co.ao,google.com.ar,google.as,google.at,google.com.au,google.az,google.ba,google.com.bd,google.be,google.bf,google.bg,google.com.bh,google.bi,google.bj,google.com.bn,google.com.bo,google.com.br,google.bs,google.bt,google.co.bw,google.by,google.com.bz,google.ca,google.cd,google.cf,google.cg,google.ch,google.ci,google.co.ck,google.cl,google.cm,google.cn,google.com.co,google.co.cr,google.com.cu,google.cv,google.com.cy,google.cz,google.de,google.dj,google.dk,google.dm,google.com.do,google.dz,google.com.ec,google.ee,google.com.eg,google.es,google.com.et,google.fi,google.com.fj,google.fm,google.fr,google.ga,google.ge,google.gg,google.com.gh,google.com.gi,google.gl,google.gm,google.gr,google.com.gt,google.gy,google.com.hk,google.hn,google.hr,google.ht,google.hu,google.co.id,google.ie,google.co.il,google.im,google.co.in,google.iq,google.is,google.it,google.je,google.com.jm,google.jo,google.co.jp,google.co.ke,google.com.kh,google.ki,google.kg,google.co.kr,google.com.kw,google.kz,google.la,google.com.lb,google.li,google.lk,google.co.ls,google.lt,google.lu,google.lv,google.com.ly,google.co.ma,google.md,google.me,google.mg,google.mk,google.ml,google.com.mm,google.mn,google.ms,google.com.mt,google.mu,google.mv,google.mw,google.com.mx,google.com.my,google.co.mz,google.com.na,google.com.ng,google.com.ni,google.ne,google.nl,google.no,google.com.np,google.nr,google.nu,google.co.nz,google.com.om,google.com.pa,google.com.pe,google.com.pg,google.com.ph,google.com.pk,google.pl,google.pn,google.com.pr,google.ps,google.pt,google.com.py,google.com.qa,google.ro,google.ru,google.rw,google.com.sa,google.com.sb,google.sc,google.se,google.com.sg,google.sh,google.si,google.sk,google.com.sl,google.sn,google.so,google.sm,google.sr,google.st,google.com.sv,google.td,google.tg,google.co.th,google.com.tj,google.tl,google.tm,google.tn,google.to,google.com.tr,google.tt,google.com.tw,google.co.tz,google.com.ua,google.co.ug,google.co.uk,google.com.uy,google.co.uz,google.com.vc,google.co.ve,google.vg,google.co.vi,google.com.vn,google.vu,google.ws,google.rs,google.co.za,google.co.zm,google.co.zw,google.cat,calendar.google.com,play.google.com,drive.google.com,mail.google.com,meet.google.com,duo.google.com,classroom.google.com,docs.google.com,forms.google.com,shopping.google.com,myaccount.google.com"
# websites That you want to block
website_list = []

def block(web, mode):    
    database.setWebs((database.getWebs(mode)+web+","), mode)
           
def unblock(mode):
        website_list.clear()
        database.setWebs("", mode) 

def unblockS(web, mode):
    websites = database.getWebs(mode)
    websites = websites.split(",")
    website_list.clear()
    
    for webs in websites:
        if webs != web: website_list.append(webs)
    if "" in website_list: website_list.remove("")
    x = ""

    for i in website_list: 
        x = x+i+","
    database.setWebs(x, mode) 
    
def Google(modal): 
    webList = ""
    if modal == 0: 
        websites = database.getWebs(1)
        websites = websites.split(',')
        website_list.clear()
        for web in websites:
            if web in googleDomains.split(','): pass
            else: 
                if web!= '':
                    webList = webList+web+','
        unblock(1)
        database.setWebs(webList, 1)    
    else: block(googleDomains, 1)
    
    
def restrictedPages(): 
    webList = []
    google = False
    googledomainslist = googleDomains.split(",")
    
    webs = database.getWebs(1)
    
    if webs !="":
        webs = webs.split(',')
        
        for i in webs:
            if i in googledomainslist: google = True
            else:
                if i != "": webList.append(i)
    
    
    file = open("WebsRestringidas.txt", "w")
    file.write("P??ginas Web Restringidas:"+"\n")

    for data in webList:
        file.write("\n")
        file.write("- "+data+"\n")
    if webList == [] and google == False:
        file.write("\n")
        file.write("No hay p??ginas web bloqueadas")
    if google:
        file.write("\n")
        file.write("Dominios de Google Bloqueados")
    file.close()
    
    os.system('WebsRestringidas.txt')