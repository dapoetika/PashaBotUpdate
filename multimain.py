#sa
from tkinter.ttk import *
from tkinter import *

import bs4
import requests 

def hesapgir(window):
   

 
    vericek = open("./data/data.txt")
    r = requests.get("https://nebulousalih620.wixsite.com/muhtesemveritabani")
    soup = bs4.BeautifulSoup(r.content,"html.parser")

    kkkk = soup.find_all("h6",{"class" : "wixui-rich-text__text"})
    kkkk = str(kkkk)
    aa = vericek.readline()
    bb = vericek.readline()
    aa = aa[0:-1]
    bb = bb[0:-1]
   
    if "%" + aa + " ; " + bb + "%" in kkkk:

        #sonraki girişler

        frame2 = Frame(window,height = 100,width = 400,background= "DarkSlateGray4", borderwidth=2, relief="groove")
        frame2.place(x=105,y = 115)
        labelhesapsayisi = Label(frame2,text="Hesap Sayısı",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
        labelhesapsayisi.grid(row = 0,column = 0,padx = 20)
        hesapentry = Entry(frame2,background="antiquewhite3",justify = CENTER)
        hesapentry.grid(row = 0,column = 3)

        defaulthesap = vericek.readline()
        hesapentry.insert(0,defaulthesap)

        btn = Button(text="Start", height=2, width=10, background="MediumSpringGreen",command=lambda: otekigecis(window,int(hesapentry.get()),aa,bb,labelhesapsayisi,hesapentry,btn),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised")
        btn.place(x=500,y = 250)
        
    else:
        # ilk giriş

        frame2 = Frame(window,height = 100,width = 400,background = "DarkSlateGray4")
        frame2.place(x=105,y = 115)
        
        nicknamelabel = Label(frame2,text="Kullanıcı Adı",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
        nicknamelabel.grid(row = 0,column = 0)
        nickentry = Entry(frame2,background="antiquewhite3")
        nickentry.grid(row = 0,column = 1)


        """defaultnick = vericek.readline()
        defaultnick = defaultnick[0:-1]
        nickentry.insert(0,defaultnick)"""



        passwordlabel = Label(frame2,text="Parola",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
        passwordlabel.grid(row = 1,column = 0,pady = 30)
        passwordentry = Entry(frame2,background="antiquewhite3",show = "*")
        passwordentry.grid(row = 1,column = 1,pady = 30)

        """defaultpass = vericek.readline()
        defaultpass = defaultpass[0:-1]
        passwordentry.insert(0,defaultpass)"""


        
        labelhesapsayisi = Label(frame2,text="Hesap Sayısı",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT)
        labelhesapsayisi.grid(row = 2,column = 0,padx = 20)
        hesapentry = Entry(frame2,background="antiquewhite3",justify = CENTER)
        hesapentry.grid(row = 2,column = 1)

        defaulthesap = vericek.readline()
        hesapentry.insert(0,defaulthesap)


        buttonok = Button(text="Başla", height=2, width=10, background="MediumSpringGreen",command=lambda: gecis(window,hesapentry,passwordentry,nickentry,labelhesapsayisi,buttonok,nicknamelabel,passwordlabel,kkkk),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised")
        buttonok.place(x=500,y = 250)



        

def otekigecis(window,hesapsayisi,nickname,password,labelhesapsayisi,hesapentry,btn):
    btn.destroy()
    labelhesapsayisi.destroy()
    hesapentry.destroy()
    tablegiris(window,hesapsayisi,nickname,password) 

def gecis(window,hesapentry,passwordentry,nickentry,labelhesapsayisi,buttonok,nickamelabel,passwordlabel,kkkk):

    hesapsayisi = hesapentry.get()
    nickname = nickentry.get()
    password = passwordentry.get()



    hesapentry.destroy()
    passwordentry.destroy()
    nickentry.destroy()

    labelhesapsayisi.destroy()
    buttonok.destroy()
    nickamelabel.destroy()
    passwordlabel.destroy()


    if "%" + nickname + " ; " + password + "%" in kkkk:
        
        tablegiris(window,hesapsayisi,nickname,password) 
        
    else:
        hesapgir(window)
    
def reverseBool(hangiListe,m):
    hangiListe[m] = not hangiListe[m]
    
def tablegiris(window,hesapsayisi,nickname,password):
    global frm
    hesapsayisi = int(hesapsayisi)

    style = Style()
    style.configure('custom.TNotebook', background="DarkSlateGray4", borderwidth=0,margin=0, foreground="Black", padding=[10, 0],bordercolor = "DarkSlateGray4")
    style.configure('custom.TNotebook.Tab', background="DarkSlateGray4", foreground="Black", padding=[10, 0],bordercolor = "Red")


    notebook = Notebook(window,style='custom.TNotebook')
    notebook.grid()
   
    frm = Frame(notebook,height = (30*(hesapsayisi-2))+65,width = 750,background= "DarkSlateGray4",  relief="groove")
    frm.place()

    frm2 = Frame(notebook,height = (30*(hesapsayisi-2))+65,width = 750,background= "DarkSlateGray4", relief="groove")
    frm2.place()

    frm3 = Frame(notebook,height = (30*(hesapsayisi-2))+65,width = 750,background= "DarkSlateGray4", relief="groove")
    frm3.place()

    notebook.add(frm, text="Başlat",padding=0)
    notebook.add(frm2, text="Hesaplar",padding=0)
    notebook.add(frm3, text="Seçenekler",padding=0)

    labelfarm = Label(frm,text="Farm",background="DarkSlateGray4", relief="groove",font='Helvetica 10 bold')
    #labelfarm.place(x=30,y=100,width=60,height=20)
    labelfarm.grid(row = 0,column = 0,ipadx = 15,ipady = 5)
    
    
    
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
    
    ganimet_kara = []
    ic_kaynak = []
    dis_kaynak= []
    gozculist = []
    data = open("./data/data.txt")
    data.readline()
    data.readline()
    data.readline()

    

    k = data.readline()
    l = data.readline()
    g = data.readline()
    ic = data.readline()
    dis = data.readline()
    havuz_topla =  data.readline()
    lonca_topla =  data.readline()
    mesaj_topla =  data.readline()
    

    hasat_et = data.readline()
    hizli_topla = data.readline()
    tampon_hasat = data.readline()

    kaynak_seviye = data.readline()
    hiz_carpan = data.readline()


    labelresource = Label(frm,text="Kaynak",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
    #labelresource.place(x=90,y = 100,width=60,height=20)
    labelresource.grid(row = 0,column = 1,ipadx = 15,ipady = 5)


    labelresource = Label(frm,text="Asker Eğit",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
    #labelresource.place(x=90,y = 100,width=60,height=20)
    labelresource.grid(row = 0,column = 2,ipadx = 15,ipady = 5)


    labelresource = Label(frm,text="Gözcü",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
    #labelresource.place(x=90,y = 100,width=60,height=20)
    labelresource.grid(row = 0,column = 3,ipadx = 15,ipady = 5)


    labelresource = Label(frm,text="Saat",background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
    #labelresource.place(x=90,y = 100,width=60,height=20)
    labelresource.grid(row = 0,column = 4,ipadx = 15,ipady = 5)
    for i in range(hesapsayisi):
        
        secil = data.readline().rstrip()

        labelfarmcount = Label(frm,text = str(i+1),background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
        #labelfarmcount.place(x=30,y = 120+30*i,width=60,height=25)
        labelfarmcount.grid(row = i +1,column = 0,ipadx = 25,ipady = 5)





        combo = Combobox(frm,values=["Yok","Bugday","Odun","Demir","Kuvars"],background="DarkSlateGray4",state="readonly",width=2)
        combo.grid(row = i +1,column =  1,ipadx = 25,ipady = 5)
        gonderilcek.append(combo)
        
        if secil == "Yok" or secil == "":
            combo.set("--")
        elif secil == "Bugday":
            combo.set("Bugday")
        elif secil == "Odun":
            combo.set("Odun")
        elif secil == "Demir":
            combo.set("Demir")
        elif secil == "Kuvars":
            combo.set("Kuvars")

    for i in range(hesapsayisi):
        
        secil = data.readline().rstrip()

        combo = Combobox(frm,values=["Yok","Max","Tahil Arabasi"],background="DarkSlateGray4",state="readonly",width=4)
        combo.grid(row = i +1,column =  2,ipadx = 25,ipady = 5)
        askeregitcombo.append(combo)
        if secil == "Yok" or secil == "":
            combo.set("--")

        elif secil == "Max":
            combo.set("Max")

        elif secil == "Tahil Arabasi":
            combo.set("Tahil Arabasi")
        

    for i in range(hesapsayisi):
        combo = Checkbutton(frm,command = lambda g = i:reverseBool(gozculist,g),background="DarkSlateGray4",activebackground="CadetBlue4", borderwidth=2, relief="groove")
        combo.grid(row = i +1,column = 3,ipadx = 25,ipady = 5)
        x = data.readline()
        if x == "True\n":
            combo.select()
            gozcu = True
        else:
            gozcu = False
            combo.deselect()
        gozculist.append(gozcu)

   

    combo = Checkbutton(frm3,text = "Hasat Et",command = lambda:reverseBool(hasat_et_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if hasat_et == "True\n":
        
        hasat = True
        combo.select()
    else:
        hasat = False
        combo.deselect()
    hasat_et_list.append(hasat)


    combo = Checkbutton(frm3,text = "Hızlı Topla",command = lambda:reverseBool(hizli_topla_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if hizli_topla == "True\n":
        
        hizli = True
        combo.select()
    else:
        hizli = False
        combo.deselect()
    hizli_topla_list.append(hizli)



    combo = Checkbutton(frm3,text = "Tampon Hasat",command = lambda:reverseBool(tampon_hasat_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 2,column = 2,ipadx = 15,ipady = 5,sticky="w")
    if tampon_hasat == "True\n":
        
        tampon = True
        combo.select()
    else:
        tampon = False
        combo.deselect()
    tampon_hasat_list.append(tampon)


    combo = Checkbutton(frm3,text = "Mesaj Topla",command = lambda:reverseBool(mesaj_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if mesaj_topla == "True\n":
        
        mesaj = True
        combo.select()
    else:
        mesaj = False
        combo.deselect()
    mesaj_list.append(mesaj)


    combo = Checkbutton(frm3,text = "Lonca Topla",command = lambda:reverseBool(lonca_topla_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if lonca_topla == "True\n":
        
        topla = True
        combo.select()
    else:
        topla = False
        combo.deselect()
    lonca_topla_list.append(topla)

    combo = Checkbutton(frm3,text = "Ganimet Havuzu",command = lambda:reverseBool(havuz_list,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 2,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if havuz_topla == "True\n":
        
        havuz = True
        combo.select()
    else:
        havuz = False
        combo.deselect()
    havuz_list.append(havuz)

    

    combo = Checkbutton(frm3,text = "Kaynak Yardımı",command = lambda:reverseBool(kaynak,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 3,column = 0,ipadx = 15,ipady = 5,sticky="w")
    if k == "True\n":

        kaynak_gonder = True
        combo.select()
    else:
        kaynak_gonder = False
        combo.deselect()
    kaynak.append(kaynak_gonder)


    combo = Checkbutton(frm3,text = "Lonca Bağışı",command = lambda:reverseBool(lonca,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 0,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if l == "True\n":

        loncatech_yap = True
        combo.select()
    else:
        loncatech_yap = False
        combo.deselect()
    lonca.append(loncatech_yap)


    combo = Checkbutton(frm3,text = "Ganimet Karavanı",command = lambda:reverseBool(ganimet_kara,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 1,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if g == "True\n":

        ganimet_yap = True
        combo.select()
    else:
        ganimet_yap = False
        combo.deselect()
    ganimet_kara.append(ganimet_yap)


    combo = Checkbutton(frm3,text = "İç Kaynak Bonusu",command = lambda:reverseBool(ic_kaynak,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 2,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if ic == "True\n":

        icyap = True
        combo.select()
    else:
        icyap = False
        combo.deselect()
    ic_kaynak.append(icyap)


    combo = Checkbutton(frm3,text = "Dış Kaynak Bonusu",command = lambda:reverseBool(dis_kaynak,0),background="DarkSlateGray4",activebackground="CadetBlue4")
    combo.grid(row = 3,column = 1,ipadx = 15,ipady = 5,sticky="w")
    if dis == "True\n":

        disyap = True
        combo.select()
    else:
        disyap = False
        combo.deselect()
    dis_kaynak.append(disyap)

 


    
    
    label_kaynakseviye = Label(frm3,text="Kaynak Seviyesi",background="DarkSlateGray4",font='Helvetica 10 bold')
    label_kaynakseviye.grid(row = 4,column = 0,ipadx = 15,ipady = 5,sticky="w")

    slide_kaynak = Scale(frm3,from_=1,to=6,orient=HORIZONTAL,background="DarkSlateGray4",activebackground="CadetBlue4", bd="0px", relief=FLAT)
    slide_kaynak.grid(row = 4,column = 1,ipadx = 15,ipady = 5,pady=20,sticky="w")
    if(kaynak_seviye !=""):
   
        slide_kaynak.set(int(kaynak_seviye))
    else:
        slide_kaynak.set(3)


    label_kaynakseviye = Label(frm3,text="Hız",background="DarkSlateGray4",font='Helvetica 10 bold')
    label_kaynakseviye.grid(row = 5,column = 0,ipadx = 15,ipady = 5,sticky="w")

    slide_carpan = Scale(frm3,from_=1,to=5,orient=HORIZONTAL,background="DarkSlateGray4",activebackground="CadetBlue4", bd="0px", relief=FLAT)
    slide_carpan.grid(row = 5,column = 1,ipadx = 15,ipady = 5,pady=20,sticky="w")
    if(hiz_carpan !=""):
   
        slide_carpan.set(int(hiz_carpan))
    else:
        slide_carpan.set(3)

    
    global btn
    btn = Button(text="Başla", height=2, width=10, background="MediumSpringGreen",command=lambda: basla(askeregitcombo,hasat_et_list,tampon_hasat_list,hizli_topla_list,havuz_list,lonca_topla_list,mesaj_list,gozculist,ic_kaynak,dis_kaynak,btn,slide_carpan,slide_kaynak,gonderilcek,hesapsayisi,kaynak,lonca,ganimet_kara,frm,nickname,password),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised",)
    btn.place(x=575,y = 405)

    
    

   
    if hesapsayisi >=6:
        window.geometry('750x' + str(230+30*hesapsayisi))
    else:
        window.geometry('750x' + str(350))

    f = open("./data/acc.txt")

    
    entry_mail = []
    entry_password = []

    

    
    label = Label(frm2,text="Farmlar",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
    label.grid(row = 0,column = 0,padx = 20,pady=5)

    label = Label(frm2,text="Mail",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
    label.grid(row = 0,column = 1,padx = 20,pady=5)

    label = Label(frm2,text="Sifre",background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
    label.grid(row = 0,column = 2,padx = 20,pady=5)

    for i in range(hesapsayisi):
        
        
        labelhesapsayisi = Label(frm2,text="Farm {hesap}".format(hesap = i),background="DarkSlateGray4",font='Helvetica 10 bold',justify = LEFT, borderwidth=2, relief="groove")
        labelhesapsayisi.grid(row = i+1,column = 0,padx = 5,pady=5)

        hesapentry = Entry(frm2,background="antiquewhite3",justify = CENTER, borderwidth=2, relief="groove",width= 30)
        hesapentry.grid(row = i+1,column = 1,padx = 5,pady=5)
        hesapentry.insert(0,f.readline().rstrip())
        entry_mail.append(hesapentry)

        sifreentry = Entry(frm2,background="antiquewhite3",justify = CENTER, borderwidth=2, relief="groove",width= 20)
        sifreentry.grid(row = i+1,column = 2,padx = 5,pady=5)
        sifreentry.insert(0,f.readline().rstrip())
        entry_password.append(sifreentry)

    buttonok = Button(frm2,text="Kaydet", height=2, width=10, background="MediumSpringGreen",command=lambda: childsave(entry_mail,entry_password),activebackground="MediumSeaGreen",font=("Helvetica",10,"bold"), borderwidth=2, relief="raised")
    buttonok.grid(row = 1,column = 3)

    f.close()
    

def basla(askeregitcombo,hasat_et_list,tampon_hasat_list,hizli_topla_list,havuz_list,lonca_topla_list,mesaj_list,gozculist,ic_kaynak,dis_kaynak,btn,slide_carpani,slide_kaynak,gonderilcek,hesapsayisi,kaynak,lonca,ganimet_kara,frm,nickname,password):
    
    data = open("./data/data.txt",W)
    data.write(str(nickname).rstrip()+"\n")
    data.write(str(password).rstrip()+"\n")
    data.write(str(hesapsayisi).rstrip()+"\n")
    data.write(str(kaynak[0]).rstrip()+"\n")
    data.write(str(lonca[0]).rstrip()+"\n")
    data.write(str(ganimet_kara[0]).rstrip()+"\n")
    data.write(str(ic_kaynak[0]).rstrip()+"\n")
    data.write(str(dis_kaynak[0]).rstrip()+"\n")

    data.write(str(havuz_list[0]).rstrip()+"\n")
    data.write(str(lonca_topla_list[0]).rstrip()+"\n")
    data.write(str(mesaj_list[0]).rstrip()+"\n")

    data.write(str(hasat_et_list[0]).rstrip()+"\n")
    data.write(str(hizli_topla_list[0]).rstrip()+"\n")
    data.write(str(tampon_hasat_list[0]).rstrip()+"\n")

    data.write(str(slide_kaynak.get()).rstrip()+"\n")
    data.write(str(slide_carpani.get()).rstrip()+"\n")

    for i in range(hesapsayisi):
        data.write(str(gonderilcek[i].get())+"\n")
    
    for i in range(hesapsayisi):
        data.write(str(askeregitcombo[i].get())+"\n")

    for i in range(hesapsayisi):
        data.write(str(gozculist[i])+"\n")
    
    url = "https://raw.githubusercontent.com/dapoetika/PashaBotUpdate/refs/heads/main/game.py"

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        kod = response.text

        # exec ile çalıştırılacak ortam (fonksiyonlar buraya yüklenecek)
        ortam = {}

        # Kodları ortam içine çalıştır
        exec(kod, ortam)

        ortam["trr"](btn,frm)
        

    except Exception as e:
        print(f"Hata oluştu: {e}")

 

def childsave(entry_mail,entry_password):
    f = open("./data/acc.txt", "w")
    for i in range(len(entry_mail)):
        f.write(str(entry_mail[i].get()).rstrip()+"\n")
        f.write(str(entry_password[i].get()).rstrip()+"\n")

    f.close()


def main():
    
    window = Tk()
    
    
    window.title("PashaBot")
    window.iconbitmap("./images/favicon.ico")

    window.geometry('700x350')
    window.configure(bg='DarkSlateGray4')
    
    
    lbl = Label(text="PashaBot", font=("Helvetica",30,"bold"),background="DarkSlateGray4")
    lbl.grid(row=0,column=0,padx=20,pady=20)


    hesapgir(window)
    window.mainloop()

if __name__ == "__main__":
    main()
