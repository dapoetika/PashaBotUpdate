#asd

import requests

from tkinter.ttk import *
import bs4

from tkinter import *
import time
import subprocess
from threading import Thread
import win32gui
import pyautogui
from python_imagesearch import imagesearch
import os
import datetime
def login():
    vericek = open("./data/data.txt")
    username = vericek.readline().rstrip()
    password = vericek.readline().rstrip()
    
    try:
        r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/login",json={"username":username,"password":password}, timeout=(15, 30))
        return r
    except:
        print("internet bağlantısı yok")
        return
def sonrakihesapgir(window,r):
    vericek = open("./data/data.txt")
    username = vericek.readline().rstrip()
    password = vericek.readline().rstrip()
    hesapsayisi = vericek.readline().rstrip()
    #sonraki girişler

    frame2 = Frame(window,height = 100,width = 400,background= "DarkSlateGray4", borderwidth=2, relief="groove")
    frame2.pack(fill='both', expand=True)
    labelhesapsayisi = Label(frame2,text="Farm Count",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
    labelhesapsayisi.pack()
    hesapentry = Entry(frame2,background="antiquewhite3",justify = CENTER)
    hesapentry.pack()
    hesapentry.insert(0,hesapsayisi)
    btn = Button(frame2,text="Start", height=2, width=10, background="MediumSpringGreen",command=lambda: otekigecis(window,int(hesapentry.get()),username,password,frame2,r),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised")
    btn.pack()
def ilkhesapgir(window):
    # ilk giriş

    frame2 = Frame(window,height = 100,width = 400,background = "DarkSlateGray4")
    #frame2.place(x=105,y = 115)
    frame2.pack(fill='both', expand=True)
    nicknamelabel = Label(frame2,text="Username",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
    nicknamelabel.pack()
    nickentry = Entry(frame2,background="antiquewhite3")
    nickentry.pack()


    """defaultnick = vericek.readline()
    defaultnick = defaultnick[0:-1]
    nickentry.insert(0,defaultnick)"""



    passwordlabel = Label(frame2,text="Password",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
    passwordlabel.pack()
    passwordentry = Entry(frame2,background="antiquewhite3",show = "*")
    passwordentry.pack()

    """defaultpass = vericek.readline()
    defaultpass = defaultpass[0:-1]
    passwordentry.insert(0,defaultpass)"""


    
    labelhesapsayisi = Label(frame2,text="Farm Count",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
    labelhesapsayisi.pack()
    hesapentry = Entry(frame2,background="antiquewhite3",justify = CENTER)
    hesapentry.pack()

    buttonok = Button(text="Start", height=2, width=10, background="MediumSpringGreen",command=lambda: gecis(window,hesapentry,passwordentry,nickentry,frame2),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised")
    buttonok.place(x=500,y = 250)

    
def otekigecis(window,hesapsayisi,nickname,password,frame2,r):
    frame2.destroy()
    data = open("./data/data.txt")

    first = data.readline().rstrip()
    sec = data.readline().rstrip()
    third = data.readline().rstrip()
    fourth = data.readline().rstrip()

    data = open("./data/data.txt","w")
    data.write(str(nickname).rstrip()+"\n")
    data.write(str(password).rstrip()+"\n")
    data.write(str(hesapsayisi).rstrip()+"\n")
    data.write(str(fourth).rstrip()+"\n")
    tablegiris(window,hesapsayisi,nickname,password,r) 

def gecis(window,hesapentry,passwordentry,nickentry,frame):

    hesapsayisi = hesapentry.get().rstrip()
    username = str(nickentry.get().rstrip())
    password = str(passwordentry.get().rstrip())

    frame.destroy()
    print(username,password)
    r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/login",json={"username":username,"password":password}, timeout=10)

    if r.status_code==200:
        data = open("./data/data.txt","w")
        data.write(str(username).rstrip()+"\n")
        data.write(str(password).rstrip()+"\n")
        data.write(str(hesapsayisi).rstrip()+"\n")
        tablegiris(window,hesapsayisi,username,password,r) 
        
    else:
        ilkhesapgir(window)

def show_frame(frame):
    frame.tkraise()

def reverseBool(hangiListe,m):
    hangiListe[m] = not hangiListe[m]
    
def tablegiris(window,hesapsayisi,nickname,password,r):
    
    hesapsayisi = int(hesapsayisi)
    data = r.json().get("userData")
    print(data)
    tab_buttons = Frame(window,background="DarkSlateGray4")
    tab_buttons.pack(side="top",anchor="w")

    content = Frame(window)
    content.pack(fill='both', expand=True)

    global ayarlarTABlist
    ayarlarTABlist = []
    hesaplarTABlist= []
    """Farm Ayarları Tab Ayarları"""
    frm = Frame(content,background="DarkSlateGray4")
    ayarlarTABlist.append(frm)

    btn1 = Button(tab_buttons, text='    Farm     ', command=lambda: show_frame(frm))
    btn1.grid(row=0, column=0)
    
    if hesapsayisi > 15:
        frm11 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm11)
        btn1 = Button(tab_buttons, text='   Farm 2    ', command=lambda: show_frame(frm11))
        btn1.grid(row=0, column=1)
    if hesapsayisi > 30:
        frm12 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm12)
        btn1 = Button(tab_buttons, text='   Farm 3    ', command=lambda: show_frame(frm12))
        btn1.grid(row=0, column=2)
        
    if hesapsayisi > 45:
        frm13 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm13)
        btn1 = Button(tab_buttons, text='   Farm 4    ', command=lambda: show_frame(frm13))
        btn1.grid(row=0, column=3)

    if hesapsayisi > 60:
        frm14 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm14)
        btn1 = Button(tab_buttons, text='   Farm 5    ', command=lambda: show_frame(frm14))
        btn1.grid(row=0, column=4)
        
    if hesapsayisi > 75:
        frm15 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm15)
        btn1 = Button(tab_buttons, text='   Farm 6    ', command=lambda: show_frame(frm15))
        btn1.grid(row=0, column=5)
        
    if hesapsayisi > 90:
        frm16 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm16)
        btn1 = Button(tab_buttons, text='   Farm 7    ', command=lambda: show_frame(frm16))
        btn1.grid(row=0, column=6)
    if hesapsayisi > 105:
        frm17 = Frame(content,background="DarkSlateGray4")
        ayarlarTABlist.append(frm17)
        btn1 = Button(tab_buttons, text='   Farm 8    ', command=lambda: show_frame(frm17))
        btn1.grid(row=0, column=7)
    
    for f in ayarlarTABlist:
        f.place(relx=0, rely=0, relwidth=1, relheight=1)

    """Hesap Kayıt Tab ayarları"""
    frm2 = Frame(content,height = (30*(15-2))+65,width = 750,background= "DarkSlateGray4", relief="groove")
    frm2.place()
    hesaplarTABlist.append(frm2)
    btn1 = Button(tab_buttons, text=' Hesaplar  ', command=lambda: show_frame(frm2))
    btn1.grid(row=1, column=0)
    if hesapsayisi > 15:
        frm21 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm21)
        btn1 = Button(tab_buttons, text=' Hesaplar 2', command=lambda: show_frame(frm21))
        btn1.grid(row=1, column=1)

    if hesapsayisi > 30:
        frm22 = Frame(content,background="DarkSlateGray4",relief="groove")
        hesaplarTABlist.append(frm22)
        btn1 = Button(tab_buttons, text=' Hesaplar 3', command=lambda: show_frame(frm22))
        btn1.grid(row=1, column=2)

    if hesapsayisi > 45:
        frm23 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm23)
        btn1 = Button(tab_buttons, text=' Hesaplar 4', command=lambda: show_frame(frm23))
        btn1.grid(row=1, column=3)

    if hesapsayisi > 60:
        frm24 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm24)
        btn1 = Button(tab_buttons, text=' Hesaplar 5', command=lambda: show_frame(frm24))
        btn1.grid(row=1, column=4)

    if hesapsayisi > 75:
        frm25 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm25)
        btn1 = Button(tab_buttons, text=' Hesaplar 6', command=lambda: show_frame(frm25))
        btn1.grid(row=1, column=5)

    if hesapsayisi > 90:
        frm26 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm26)
        btn1 = Button(tab_buttons, text=' Hesaplar 7', command=lambda: show_frame(frm26))
        btn1.grid(row=1, column=6)

    if hesapsayisi > 105:
        frm27 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm27)
        btn1 = Button(tab_buttons, text=' Hesaplar 8', command=lambda: show_frame(frm27))
        btn1.grid(row=1, column=7)

    if hesapsayisi > 120:
        frm27 = Frame(content,background="DarkSlateGray4")
        hesaplarTABlist.append(frm27)
        btn1 = Button(tab_buttons, text=' Hesaplar 9', command=lambda: show_frame(frm27))
        btn1.grid(row=1, column=8)

    for k in hesaplarTABlist:
        k.place(relx=0, rely=0, relwidth=1, relheight=1)
    """Seçenekler TAB """

    frm3 = Frame(content,background="DarkSlateGray4")
    frm3.place(relx=0, rely=0, relwidth=1, relheight=1)
    btn1 = Button(tab_buttons, text='Seçenekler', command=lambda: show_frame(frm3))
    btn1.grid(row=2, column=0)
    

    arttiriciAl =data.get("arttiriciAl")
    askeregitList=data.get("askeregitList")
    beklemeCarpani=data.get("beklemeCarpani")
    diskaynakBonus=data.get("disKaynakBonus")
    ganimetYap=data.get("ganimetYap")
    gonderilcekList=data.get("gonderilcekList")
    gozcuList=data.get("gozcuList")
    hasatet=data.get("hasatEt")
    hazinetopla=data.get("hazineTopla")
    hesapSayisi=data.get("hesapSayisi")
    hizliTopla=data.get("hizliTopla")
    icKaynakBonus=data.get("icKaynakBonus")
    ifritList=data.get("ifritList")
    kaynakGonder=data.get("kaynakGonder")
    kaynakSeviye=data.get("kaynakSeviye")
    kvkKalkan=data.get("kvkKalkan")
    loncaTopla=data.get("loncaTopla")
    loncatechYap=data.get("loncatechYap")
    mail=data.get("mail")
    mesajTopla=data.get("mesajTopla")
    password=data.get("password")
    sifreList = data.get("sifre")
    tamponHasat=data.get("tamponHasat")
    username=data.get("username")
    hayvan=data.get("hayvan")
    kahraman = data.get("kahraman")
    dailyvip = data.get("dailyvip")

    gonderilcek = []
    askeregitcombo = []

    kaynak = []
    lonca = []
    mesaj_list = []
    lonca_topla_list = []
    havuz_list = []

    hasat_et_list = []
    hizli_topla_list = []
    tampon_hasat_list = []
    kvk_kalkan_list = []
    arttirici = []
    ganimet_kara = []
    ic_kaynak = []
    dis_kaynak= []
    gozculist = []
    ifritlist = []
    hayvanlist = []
    kahramanList = []
    viplist = []

    sayac = 0
    tur = 15
    kalan = hesapsayisi
    for tab in ayarlarTABlist:

        labelfarm = Label(tab,text="Farm",background="DarkSlateGray4", relief="groove",font='Helvetica 10 bold')
        labelfarm.grid(row = 0,column = 0,ipadx = 15,ipady = 5)


        labelresource = Label(tab,text="Source",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        labelresource.grid(row = 0,column = 1,ipadx = 15,ipady = 5)


        labelresource = Label(tab,text="Train Soldier",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        labelresource.grid(row = 0,column = 2,ipadx = 15,ipady = 5)


        labelresource = Label(tab,text="Pet Patrol",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        labelresource.grid(row = 0,column = 3,ipadx = 15,ipady = 5)


        labelresource = Label(tab,text="Scout",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        labelresource.grid(row = 0,column = 4,ipadx = 15,ipady = 5)


        labelresource = Label(tab,text="İfrit",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        labelresource.grid(row = 0,column = 5,ipadx = 25,ipady = 5)


        labelresource = Label(tab,text="Time",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        labelresource.grid(row = 0,column = 6,ipadx = 15,ipady = 5)
        if kalan > 15:
            tur = 15
            kalan -= 15
        else:
            tur = kalan
        
        for i in range(tur):
            
            try:
                secil = gonderilcekList[sayac]
            except:
                secil = "Yok"
            labelfarmcount = Label(tab,text = str(sayac+1),background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
            
            
            labelfarmcount.grid(row = i+1,column = 0,ipadx = 25,ipady = 5)
            combo = Combobox(tab,values=["Yok","Grain","Lumber","Iron","Quartz","Gold"],background="DarkSlateGray4",state="readonly",width=2)
            combo.grid(row = i +1,column =  1,ipadx = 25,ipady = 5)
            gonderilcek.append(combo)

            if secil == "Yok" or secil == "":
                combo.set("--")
            elif secil == "Bugday" or secil == "Grain":
                combo.set("Grain")
            elif secil == "Odun" or secil == "Lumber":
                combo.set("Lumber")
            elif secil == "Demir" or secil == "Iron":
                combo.set("Iron")
            elif secil == "Kuvars" or secil == "Quartz":
                combo.set("Quartz")
            elif secil == "Altin" or secil == "Gold":
                combo.set("Gold")
        

            try:
                secil = askeregitList[sayac]
            except:
                secil="Yok"
            
            combo = Combobox(tab,values=["Yok","Max","Grain Car"],background="DarkSlateGray4",state="readonly",width=4)
            combo.grid(row = i +1,column =  2,ipadx = 25,ipady = 5)
            askeregitcombo.append(combo)
            if secil == "Yok" or secil == "" or secil == "--":
                combo.set("--")

            elif secil == "Max":
                combo.set("Max")

            elif secil == "Tahil Arabasi" or secil == "Grain Car":
                combo.set("Grain Car")
            


            #-----------------------------
            try:
                secil = hayvan[sayac]
            except:
                secil = "Yok"
            combo = Combobox(tab,values=["Yok","Ofkeli Kaplan","Grifon","Gergedan","Kaplan","Aslan","Kartal","Bozkurt","Panter","Ayi","Fil","Bufalo","Kangal"],background="DarkSlateGray4",state="readonly",width=2)
            combo.grid(row = i +1,column =  3,ipadx = 25,ipady = 5)
            hayvanlist.append(combo)

            if secil == "Yok" or secil == "":
                combo.set("--")
            elif secil == "Ofkeli Kaplan" or secil == "Angry Tiger":
                combo.set("Ofkeli Kaplan")
            elif secil == "Grifon" or secil == "Griffin":
                combo.set("Grifon")
            elif secil == "Gergedan" or secil == "Rhinoceros":
                combo.set("Gergedan")
            elif secil == "Kaplan" or secil == "Tiger":
                combo.set("Kaplan")
            elif secil == "Aslan" or secil == "Lion":
                combo.set("Aslan")
            elif secil == "Kartal" or secil == "Eagle":
                combo.set("Kartal")
            elif secil == "Bozkurt" or secil == "Gray Wolf":
                combo.set("Bozkurt")
            elif secil == "Panter" or secil == "Panther":
                combo.set("Panter")
            elif secil == "Ayi" or secil == "Bear":
                combo.set("Ayi")
            elif secil == "Fil" or secil == "Elephant":
                combo.set("Fil")
            elif secil == "Bufalo" or secil == "Buffalo":
                combo.set("Bufalo")
            elif secil == "Kangal" or secil == "Kangal Dog":
                combo.set("Kangal")
            
            #-----------------------------
        
            combo = Checkbutton(tab,command = lambda g = sayac:reverseBool(gozculist,g),background="DarkSlateGray4",activebackground="CadetBlue4", borderwidth=2, relief="groove")
            combo.grid(row = i +1,column = 4,ipadx = 25,ipady = 5)
            try:
                x = gozcuList[sayac]
            except:
                x = ""
            
            if x == True:
                combo.select()
                gozcu = True
            else:
                gozcu = False
                combo.deselect()
            gozculist.append(gozcu)


            combo = Checkbutton(tab,command = lambda ifr = sayac:reverseBool(ifritlist,ifr),background="DarkSlateGray4",activebackground="CadetBlue4", borderwidth=2, relief="groove")
            combo.grid(row = i +1,column = 5,ipadx = 25,ipady = 5)
            try:
                x = ifritList[sayac]
            except:
                x = "Yok"
            
            if x == True:
                combo.select()
                ifrit = True
            else:
                ifrit = False
                combo.deselect()
            ifritlist.append(ifrit)
            sayac += 1
    

    combo = Checkbutton(frm3,text = "Harvest",command = lambda:reverseBool(hasat_et_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if hasatet == True:
        
        hasat = True
        combo.select()
    else:
        hasat = False
        combo.deselect()
    hasat_et_list.append(hasat)


    combo = Checkbutton(frm3,text = "Quick Collect",command = lambda:reverseBool(hizli_topla_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if hizliTopla == True:
        
        hizli = True
        combo.select()
    else:
        hizli = False
        combo.deselect()
    hizli_topla_list.append(hizli)



    combo = Checkbutton(frm3,text = "Bumper Harvest",command = lambda:reverseBool(tampon_hasat_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 2,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if tamponHasat == True:
        
        tampon = True
        combo.select()
    else:
        tampon = False
        combo.deselect()
    tampon_hasat_list.append(tampon)


    combo = Checkbutton(frm3,text = "Collect MailBox",command = lambda:reverseBool(mesaj_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if mesajTopla == True:
        
        mesaj = True
        combo.select()
    else:
        mesaj = False
        combo.deselect()
    mesaj_list.append(mesaj)


    combo = Checkbutton(frm3,text = "Collect Alliance Box",command = lambda:reverseBool(lonca_topla_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if loncaTopla == True:
        
        topla = True
        combo.select()
    else:
        topla = False
        combo.deselect()
    lonca_topla_list.append(topla)

    combo = Checkbutton(frm3,text = "Treasue Pool",command = lambda:reverseBool(havuz_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 2,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if hazinetopla == True:
        
        havuz = True
        combo.select()
    else:
        havuz = False
        combo.deselect()
    havuz_list.append(havuz)

    

    combo = Checkbutton(frm3,text = "Resource Aid",command = lambda:reverseBool(kaynak,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 3,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if kaynakGonder == True:

        kaynak_gonder = True
        combo.select()
    else:
        kaynak_gonder = False
        combo.deselect()
    kaynak.append(kaynak_gonder)


    combo = Checkbutton(frm3,text = "Technology Donation",command = lambda:reverseBool(lonca,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if loncatechYap == True:

        loncatech_yap = True
        combo.select()
    else:
        loncatech_yap = False
        combo.deselect()
    lonca.append(loncatech_yap)


    combo = Checkbutton(frm3,text = "Loot Caravan",command = lambda:reverseBool(ganimet_kara,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if ganimetYap == True:

        ganimet_yap = True
        combo.select()
    else:
        ganimet_yap = False
        combo.deselect()
    ganimet_kara.append(ganimet_yap)


    combo = Checkbutton(frm3,text = "Water Mill",command = lambda:reverseBool(ic_kaynak,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 2,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if icKaynakBonus == True:

        icyap = True
        combo.select()
    else:
        icyap = False
        combo.deselect()
    ic_kaynak.append(icyap)



    combo = Checkbutton(frm3,text = "Collecting Bonus",command = lambda:reverseBool(dis_kaynak,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 3,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if diskaynakBonus == True:

        disyap = True
        combo.select()
    else:
        disyap = False
        combo.deselect()
    dis_kaynak.append(disyap)

    combo = Checkbutton(frm3,text = "KVK Shield",command = lambda:reverseBool(kvk_kalkan_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 3,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if kvkKalkan == True:
        kalkan = True
        combo.select()
    else:
        kalkan = False
        combo.deselect()
    kvk_kalkan_list.append(kalkan)


    combo = Checkbutton(frm3,text = "Kahraman Salonu",command = lambda:reverseBool(kahramanList,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 3,ipadx = 15,ipady = 5,sticky="w")
    if kahraman == True:
        salonyap = True
        combo.select()
    else:
        salonyap = False
        combo.deselect()
    kahramanList.append(salonyap)


    combo = Checkbutton(frm3,text = "Günlük VIP",command = lambda:reverseBool(viplist,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 3,ipadx = 15,ipady = 5,sticky="w")
    if dailyvip == True:
        dailyvipbool = True
        combo.select()
    else:
        dailyvipbool = False
        combo.deselect()
    viplist.append(dailyvipbool)

    global dictbool
    dictbool = {}
    value = []
    if arttiriciAl[0]:
        value.append("✅Grain")
        dictbool["Grain"] = True
    else:
        value.append("Grain")
        dictbool["Grain"] = False

    if arttiriciAl[1]:
        value.append("✅Lumber")
        dictbool["Lumber"] = True
    else:
        value.append("Lumber")
        dictbool["Lumber"] = False
    
    if arttiriciAl[2]:
        value.append("✅Iron")
        dictbool["Iron"] = True
    else:
        value.append("Iron")
        dictbool["Iron"] = False
    
    if arttiriciAl[3]:
        value.append("✅Quartz")
        dictbool["Quartz"] = True
    else:
        value.append("Quartz")
        dictbool["Quartz"] = False

    global comboarttirici
    comboarttirici = Combobox(frm3,values=value,background="DarkSlateGray4",state="readonly")
    comboarttirici.bind("<<ComboboxSelected>>",comboboxchange)
    comboarttirici.grid(row = 4,column = 0,ipadx = 15,ipady = 5,sticky="w")
    comboarttirici.set("Water Mill")

    
    label_kaynakseviye = Label(frm3,text="Resource Level",background="DarkSlateGray4",font='Helvetica 10 bold')
    label_kaynakseviye.grid(row = 5,column = 0,ipadx = 15,ipady = 5,sticky="w")

    slide_kaynak = Scale(frm3,from_=1,to=6,orient=HORIZONTAL,background="DarkSlateGray4",activebackground="CadetBlue4", bd="0px", relief=FLAT)
    slide_kaynak.grid(row = 5,column = 1,ipadx = 15,ipady = 5,pady=20,sticky="w")
    try:
        if(kaynakSeviye !=""):
            slide_kaynak.set(int(kaynakSeviye))
        else:
            slide_kaynak.set(3)
    except:
        slide_kaynak.set(3)
    label_kaynakseviye = Label(frm3,text="Speed",background="DarkSlateGray4",font='Helvetica 10 bold')
    label_kaynakseviye.grid(row = 6,column = 0,ipadx = 15,ipady = 5,sticky="w")

    slide_carpan = Scale(frm3,from_=1,to=5,orient=HORIZONTAL,background="DarkSlateGray4",activebackground="CadetBlue4", bd="0px", relief=FLAT)
    slide_carpan.grid(row = 6,column = 1,ipadx = 15,ipady = 5,pady=20,sticky="w")
    try:
        if(beklemeCarpani !=""):
            slide_carpan.set(int(beklemeCarpani))
        else:
            slide_carpan.set(3)
    except:
        slide_carpan.set(3)
    
    global btn
    
   
    if hesapsayisi >=6:
        window.geometry('750x' + str(230+30*17))
    else:
        window.geometry('750x' + str(230+30*17))

    
    
    entry_mail = []
    entry_password = []

    sayac = 0
    tur = 15
    kalan = hesapsayisi
    for frame in hesaplarTABlist:
        
        label = Label(frame,text="Farms",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
        label.grid(row = 0,column = 0,padx = 20,pady=5)

        label = Label(frame,text="Mail",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
        label.grid(row = 0,column = 1,padx = 20,pady=5)

        label = Label(frame,text="Password",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
        label.grid(row = 0,column = 2,padx = 20,pady=5)

        if kalan > 15:
            tur = 15
            kalan -= 15
        else:
            tur = kalan
        for i in range(tur):
            
            
            labelhesapsayisi = Label(frame,text="Farm {hesap}".format(hesap=sayac+1),background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
            labelhesapsayisi.grid(row = i+1,column = 0,padx = 5,pady=5)
            
            hesapentry = Entry(frame,background="antiquewhite3",justify = CENTER, borderwidth=2, relief="groove",width= 30)
            hesapentry.grid(row = i+1,column = 1,padx = 5,pady=5)
            try:
                hesapentry.insert(0,mail[sayac])
            except:
                hesapentry.insert(0,"")
            entry_mail.append(hesapentry)

            sifreentry = Entry(frame,background="antiquewhite3",justify = CENTER, borderwidth=2, relief="groove",width= 20)
            sifreentry.grid(row = i+1,column = 2,padx = 5,pady=5)
            try:
                sifreentry.insert(0,sifreList[sayac])
            except:
                sifreentry.insert(0,"")
            entry_password.append(sifreentry)
            sayac += 1


    show_frame(frm)

    btn = Button(text="Başla", height=2, width=10, background="MediumSpringGreen",command=lambda: basla(entry_mail,entry_password,viplist,kahramanList,hayvanlist,ifritlist,arttirici,kvk_kalkan_list,askeregitcombo,hasat_et_list,tampon_hasat_list,hizli_topla_list,havuz_list,lonca_topla_list,mesaj_list,gozculist,ic_kaynak,dis_kaynak,btn,slide_carpan,slide_kaynak,gonderilcek,hesapsayisi,kaynak,lonca,ganimet_kara,frm,nickname,password),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised",)
    btn.place(x=575,y = 405)

def comboboxchange(event):
    secilen = comboarttirici.get()
    
    
    secilen = secilen.replace("✅","")
    dictbool[secilen] = not dictbool.get(secilen)
    value = []
    if dictbool.get("Grain")== True:
        value.append("✅Grain")
    else:
        value.append("Grain")

    if dictbool.get("Lumber")== True:
        value.append("✅Lumber")
    else:
        value.append("Lumber")
    if dictbool.get("Iron")== True:
        value.append("✅Iron")
    else:
        value.append("Iron")
    if dictbool.get("Quartz")== True:
        value.append("✅Quartz")
    else:
        value.append("Quartz")
    
    print(dictbool)
    comboarttirici.config(values=value)
    comboarttirici.set("Değirmen Arttırıcı Al")

def basla(entry_mail,entry_password,viplist,kahraman,hayvan,ifritlist,arttirici,kvk_kalkan_list,askeregitcombo,hasat_et_list,tampon_hasat_list,hizli_topla_list,havuz_list,lonca_topla_list,mesaj_list,gozculist,ic_kaynak,dis_kaynak,btn,slide_carpani,slide_kaynak,gonderilcek,hesapsayisi,kaynak,lonca,ganimet_kara,frm,nickname,password):
    gonderler = []
    askerler= []
    gozculer = []
    ifritler = []
    mailler = []
    sifreler = []
    hayvanlist = []
    degirmenal = [False,False,False,False]
    if dictbool.get("Grain")== True:
        degirmenal[0] = True
    if dictbool.get("Lumber")== True:
        degirmenal[1] = True
    if dictbool.get("Iron")== True:
        degirmenal[2] = True
    if dictbool.get("Quartz")== True:
        degirmenal[3] = True
   
    for i in range(hesapsayisi):
        gonderler.append(gonderilcek[i].get())
    
    for i in range(hesapsayisi):
        askerler.append(askeregitcombo[i].get())
    
    for i in range(hesapsayisi):
        hayvanlist.append(hayvan[i].get())

    for i in range(hesapsayisi):
        gozculer.append(gozculist[i])
    
    for i in range(hesapsayisi):
        ifritler.append(ifritlist[i])

    for i in range(hesapsayisi):
        mailler.append(entry_mail[i].get())
    for i in range(hesapsayisi):
        sifreler.append(entry_password[i].get())

    data = {
        'arttiriciAl': degirmenal,
        'askeregitList': askerler,
        'beklemeCarpani': slide_carpani.get(),
        'disKaynakBonus': dis_kaynak[0],
        'ganimetYap': ganimet_kara[0],
        'gonderilcekList': gonderler,
        'gozcuList': gozculer,
        'hasatEt': hasat_et_list[0],
        'hazineTopla': havuz_list[0],
        'hesapSayisi': hesapsayisi,
        'hizliTopla': hizli_topla_list[0],
        'icKaynakBonus': ic_kaynak[0],
        'ifritList': ifritler,
        'kaynakGonder': kaynak[0],
        'kaynakSeviye': slide_kaynak.get(),
        'kvkKalkan': kvk_kalkan_list[0],
        'loncaTopla': lonca_topla_list[0],
        'loncatechYap':lonca[0] ,
        'mail': mailler,
        'mesajTopla': mesaj_list[0],
        'password': password,
        'sifre': sifreler,
        'tamponHasat': tampon_hasat_list[0],
        'username': nickname,
        "hayvan": hayvanlist,
        "kahraman": kahraman[0],
        "dailyvip": viplist[0],
    }



    try:
        r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/edit",json=data, timeout=(15, 30))
        url = "https://raw.githubusercontent.com/dapoetika/PashaBotUpdate/refs/heads/main/game.py"
        response = requests.get(url)
        response.raise_for_status()
        
        kod = response.text

        # exec ile çalıştırılacak ortam (fonksiyonlar buraya yüklenecek)
        ortam = {}

        # Kodları ortam içine çalıştır
        exec(kod, ortam)

        ortam["trr"](btn,ayarlarTABlist,data)
        #import game
        #game.trr(btn,ayarlarTABlist,data)
    except Exception as e:
        print(f"Hata oluştu: {e}")


def label_guncelle(lbl, text):
    # Tkinter thread-safe label güncelleme
    lbl.after(0, lambda: lbl.config(text=text))


def dosyakontrol(lblkontrol,window):
    # GitHub bilgileri
    GITHUB_USER = "dapoetika"
    REPO_NAME = "PashaBotUpdate"
    BRANCH = "main"
    FOLDER = "images"

    # Dosya listesi URL
    url = "https://raw.githubusercontent.com/dapoetika/PashaBotUpdate/refs/heads/main/images/aafiles"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        remote_files = response.text.split(",")
    except Exception as e:
        label_guncelle(lblkontrol, f"Dosya kontrolü başarısız: {e}")
        return

    # Klasörler
    LOCAL_FOLDER = "images"
    DATADIR = "data"

    os.makedirs(LOCAL_FOLDER, exist_ok=True)
    os.makedirs(DATADIR, exist_ok=True)

    # Gerekli txt dosyaları
    for fname in ["data.txt","logs.txt"]:
        fpath = os.path.join(DATADIR, fname)
        if not os.path.exists(fpath):
            open(fpath, "w", encoding="utf-8").close()

    # Dosya kontrol / indirme
    for x in remote_files:
        filename = x.strip()
        if not filename:
            continue

        local_path = os.path.join(LOCAL_FOLDER, filename)

        if not os.path.exists(local_path):
            label_guncelle(lblkontrol, f"[+] Eksik: {filename} — indiriliyor...")

            raw_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{FOLDER}/{filename}"

            try:
                r = requests.get(raw_url, timeout=10)
                r.raise_for_status()
                with open(local_path, "wb") as f:
                    f.write(r.content)
            except Exception as e:
                label_guncelle(lblkontrol, f"[!] {filename} indirilemedi: {e}")
        else:
            label_guncelle(lblkontrol, f"[=] Zaten var: {filename}")

    label_guncelle(lblkontrol, "Dosya kontrolü tamamlandı ✔")
    r = login()
    if r.status_code == 200:
        sonrakihesapgir(window, r)
    else:
        ilkhesapgir(window)


def main():
    
    window = Tk()
    window.title("PashaBot")

    try:
        window.iconbitmap("./images/favicon.ico")
    except:
        pass

    window.geometry("700x350")
    window.configure(background="DarkSlateGray4", pady=20)

    lbl = Label(
        window,
        text="PashaBot",
        font=("Helvetica", 30, "bold"),
        background="DarkSlateGray4"
    )
    lbl.pack()

    lblkontrol = Label(
        window,
        text="Dosyalar kontrol ediliyor...",
        font=("Helvetica", 14),
        background="DarkSlateGray4"
    )
    lblkontrol.pack(pady=10)

    # Thread BAŞLAT (DOĞRU ŞEKİLDE)
    Thread(
        target=dosyakontrol,
        args=(lblkontrol,window,),
        daemon=True
    ).start()

    window.mainloop()


if __name__ == "__main__":
    main()
