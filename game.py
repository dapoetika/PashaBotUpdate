#abcd
from tkinter import *
import time
import subprocess
from threading import Thread
import win32gui
import pyautogui
from python_imagesearch import imagesearch
import requests
import os
import datetime

def cikis(btn):
    for i in range(100):
        if not os.path.exists(str(i)+".png"):
            x = pyautogui.screenshot(f"{i}.png",region=[0,0,360,614])
            time.sleep(2)
            break
    for i in range(10):
        time.sleep(2)
        girildi = ara("./images/girildi.png")
        girildi_dunya = ara("./images/girildi_dunya.png")
        tamam = ara("./images/tamam.png")
        if tamam != -1:
            logkayit(0,"Başka kullanıcı girdi ya da ağ hatası")
            
            break
        elif girildi_dunya != -1:
            time.sleep(2)
            click(btn,girildi_dunya[0]+10,girildi_dunya[1]+10)
        elif girildi != -1:
            return "girildi"
        else: 
            click(btn,20,60)
            time.sleep(bekleme_carpani*2)
    os.system("TASKKILL /F /IM HD-Player.exe")
    logkayit(0,"Bluestacks Kapatıldı")
    return "kapatıldı"

def logkayit(farm,mesaj):
    print(farm,mesaj)
    datadir = "data"
    file_path = os.path.join(datadir, "q.txt")
    if not os.path.exists(file_path):
        open(file_path, "w", encoding="utf-8").close()

    x = open(file_path, "a", encoding="utf-8")
    now = datetime.datetime.now()
    saat = now.strftime("%H:%M")
    x.write(f"{str(farm)} {saat} {mesaj}\n")
    x.close()

def click(btn,x,y):
    global stop
    if not stop:
        pyautogui.click(x,y)
    else:
        terminate(btn)

def ara(imagename,precision=0.6):
    global stop
    
    
    print("aranıyor ", imagename)
    if not stop:
        aranan = imagesearch.imagesearch_region_numLoop(imagename,0,20,0,0,360,614,precision)
        if aranan[0] != -1:
            return aranan
    else:
        return[1,1]
    return -1

def imageclick(btn,imagename,precision=0.6):
    global stop
    print("aranıyor ", imagename)
    for i in range(10):
        if not stop:
            aranan = imagesearch.imagesearch_region_numLoop(imagename,0,20,0,0,360,614,precision)
            if aranan[0] != -1:
                click(btn,aranan[0]+10,aranan[1]+10)
                time.sleep(bekleme_carpani*2)
                return True
        else:
            terminate(btn)
            return False
    return False
def send_heartbeat():
    try:
        vericek = open("./data/data.txt")
        username = vericek.readline().rstrip()
        global sonheartbeat
        sonheartbeat = datetime.datetime.now()
        r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/heartbeat",json={"username":username},timeout=(3, 20))
    except Exception as a:
        logkayit("0",a)
def trr(btn,frm):
    global sonheartbeat
    sonheartbeat = datetime.datetime.now()
    for i in range(100):
        filename = f"{i}.png"
        if os.path.exists(filename):
            os.remove(filename)
    anathr = Thread(target=lambda:sec(btn,frm),daemon=True)
    anathr.start()
    x = open("./data/data.txt")
    username = x.readline().rstrip()
    x.close()
    denetthread = Thread(target=lambda:dene(btn,frm,username),daemon=True)
    denetthread.start()
    
def dene(btn,frm,username):
    global stop 
    stop = False
    while not stop:
        
        workerdene = Thread(target=lambda:goym(btn,frm,username),daemon=True)    
       
        if not workerdene.is_alive():
            logkayit(0,"dene başladı")
            workerdene.start()
            workerdene.join()
            logkayit(0,"dene bitti")
            print("sa")

def goym(btn,frm,username):
    while True:
        try:
            datadir = "data"
            file_path = os.path.join(datadir, "dene.txt")
            if not os.path.exists(file_path):
                open(file_path, "w", encoding="utf-8").close()
        
            x = open(file_path, "a", encoding="utf-8")
            now = datetime.datetime.now()
            saat = now.strftime("%H:%M")
            global sonheartbeat
            if now - sonheartbeat > datetime.timedelta(minutes=30):
                
                log = f"{now.strftime("%d.%m.%Y %H:%M")} BOT KAPANDI"
                r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/logs",json={"username":username,"log":log}, timeout=(3, 20))
                x.write(f"Bot Durdu ve Yeniden Başlatıldı")
                anathr = Thread(target=lambda:sec(btn,frm),daemon=True)
                anathr.start()
            global worker
            x.write(f"{saat} {worker.is_alive()}\n")
            x.close()
            time.sleep(60)
        except Exception as hata:
            with open("./data/dene.txt","a") as x:
                x.write(str(hata))


def sec(btn,frm):
    global stop 
    stop = False
    while not stop:
        global worker
        worker = Thread(target=lambda:main(btn,frm),daemon=True)    
       
        if not worker.is_alive():
            logkayit(0,"start")
            worker.start()
            logkayit(0,"started")
            worker.join()
            logkayit(0,"kill")
            print("sa")
    logkayit(0,"----------------------------")
def arawork(btn):
    worker1 = Thread(target=lambda:durulan(btn),daemon=True)
    worker1.start()
    
def durulan(btn):
    import sys
    global stop
    stop = True
    print(stop)
    sys.exit()

def terminate(btn):
    import sys
    btn.config(state=ACTIVE)
    btn_dur.config(state=DISABLED)
    now = datetime.datetime.now()
    
    try:
        log = f"{now.strftime('%d.%m.%Y %H:%M')} BOT DURDURULDU"
        r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/logs",json={"username":username,"log":log}, timeout=(3, 20))
        logkayit(0,"DURDURULDU")
    except:
        logkayit(0,"DURDURULDU")
    sys.exit()

def collectdata():

    try:
        vericek = open("./data/data.txt")
        username = vericek.readline().rstrip()
        password = vericek.readline().rstrip()
        vericek.close()
        r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/login",json={"username":username,"password":password}, timeout=(3, 20))
        data = r.json().get("userData")

        kullaniciadi = username
        gereksiz = password
        hesapsayisi = data.get("hesapSayisi")

        kaynak_gonder = data.get("kaynakGonder")
        loncatech_yap = data.get("loncatechYap")
        ganimet_yap = data.get("ganimetYap")
        ic_kaynak_bonus = data.get("icKaynakBonus")
        dis_kaynak_bonus = data.get("disKaynakBonus")


        hazine_topla = data.get("hazineTopla")
        lonca_topla = data.get("loncaTopla")
        mesaj_topla = data.get("mesajTopla")

        hasat_et = data.get("hasatEt")
        hizli_topla = data.get("hizliTopla")
        tampon_hasat = data.get("tamponHasat")
        kalkan_kvk = data.get("kvkKalkan")
        arttirici_al = data.get("arttiriciAl")

        global bekleme_carpani
        try:
            kaynakseviye = int(data.get("kaynakSeviye")) - 1
            bekleme_carpani = int(data.get("beklemeCarpani"))
        except:
            kaynakseviye = 5
            bekleme_carpani = 3


        gonderilcekList = data.get("gonderilcekList")
        gozculist = data.get("gozcuList")
        askeregitlist = data.get("askeregitList")
        ifritlist = data.get("ifritList")

        
        if bekleme_carpani == 1:
            bekleme_carpani = 2
        elif bekleme_carpani == 2:
            bekleme_carpani = 1.5
        elif bekleme_carpani == 3:
            bekleme_carpani = 1
        elif bekleme_carpani == 4:
            bekleme_carpani = 0.75
        elif bekleme_carpani == 5:
            bekleme_carpani = 0.5
        
        mail =data.get("mail")
        sifre = data.get("sifre")
        
        

        return {
            "kullaniciadi":kullaniciadi,
            "hesapsayisi": hesapsayisi,
            "kaynak_gonder": kaynak_gonder,
            "loncatech_yap": loncatech_yap,
            "ganimet_yap": ganimet_yap,
            "ic_kaynak_bonus": ic_kaynak_bonus,
            "dis_kaynak_bonus": dis_kaynak_bonus,
            "hazine_topla": hazine_topla,
            "lonca_topla": lonca_topla,
            "mesaj_topla": mesaj_topla,
            "hasat_et": hasat_et,
            "hizli_topla": hizli_topla,
            "tampon_hasat": tampon_hasat,
            "kaynakseviye": kaynakseviye,
            "bekleme_carpani": bekleme_carpani,
            "gonderilcekList": gonderilcekList,
            "gozculist": gozculist,
            "askeregitlist":askeregitlist,
            "mail":mail,
            "sifre":sifre,
            "kvkkalkan":kalkan_kvk,
            "arttirici_al":arttirici_al,
            "ifritlist":ifritlist
        }
    except ValueError:
        print("hata")
        return "hata"

def oyunac():
    
    harf = ["C","D","E","F","G"]
    
    for k in harf:
        try: 
            
            proce = subprocess.Popen(k+":/Program Files/BlueStacks_nxt/HD-Player.exe --instance Pie64 --cmd launchApp --package and.onemt.boe.tr")
                
        except:
            
            continue
    for k in harf:
        try: 
            subprocess.Popen('"'+k+':/Program Files/Microvirt/MEmu/MEmu.exe" MEmu applink and.onemt.boe.tr/org.cocos2dx.lua.AppActivity')
            
        except:
            
            continue
    
    
    time.sleep(bekleme_carpani*5)
    
    hwnd = win32gui.FindWindow(None,"BlueStacks App Player")
    if hwnd == 0:
        hwnd = win32gui.FindWindow(None,"MEmu")
        
    for i in range(5):
        try:
            win32gui.MoveWindow(hwnd,0,0,360,614,True)
        except:
            pass
    
def hesapgiris(btn,mail,sifre):
    logkayit(farm,"Hesap Giriliyor")
    global appopen
    appopen = False
    for i in range(100):
        girildi = ara("./images/girildi.png")
        girildi_dunya = ara("./images/girildi_dunya.png")
        xtus = ara("./images/xtus.png")
        time.sleep(1)
        click(btn,150, 440)
        if girildi != -1:
            appopen = True
            break

        if xtus != -1:
            appopen = True
            break
        if girildi_dunya != -1:
            appopen = True
            break
    
    if appopen:
        pass
    else:
        logkayit(farm,"appopen hesap giris")
        time.sleep(bekleme_carpani*5)
        return "appopen"
    
    logkayit(farm,"Hesap giriliyor 1")
    for i in range(100):
        logkayit(farm,"Hesap giriliyor 1 loop " + str(i))
        girildi_dunya = ara("./images/girildi_dunya.png")
        girildi = ara("./images/girildi.png")
        xtus = ara("./images/xtus.png")
        devredisi = ara("./images/devredisi.png")
        if devredisi != -1:
            logkayit(farm,"Hesap giriliyor 1 Devre Dışı Basıldı")
            click(btn,devredisi[0]+10,devredisi[1]+10)

        elif xtus != -1:
            logkayit(farm,"Hesap giriliyor 1 Xtus Basıldı")
            click(btn,xtus[0]+5,xtus[1]+5)
        

        elif girildi != -1:
            logkayit(farm,"Hesap giriliyor 1 Girildi Tamamlandı")
            break
        elif girildi_dunya != -1:
            logkayit(farm,"Hesap giriliyor 1 GirildiDunya Tamamlandı")
            break
        else:
            logkayit(farm,"Hesap giriliyor 1 Hic Birsey bulunamadı")
            
    
    logkayit(farm,"Hesap Giriliyor 2")
    time.sleep(bekleme_carpani*1)
    
    click(btn,160, 400)
    #hesap değişme
    if hesapgir:
        
        logkayit(farm,"Geçiliyor")
        girildi = ara("./images/girildi.png")
        time.sleep(bekleme_carpani*2)
        if girildi != -1:
            click(btn,160, 400)
            time.sleep(bekleme_carpani*2)
            click(btn,20,75)
            time.sleep(bekleme_carpani*2)
            imageclick(btn,"./images/ayarlar.png")
            time.sleep(bekleme_carpani*2)
            click(btn,290,585)
            time.sleep(bekleme_carpani*2)
            imageclick(btn,"./images/hesaplar.png")
            time.sleep(bekleme_carpani*2)
            time.sleep(bekleme_carpani*2)
            click(btn,50,150)
            time.sleep(bekleme_carpani*2)
            time.sleep(bekleme_carpani*2)
            imageclick(btn,"./images/hesapdegistir.png")
            time.sleep(bekleme_carpani*2)
            time.sleep(bekleme_carpani*2)
            click(btn,110,227)
            time.sleep(bekleme_carpani*2)
            click(btn,110,227)
            time.sleep(bekleme_carpani*2)

            for i in mail[farm]:
                if i == "@":
                    pyautogui.hotkey("altright","q")
                else:
                    pyautogui.write(i)
            time.sleep(bekleme_carpani*2)
            time.sleep(bekleme_carpani*2)
            click(btn,165,320)
            time.sleep(bekleme_carpani*2)
            click(btn,165,320)
            time.sleep(bekleme_carpani*2)
            time.sleep(bekleme_carpani*2)
            for i in sifre[farm]:
                if i == "@":
                    pyautogui.hotkey("altright","q")
                else:
                    pyautogui.write(i)
            time.sleep(bekleme_carpani*2)
            click(btn,170,390)
            time.sleep(bekleme_carpani*2)
            
            hesap_giris_hata = ara("./images/hesap-giris-hata.png")
            if hesap_giris_hata != -1:
                click(btn,20,55)
                time.sleep(bekleme_carpani*2)
                time.sleep(bekleme_carpani*1)
                
                click(btn,20,55)
                time.sleep(bekleme_carpani*2)
                click(btn,20,65)
                time.sleep(bekleme_carpani*2)
                click(btn,20,65)
                time.sleep(bekleme_carpani*2)
                
        for i in range(200):
            
            time.sleep(bekleme_carpani*1)
            girildi = ara("./images/girildi.png")
            xtus = ara("./images/xtus.png")

            if girildi != -1:
                break

            if xtus != -1:
                break
        
        
        time.sleep(bekleme_carpani*1)
        
        xtus = ara("./images/xtus.png")
        devredisi = ara("./images/devredisi.png")
        if devredisi != -1:
            click(btn,devredisi[0]+10,devredisi[1]+10)

        if xtus != -1:
            click(btn,xtus[0]+10,xtus[1]+10)
            
        time.sleep(bekleme_carpani*1)
        
            
            
            #stop
   
    click(btn,160, 400)
    time.sleep(bekleme_carpani*2)
    logkayit(farm,"Hesap Giriliyor 3")
def liman(btn):
    time.sleep(bekleme_carpani*2)
    giris = ara("./images/giris.png")
    if giris != -1:
        click(btn,165, 250)
        time.sleep(bekleme_carpani*1)
        click(btn,160, 380)
    else:
        return "bulunamadi"
        



def ickaynakbonusu(btn,arttirici_al):
    bugday = True
    odun = True
    demir = True
    kuvars = True
    marketegit = False
    for i in arttirici_al:
        if i:
            marketegit = True
    devredisi = ara("./images/devredisi.png")
    if devredisi != -1:
        click(btn,devredisi[0]+10,devredisi[1]+10)
        x = mesajtopla(btn)
        if x =="appopen":
            return "appopen"
    girildi = ara("./images/girildi.png")
    if girildi == -1:
        isOkey = False
        for i in range(10):
            time.sleep(2)
            girildi = ara("./images/girildi.png")
            girildi_dunya = ara("./images/girildi_dunya.png")
            tamam = ara("./images/tamam.png")
            if tamam != -1:
                return "appopen"
            elif girildi_dunya != -1:
                time.sleep(2)
                click(btn,girildi_dunya[0]+10,girildi_dunya[1]+10)
            elif girildi != -1:
                isOkey = True
                break
            else: 
                click(btn,20,60)
                time.sleep(bekleme_carpani*2)
        if not isOkey:
            logkayit(0,"appopen isokey 2")
            return "appopen"
    giris = ara("./images/giris.png")
    if giris == -1:
        return "limanyok"
    time.sleep(bekleme_carpani * 2)
    pyautogui.moveTo(160,380)
    pyautogui.dragTo(160,180,2)
    time.sleep(bekleme_carpani * 2)
   
    pyautogui.moveTo(160, 380)
    pyautogui.dragTo(160,180,2)
    time.sleep(bekleme_carpani * 2)
   
    pyautogui.moveTo(160, 380)
    pyautogui.dragTo(160,280,2)
    time.sleep(bekleme_carpani * 2)
    
    click(btn,265, 400)
    time.sleep(bekleme_carpani * 2)
   
    arttirici_eksik = False
    
    sehir = ara("./images/sehir.png")
    if sehir != -1:
        click(btn,sehir[0] + 10, sehir[1]+ 10)
        time.sleep(bekleme_carpani * 2)
       
        time.sleep(bekleme_carpani * 2)
        for k in range(4):
            x = pyautogui.pixel(250, 140 +(k*60))
            if x[0]>100 or x[1]>100 or x[2]>100:
                pass
            else:
                continue
            click(btn,280, 140 +(k*60))
            time.sleep(bekleme_carpani * 2)
            tamam = ara("./images/tamam.png")
            if tamam != -1:
                click(btn,220, 370)
                time.sleep(bekleme_carpani * 2)
            else:
                if k == 0:
                    odun = False
                elif k==1:
                    bugday = False
                elif k ==2:
                    demir = False
                elif k == 3:
                    kuvars = False
                arttirici_eksik = True
                click(btn,20,65)
                time.sleep(bekleme_carpani * 2)
        click(btn,160, 560)
        time.sleep(bekleme_carpani * 2)
       
        click(btn,20,65)
        time.sleep(bekleme_carpani * 2)
        if arttirici_eksik and marketegit:
            if arttirici_al[0] == False:
                bugday = True
            if arttirici_al[1] == False:
                odun = True
            if arttirici_al[2] == False:
                demir = True
            if arttirici_al[3] == False:
                kuvars = True

            time.sleep(bekleme_carpani * 2)
            click(btn,290,590)
            time.sleep(bekleme_carpani * 2)
            click(btn,240,435)
            time.sleep(bekleme_carpani * 2)
            yukari = 0
            satinalindi = False
            for i in range(20):
                if yukari == 3:
                    break
                bugday_arttirici = ara("./images/bugday_arttirici.png",0.8)
                time.sleep(bekleme_carpani * 2)
                if (bugday_arttirici != -1 and not bugday):
                    time.sleep(bekleme_carpani * 2)
                    click(btn,bugday_arttirici[0]+100,bugday_arttirici[1]+45)
                    print(f"bugday tıkladım {bugday}")
                    time.sleep(bekleme_carpani * 2)
                    bugday = True
                    satinalindi = True
                    for i in range(9):
                        click(btn,235,355)
                        time.sleep(bekleme_carpani*1)
                    yukari = 0
                    click(btn,160,395)
                    tamam = ara("./images/tamam.png",0.8)
                    if tamam != -1:
                        time.sleep(bekleme_carpani*1)
                        click(btn,tamam[0]+10,tamam[1]+10)
                        time.sleep(bekleme_carpani*1)
                        satinalindi = False
                        break
                    continue
                odun_arttirici = ara("./images/odun_arttirici.png",0.8)
                if (odun_arttirici != -1 and not odun):
                    time.sleep(bekleme_carpani * 2)
                    click(btn,odun_arttirici[0]+100,odun_arttirici[1]+45)
                    print(f"odun tıkladım {odun}")
                    time.sleep(bekleme_carpani * 2)
                    odun = True
                    satinalindi = True
                    for i in range(9):
                        click(btn,235,355)
                        time.sleep(bekleme_carpani*1)
                    click(btn,160,395)
                    yukari = 0
                    tamam = ara("./images/tamam.png",0.8)
                    if tamam != -1:
                        time.sleep(bekleme_carpani*1)
                        click(btn,tamam[0]+10,tamam[1]+10)
                        time.sleep(bekleme_carpani*1)
                        satinalindi = False
                        break
                    continue
                demir_arttirici = ara("./images/demir_arttirici.png",0.8)
                if (demir_arttirici != -1 and not demir):
                    time.sleep(bekleme_carpani * 2)
                    click(btn,demir_arttirici[0]+100,demir_arttirici[1]+45)
                    print(f"demir tıkladım {demir}")
                    time.sleep(bekleme_carpani * 2)
                    demir = True
                    satinalindi = True
                    for i in range(7):
                        click(btn,235,355)
                        time.sleep(bekleme_carpani*1)
                    click(btn,160,395)
                    yukari = 0
                    tamam = ara("./images/tamam.png",0.8)
                    if tamam != -1:
                        time.sleep(bekleme_carpani*1)
                        click(btn,tamam[0]+10,tamam[1]+10)
                        time.sleep(bekleme_carpani*1)
                        satinalindi = False
                        break
                    continue
                kuvars_arttirici = ara("./images/kuvars_arttirici.png",0.8)
                if (kuvars_arttirici != -1 and not kuvars):
                    time.sleep(bekleme_carpani * 2)
                    click(btn,kuvars_arttirici[0]+100,kuvars_arttirici[1]+45)
                    print(f"kuvars tıkladım {kuvars}")
                    time.sleep(bekleme_carpani * 2)
                    kuvars = True
                    satinalindi = True
                    for i in range(7):
                        click(btn,235,355)
                        time.sleep(bekleme_carpani*1)
                    click(btn,160,395)
                    yukari = 0
                    tamam = ara("./images/tamam.png",0.8)
                    if tamam != -1:
                        time.sleep(bekleme_carpani*1)
                        click(btn,tamam[0]+10,tamam[1]+10)
                        time.sleep(bekleme_carpani*1)
                        satinalindi = False
                        break
                    continue
                
                if(not bugday or not demir or not odun or not kuvars):
                    x = pyautogui.pixel(200,515)
                    print(x)
                    if x[0] > 50 or x[1] > 50 or x[2] > 50 :
                        pyautogui.moveTo(170,500)
                        pyautogui.dragTo(170,275,1)
                        time.sleep(3)
                        yukari +=1
                    else:
                        break
                else:
                
                    break

            #son
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            if satinalindi:
                time.sleep(bekleme_carpani*2)
                click(btn,200,365)
                time.sleep(bekleme_carpani*2)
                sehir = ara("./images/sehir.png")
                if sehir != -1:
                    time.sleep(bekleme_carpani*1)
                    click(btn,sehir[0] + 10, sehir[1]+ 10)
                    time.sleep(bekleme_carpani * 2)
                    for k in range(4):
                        x = pyautogui.pixel(250, 140 +(k*60))
                        if x[0]>100 or x[1]>100 or x[2]>100:
                            pass
                        else:
                            continue
                        click(btn,280, 140 +(k*60))
                        time.sleep(bekleme_carpani * 2)
                        tamam = ara("./images/tamam.png")
                        if tamam != -1:
                            click(btn,220, 370)
                            time.sleep(bekleme_carpani * 2)
                        else:
                            if k == 0:
                                odun = False
                            elif k==1:
                                bugday = False
                            elif k ==2:
                                demir = False
                            elif k == 3:
                                kuvars = False
                            arttirici_eksik = True
                            click(btn,20,65)
                            time.sleep(bekleme_carpani * 2)
                    time.sleep(bekleme_carpani * 2)
                    click(btn,20,65)                
               
def mesajtopla(btn):
    time.sleep(bekleme_carpani*2)
    isOkey = False
    for i in range(10):
        time.sleep(bekleme_carpani*2)
        girildi = ara("./images/girildi.png")
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi != -1 or girildi_dunya != -1:
            isOkey = True
            break
        else:
            click(btn,20,60)
    if not isOkey:
        logkayit(0,"mesaj topla appopen")
        return "appopen"
    click(btn,235,590)
    time.sleep(bekleme_carpani*2)
    
    sistem = ara("./images/sistem.png")
    if sistem != -1:
        click(btn,sistem[0]+10,sistem[1]+10)
    
        time.sleep(bekleme_carpani*2)
        click(btn,160,590)
        
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
    time.sleep(bekleme_carpani*2)
    etkinlikler = ara("./images/etkinlikler.png")
    if etkinlikler != -1:
        time.sleep(bekleme_carpani*2)
        click(btn,160,335)
        time.sleep(bekleme_carpani*2)
        while True:
            click(btn,160,590)
            time.sleep(bekleme_carpani*2)
            tumunu_oku = ara("./images/tumunu_oku.png")
            if tumunu_oku != -1:
                click(btn,160,590)
            else:
                break

            time.sleep(bekleme_carpani*0.5)
        #mesajları sil
        time.sleep(bekleme_carpani*2)
        click(btn,300,595)
        time.sleep(bekleme_carpani*2)
        click(btn,25,595)
        time.sleep(bekleme_carpani*2)
        click(btn,160,595)
        time.sleep(bekleme_carpani*2)
        click(btn,160,370)
        time.sleep(bekleme_carpani*2)
        click(btn,25,595)
        time.sleep(bekleme_carpani*2)
        click(btn,160,595)
        time.sleep(bekleme_carpani*2)
        click(btn,160,370)
        time.sleep(bekleme_carpani*2)
        click(btn,300,595)
        time.sleep(bekleme_carpani*2)
        while True:
            click(btn,160,590)
            time.sleep(bekleme_carpani*2)
            tumunu_oku = ara("./images/tumunu_oku.png")
            if tumunu_oku != -1:
                click(btn,160,590)
            else:
                break

        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
    
        
    time.sleep(bekleme_carpani*1)
    click(btn,20,65)
    
    time.sleep(bekleme_carpani*1)
    
    time.sleep(bekleme_carpani*2)
    for i in range(5):
        girildi = ara("./images/girildi.png")
        if girildi == -1:
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
        else:
            break
    time.sleep(bekleme_carpani*3)
    time.sleep(bekleme_carpani*4)
    pyautogui.hotkey("ctrl", "shift","3")
    time.sleep(bekleme_carpani*10)

def mesajtoplaoteki(btn):
    time.sleep(bekleme_carpani*2)
    girildi = ara("./images/girildi_dunya.png")
    if girildi == -1:
        logkayit(0,"mesaj topla öteki app")
        return "appopen"
    click(btn,235,590)
    time.sleep(bekleme_carpani*2)
    
    click(btn,150,450)
    
    time.sleep(bekleme_carpani*2)
    click(btn,160,590)
    
    time.sleep(bekleme_carpani*2)
    click(btn,20,65)
    
    time.sleep(bekleme_carpani*2)
    click(btn,160,335)
    
    while True:
        time.sleep(bekleme_carpani*2)
        tumunu_oku = ara("./images/tumunu_oku.png")
        if tumunu_oku != -1:
            click(btn,160,590)
        else:
            break

        time.sleep(bekleme_carpani*0.5)
    
    time.sleep(bekleme_carpani*2)
    click(btn,20,65)
    
        
    time.sleep(bekleme_carpani*1)
    click(btn,20,65)
    
    time.sleep(bekleme_carpani*1)
    
    time.sleep(bekleme_carpani*2)
    girildi = ara("./images/girildi_dunya.png")

    if girildi != -1:
        pass
    else:
        logkayit(farm,"mesaj topla oteki 2")
        
        time.sleep(bekleme_carpani*5)
        return "appopen"

def loncatopla(btn,loncatech_yap):
    time.sleep(bekleme_carpani*2)
    girildi = ara("./images/girildi.png")
    if girildi == -1:
        logkayit(0,"lonca topla app")
        return "appopen"
    
    click(btn,290,590)

    loncakatil = ara("./images/loncaya-katil.png")
    if loncakatil != -1:
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
        return "lonca yok"
    
    time.sleep(bekleme_carpani*2)
    click(btn,160,520)
    
    time.sleep(bekleme_carpani*2)
    click(btn,160,595)

    time.sleep(bekleme_carpani*2)
    click(btn,20,65)
    time.sleep(bekleme_carpani*2)
    click(btn,160,300)
    
    
    
        

    time.sleep(bekleme_carpani*2)
    click(btn,160,580)
    
    time.sleep(bekleme_carpani*2)
    
    click(btn,20,65)
    
    time.sleep(bekleme_carpani*2)
    click(btn,160,475)
    

    time.sleep(bekleme_carpani*2)
    
    free = ara("./images/free.png")
    time.sleep(bekleme_carpani*2)
    if free != -1:
        click(btn,free[0] + 10,free[1]+10)
    
    
    time.sleep(bekleme_carpani*2)
    click(btn,160,100)
    

    for i in range(3):
        time.sleep(bekleme_carpani*2)
        topla = ara("./images/topla.png")
        time.sleep(bekleme_carpani*2)
        if topla != -1:
            click(btn,topla[0] + 10,topla[1]+10)
            time.sleep(bekleme_carpani*2)
            
        else:
            break
    
    
    
    time.sleep(bekleme_carpani*2)
    helpreq = ara("./images/helpreq.png")
    if helpreq != -1:
        click(btn,helpreq[0] + 10,helpreq[1]+10)
        time.sleep(bekleme_carpani*2)
        
    click(btn,270,100)
  



    for i in range(3):
        time.sleep(bekleme_carpani*2)
        topla = ara("./images/topla.png")
        
        time.sleep(bekleme_carpani*2)
        if topla != -1:
            click(btn,topla[0] + 10,topla[1]+10)
           
            time.sleep(bekleme_carpani*2)
            
        else:
            
            break
    
    time.sleep(bekleme_carpani*2)
    help = ara("./images/help.png")
    if help != -1:
        click(btn,help[0] + 10,help[1]+10)
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)
    
    else:
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)
    if not loncatech_yap:
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)

def loncatek(btn):

    time.sleep(bekleme_carpani*2)
    click(btn,290,590)
    time.sleep(bekleme_carpani*2)
    click(btn,245,390)
    time.sleep(bekleme_carpani*2)
    click(btn,160,180)
    for i in range(25):
        tamam = ara("./images/tamam.png")
        time.sleep(bekleme_carpani*1)
        x = pyautogui.pixel(200,425)
        if x[0] > 100 or x[1] > 100 or x[2] > 100:
            pass
        else:
            time.sleep(bekleme_carpani*2)
            for i in range(4):
                girildi = ara("./images/girildi.png")
                if girildi == -1:
                    click(btn,20,65)
                    time.sleep(bekleme_carpani*2)
                    continue
                return "bitti"
        if tamam != -1:
            time.sleep(bekleme_carpani*2)
            for i in range(4):
                girildi = ara("./images/girildi.png")
                if girildi == -1:
                    click(btn,20,65)
                    time.sleep(bekleme_carpani*2)
                    continue
                else:
                    return "bitti"
        else: 
            click(btn,240,430)
    
def trainsoldier(btn,tahilarabasi):

    for hangisi in range(5):
        girildi = ara("./images/girildi.png")
        if girildi != -1:
            pass
        else:
            isOkey = False
            for i in range(10):
                time.sleep(2)
                girildi = ara("./images/girildi.png")
                girildi_dunya = ara("./images/girildi_dunya.png")
                if girildi_dunya != -1:
                    time.sleep(2)
                    click(btn,girildi_dunya[0]+10,girildi_dunya[1]+10)
                elif girildi != -1:
                    isOkey = True
                    break
                else: 
                    click(btn,20,60)
                    time.sleep(bekleme_carpani*2)
            if not isOkey:
                logkayit(0,"appopen isokey 4")
                return "appopen"
            
        time.sleep(bekleme_carpani*2)
        click(btn,10,320)

        
        askerler = ara("./images/askerler.png")
        time.sleep(bekleme_carpani*2)
        for i in range(3):
            if askerler != -1:
                if tahilarabasi:
                    click(btn,askerler[0] +205,askerler[1] + 45 +(26*3))
                else:
                    click(btn,askerler[0] +205,askerler[1] + 45 +(26*hangisi))
                time.sleep(bekleme_carpani*2)
                break
            else:
                pyautogui.moveTo(140,335)
                time.sleep(bekleme_carpani*2)
                pyautogui.dragTo(140,145,1)
                time.sleep(bekleme_carpani*2)
        
        girildi = ara("./images/girildi.png")
        if girildi != -1:
            pass
        else:
            isOkey = False
            for i in range(10):
                time.sleep(2)
                girildi = ara("./images/girildi.png")
                girildi_dunya = ara("./images/girildi_dunya.png")
                if girildi_dunya != -1:
                    time.sleep(2)
                    click(btn,girildi_dunya[0]+10,girildi_dunya[1]+10)
                elif girildi != -1:
                    isOkey = True
                    break
                else: 
                    click(btn,20,60)
                    time.sleep(bekleme_carpani*2)
            if not isOkey:
                logkayit(0,"appopen isokey 4")
                return "appopen"
        
        click(btn,182,355)
        time.sleep(bekleme_carpani*2)
        girildi = ara("./images/girildi.png")
        if girildi == -1:
            click(btn,245,590)

        if tahilarabasi:
            break

def hazinetopla(btn,ganimetyap):
    girildi = ara("./images/girildi.png")
    if girildi != -1:
        pass
    else:
        isOkey = False
        for i in range(10):
            time.sleep(2)
            girildi = ara("./images/girildi.png")
            girildi_dunya = ara("./images/girildi_dunya.png")
            if girildi_dunya != -1:
                time.sleep(2)
                click(btn,girildi_dunya[0]+10,girildi_dunya[1]+10)
            elif girildi != -1:
                isOkey = True
                break
            else: 
                click(btn,20,60)
                time.sleep(bekleme_carpani*2)
        if not isOkey:
            logkayit(0,"hazine havuzu app")
            return "appopen"
        
    time.sleep(bekleme_carpani*2)
    click(btn,10,320)
    bulundu = False

   

    for i in range(5):
        
        hazinehavuzu = ara("./images/hazinehavuzu.png")
        time.sleep(bekleme_carpani*2)
        
        if hazinehavuzu != -1:
            click(btn,hazinehavuzu[0] +210,hazinehavuzu[1] +45)
            time.sleep(bekleme_carpani*2)
            break
        else:
            pyautogui.moveTo(140,335)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(140,145,1)
            time.sleep(bekleme_carpani*2)
            
    time.sleep(bekleme_carpani*2)
    
    
    detaylar = ara("./images/detaylar.png")
    time.sleep(bekleme_carpani*2)
    if detaylar != -1:
        click(btn,228, 356)
        bulundu = True
        
        time.sleep(bekleme_carpani*2)
        
    else:
        
        if ganimetyap == True:
            pass
        else:
            click(btn,160, 600)
            
        

    if bulundu:
        for i in range(20):
            
            satin = ara("./images/satin.png")
            if satin != -1:
                click(btn,160, 150)
                time.sleep(bekleme_carpani*1)
                click(btn,20, 60)
                time.sleep(bekleme_carpani*1)
                break
            else:
                click(btn,160, 150)
                time.sleep(bekleme_carpani*1)

def ganimet_karavani(btn):

    girildi = ara("./images/girildi.png")
    if girildi == -1:
        logkayit(farm,"appopen karavan oncesi hata çıktı")
        isOkey = False
        for i in range(10):
            time.sleep(2)
            girildi = ara("./images/girildi.png")
            girildi_dunya = ara("./images/girildi_dunya.png")
            tamam = ara("./images/tamam.png")
            if tamam != -1:
                return "appopen"
            elif girildi_dunya != -1:
                time.sleep(2)
                logkayit(farm,"appopen karavan oncesi girildi_dunya basıldı")
                click(btn,girildi_dunya[0]+10,girildi_dunya[1]+10)
            elif girildi != -1:
                logkayit(farm,"appopen karavan oncesi girildi bulundu")
                isOkey = True
                break
            else: 
                logkayit(farm,"appopen karavan oncesi geri basıldı")
                click(btn,20,60)
                time.sleep(bekleme_carpani*2)
        if not isOkey:
            logkayit(farm,"appopen karavan oncesi")
            return "appopen"
    
    now = datetime.datetime.now()
    if int(now.strftime("%H") ) < 6 and int(now.strftime("%H") ) > 0:
        print("gece")
        time.sleep(bekleme_carpani*3)
        click(btn,295, 525)
        return "gece"
    print("gece kontrol")
    time.sleep(bekleme_carpani*3)
    click(btn,10,320)
    time.sleep(bekleme_carpani*3)

    for i in range(5):
        ganimet_karavani = ara("./images/ganimet_karavani.png",0.8)
        time.sleep(bekleme_carpani*3)
        
        if ganimet_karavani != -1:
            click(btn,ganimet_karavani[0] +210,ganimet_karavani[1] +45)
            time.sleep(bekleme_carpani*3)
            break
        else:
            pyautogui.moveTo(140,335)
            time.sleep(bekleme_carpani*3)
            pyautogui.dragTo(140,145,1)
            time.sleep(bekleme_carpani*3)

    for i in range(5):
        topla = ara("./images/topla-dene.png")
        time.sleep(bekleme_carpani*1)
        if topla != -1:

            click(btn,160,475)
            time.sleep(bekleme_carpani*3)

            click(btn,295,485)
            time.sleep(bekleme_carpani*3)

            click(btn,160,460)
            time.sleep(bekleme_carpani*3)

            click(btn,230,370)
            time.sleep(bekleme_carpani*3)
            click(btn,20,65)

        
    click(btn,265,585) 
    time.sleep(bekleme_carpani*2)
    
    

    ganimet_karavani_hata = ara("./images/ganimet_karavani_hata.png")
    ganimet_karavani_gece = ara("./images/ganimet_karavani_gece.png")
    hallet = ara("./images/hallet.png")
    time.sleep(bekleme_carpani*3)
    if(ganimet_karavani_hata != -1):
        time.sleep(bekleme_carpani*3)
        click(btn,20,65) 
        time.sleep(bekleme_carpani*3)
        logkayit(farm,"ganimet karavani hata")
    
      
    elif(ganimet_karavani_gece != -1):
        time.sleep(bekleme_carpani*3)
        click(btn,20,65) 
        time.sleep(bekleme_carpani*3)
        logkayit(farm,"ganimet karavani gece")
    
      
    elif hallet != -1:
        click(btn,hallet[0]+20,hallet[1]+20)
        time.sleep(bekleme_carpani*2)
        click(btn,230,370)
        time.sleep(bekleme_carpani*2)
        click(btn,20,65) 
        time.sleep(bekleme_carpani*2)
        click(btn,20,65) 
      
    else:

        click(btn,165,590) 
        time.sleep(bekleme_carpani*3)
        
        ganimet_askervar = ara("./images/ganimet_askervar.png")
        if ganimet_askervar != -1:

            click(btn,65,300) 
            time.sleep(bekleme_carpani*3)

            click(btn,160,575) 
            time.sleep(bekleme_carpani*3)




            click(btn,135,300) 
            time.sleep(bekleme_carpani*3)

            click(btn,160,575) 
            time.sleep(bekleme_carpani*3)




            click(btn,200,300) 
            time.sleep(bekleme_carpani*3)

            click(btn,160,460) 
            time.sleep(bekleme_carpani*3)

            click(btn,265,300) 
            time.sleep(bekleme_carpani*3)

            click(btn,160,470) 
            time.sleep(bekleme_carpani*3)


            click(btn,270,235) 
            time.sleep(bekleme_carpani*3)

            click(btn,255,225) 
            time.sleep(bekleme_carpani*3)


            pyautogui.moveTo(110,386)
            pyautogui.dragTo(290,386,2) 
            time.sleep(bekleme_carpani*3)


            click(btn,160,590)
            time.sleep(bekleme_carpani*3)

            click(btn,20,65)
            time.sleep(bekleme_carpani*3)
            
        else:
            click(btn,100,65)
            time.sleep(bekleme_carpani*3)
            click(btn,20,65)
            
    #ganimet_karavani bitis

def hizlitamponhasat(btn,hizli,tampon,hasat):
    if hasat:
        time.sleep(bekleme_carpani*2)
        click(btn,295, 525)
        time.sleep(bekleme_carpani*2)
        for i in range(3):
            hasatet = ara("./images/hasatet.png")
            
            if hasatet != -1:
                click(btn,hasatet[0]+10,hasatet[1]+10)
                time.sleep(bekleme_carpani*2)
                click(btn,160, 490)
                time.sleep(bekleme_carpani*2)
                break
            else:
                click(btn,60+(i*70),150)
                time.sleep(bekleme_carpani*2)
    if hizli:
        time.sleep(bekleme_carpani*2)
        click(btn,295, 525)
        time.sleep(bekleme_carpani*2)
        for i in range(3):
            hizlitopla = ara("./images/hizlitopla.png")
            
            if hizlitopla != -1:
                click(btn,hizlitopla[0]+10,hizlitopla[1]+10)
                time.sleep(bekleme_carpani*2)
                click(btn,160, 490)
                time.sleep(bekleme_carpani*2)
                break
            else:
                click(btn,60+(i*70),150)
                time.sleep(bekleme_carpani*2)
    if tampon:
        time.sleep(bekleme_carpani*2)
        click(btn,295, 525)
        time.sleep(bekleme_carpani*2)
        click(btn,270, 100)
        time.sleep(bekleme_carpani*2)
        tamponhasat = ara("./images/tamponhasat.png")
        if tamponhasat != -1:
            click(btn,tamponhasat[0]+10, tamponhasat[1]+10)
            time.sleep(bekleme_carpani*2)
            click(btn,160, 490)
            time.sleep(bekleme_carpani*2)
        
    click(btn,200, 600)
    time.sleep(bekleme_carpani*1)
       
def sonrakidunya(btn):
    for i in range(10):
        time.sleep(2)
        girildi = ara("./images/girildi.png")
        girildi_dunya = ara("./images/girildi_dunya.png")
        tamam = ara("./images/tamam.png")
        if tamam != -1:
            logkayit(0,"Başka kullanıcı girdi ya da ağ hatası")
            break
        elif girildi_dunya != -1:
            logkayit(0,"SONRAKİ DUNYA BULUNDU")
            time.sleep(2)
            return "basarili"
        elif girildi != -1:
            logkayit(0,"İLK DUNYADAYIZ SONRAKİNE TIKLANDI")
            click(btn,girildi[0]+10,girildi[1]+10)
        else: 
            logkayit(0,"DUNYA BULUNAMADI GERI TIKLANDI")
            click(btn,20,60)
            time.sleep(bekleme_carpani*2)
    return "basarisiz"

def ifritbul(btn):
    aranan = -1
    ifrit = ara("./images/ifrit.png")
    ifrit2 = ara("./images/ifrit2.png")
    ifrit3 = ara("./images/ifrit3.png")
    devredisibirak = ara("./images/devredisi.png")
    if devredisibirak != -1:
        
        click(btn,devredisibirak[0]+10,devredisibirak[1]+10)
        time.sleep(bekleme_carpani*2)
        mesajtoplaoteki(btn)
    if ifrit != -1:
        aranan = ifrit
    if ifrit2 != -1:
        aranan = ifrit2

    if ifrit3 != -1:
        aranan = ifrit3
    if aranan ==-1:
        return "devam"
    time.sleep(bekleme_carpani*2)
    click(btn,aranan[0]+10,aranan[1]+20)
    time.sleep(bekleme_carpani*2)
    elitifrit = ara("./images/elitifrit.png",0.8)
    if elitifrit == -1:
        time.sleep(bekleme_carpani*2)
        click(btn,160,85)
        return "devam"
    
    click(btn,160,500)
    time.sleep(bekleme_carpani*2)
    vip = ara("./images/vip.png")
    if vip !=-1:
        click(btn,160,500)
        return "vip"
    click(btn,230,480)
    time.sleep(bekleme_carpani*2)
    click(btn,60,95)
    time.sleep(bekleme_carpani*2)
    click(btn,265,590)
    time.sleep(bekleme_carpani*2)
    click(btn,265,590)
    girildi_dunya = ara("./images/girildi_dunya.png")
    if girildi_dunya == -1:
        return "appopen"
    time.sleep(bekleme_carpani*2)
    tamam = ara("./images/tamam.png")
    if tamam != -1:
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
        return "energy"
    return "basarili"

def ifrit(btn):
    kacinci = 0
    while True:
        send_heartbeat()
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi_dunya == -1:
            return "appopen"
        time.sleep(bekleme_carpani*2)
        click(btn,160,530)
        time.sleep(bekleme_carpani*2)
        click(btn,280,170)
        time.sleep(bekleme_carpani*2)
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi_dunya != -1:
            return "appopen"
        if kacinci < 9:
            click(btn,30,220+(kacinci*40))
        else:
            for i in range(kacinci-8):
                pyautogui.moveTo(100,300)
                pyautogui.dragTo(100,300-(kacinci*3),1)
            time.sleep(bekleme_carpani*2)
            click(btn,30,220+(8*40))
        time.sleep(bekleme_carpani*4)
        click(btn,160,85)
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi_dunya == -1:
            kacinci = 0
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            continue
        kacinci += 1
        for i in range(1,3):
            time.sleep(bekleme_carpani*2)
            x = ifritbul(btn)
            if x == "vip":
                return "vip"
            elif x == "appopen":
                logkayit(0,"appopen ifrit ")
                return "appopen"
            elif x == "basarili":
                break
            elif x=="energy":
                return "energy"
            elif x == "vip":
                return "vip"
            for k in range((2*i)-1):#sol
                pyautogui.moveTo(80,340)
                pyautogui.dragTo(320,340,1)
                time.sleep(bekleme_carpani*2)
                x = ifritbul(btn)
                if x == "vip":
                    return "vip"
                elif x == "appopen":
                    logkayit(0,"appopen ifrit ")
                    return "appopen"
                elif x == "basarili":
                    break
                elif x=="energy":
                    return "energy"
                elif x == "vip":
                    return "vip"
            if x == "basarili":
                break
            for k in range((2*i)-1):#yukarı
                pyautogui.moveTo(160,100)
                pyautogui.dragTo(160,490,1)
                time.sleep(bekleme_carpani*2)
                x = ifritbul(btn)
                if x == "vip":
                    return "vip"
                elif x == "appopen":
                    logkayit(0,"appopen ifrit ")
                    return "appopen"
                elif x == "basarili":
                    break
                elif x=="energy":
                    return "energy"
                elif x == "vip":
                    return "vip"
            if x == "basarili":
                break
                
            for k in range(2*i):#sag
                pyautogui.moveTo(245,340)
                pyautogui.dragTo(5,340,1)
                time.sleep(bekleme_carpani*2)
                x = ifritbul(btn)
                if x == "vip":
                    return "vip"
                elif x == "appopen":
                    logkayit(0,"appopen ifrit ")
                    return "appopen"
                elif x == "basarili":
                    break
                elif x=="energy":
                    return "energy"
                elif x == "vip":
                    return "vip"
            if x == "basarili":
                break
                
            for k in range(2*i):#aşşa
                pyautogui.moveTo(160,490)
                pyautogui.dragTo(160,100,1)
                time.sleep(bekleme_carpani*2)
                x = ifritbul(btn)
                if x == "vip":
                    return "vip"
                elif x == "appopen":
                    logkayit(0,"appopen ifrit ")
                    return "appopen"
                elif x == "basarili":
                    break
                elif x=="energy":
                    return "energy"
                elif x == "vip":
                    return "vip"
            if x == "basarili":
                break
            
def kvkkalkan(btn):
    time.sleep(bekleme_carpani*2)
    tarihler = ['2025-08-07', '2025-08-08', '2025-08-09', '2025-08-21', '2025-08-22', '2025-08-23', '2025-09-04', '2025-09-05', '2025-09-06', '2025-09-18', '2025-09-19', '2025-09-20', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-16', '2025-10-17', '2025-10-18', '2025-10-30', '2025-10-31', '2025-11-01', '2025-11-13', '2025-11-14', '2025-11-15', '2025-11-27', '2025-11-28', '2025-11-29', '2025-12-11', '2025-12-12', '2025-12-13', '2025-12-25', '2025-12-26', '2025-12-27', '2026-01-08', '2026-01-09', '2026-01-10', '2026-01-22', '2026-01-23', '2026-01-24', '2026-02-05', '2026-02-06', '2026-02-07', '2026-02-19', '2026-02-20', '2026-02-21', '2026-03-05', '2026-03-06', '2026-03-07', '2026-03-19', '2026-03-20', '2026-03-21', '2026-04-02', '2026-04-03', '2026-04-04', '2026-04-16', '2026-04-17', '2026-04-18', '2026-04-30', '2026-05-01', '2026-05-02', '2026-05-14', '2026-05-15', '2026-05-16', '2026-05-28', '2026-05-29', '2026-05-30', '2026-06-11', '2026-06-12', '2026-06-13', '2026-06-25', '2026-06-26', '2026-06-27', '2026-07-09', '2026-07-10', '2026-07-11', '2026-07-23', '2026-07-24', '2026-07-25', '2026-08-06', '2026-08-07']
    utc_time = datetime.datetime.now(datetime.timezone.utc)
    bugun = utc_time.strftime("%Y-%m-%d")
    saat = utc_time.strftime("%H")
    if bugun in tarihler:
        if utc_time.weekday() == 3 and utc_time.time() < datetime.datetime.strptime("10:00", "%H:%M").time():
            return "dahadegil"
        time.sleep(bekleme_carpani*2)
        click(btn,160, 350)
        time.sleep(bekleme_carpani*2)
        click(btn,220, 290)
        time.sleep(bekleme_carpani*2)
        click(btn,180, 125)
        time.sleep(bekleme_carpani*2)
        click(btn,275, 330)
        time.sleep(bekleme_carpani*2)
        tamam = ara("./images/tamam.png")
        if tamam != -1:
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
        else:
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)

def kaynakgonder(btn):
    kacinci = 0
    gonderilensayi = 0
    hata = 0
    while kacinci < 4:
        gonderilensayi += 1
        if gonderilensayi%10 == 0:
            send_heartbeat()
            
        if hata == 3:
            return "attack"
        devredisi = ara("./images/devredisi.png")
        if devredisi != -1:
            click(btn,devredisi[0]+10,devredisi[1]+10)
            x = mesajtoplaoteki(btn)
            if x =="appopen":
                return "appopen"
        
        girildi_dunya = ara("./images/girildi_dunya.png")

        if girildi_dunya == -1:
            logkayit(farm,"kaynak gonder baslangic appopen")
            return "appopen"
        
        time.sleep(bekleme_carpani*1)
        click(btn,165, 530)
        time.sleep(bekleme_carpani*1)
        click(btn,165, 530)
        time.sleep(bekleme_carpani*1)
        click(btn,125, 170)

        
        
       
        girildi_dunya = ara("./images/girildi_dunya.png")

        if girildi_dunya != -1:
            logkayit(farm,"appopen favori")
            return "appopen"
        
        
        time.sleep(bekleme_carpani*2)
        click(btn,125, 215)
        time.sleep(bekleme_carpani*2)

        
        for i in range(1):
            kaynakyardim = ara("./images/kaynakyardim.png")
            attack = ara("./images/attack.png")
            if kaynakyardim != -1:
                click(btn,kaynakyardim[0] + 10,kaynakyardim[1] + 10)
                time.sleep(bekleme_carpani*2)
                break
            if attack != -1:
                return "attack"
            else:
                
                pyautogui.moveTo(160, 350)
                pyautogui.dragTo(100,350,1)
                kaynakyardim = ara("./images/kaynakyardim.png")

                time.sleep(bekleme_carpani*2)
                if kaynakyardim != -1:
                    click(btn,kaynakyardim[0] + 10,kaynakyardim[1] + 10)
                    time.sleep(bekleme_carpani*2)
                    break
                else:
                    click(btn,100,350)
                    time.sleep(bekleme_carpani*2)


        vip = ara("./images/vip.png")
        
        kaynakyardim = ara("./images/kaynakyardim.png")
        if vip != -1:
            logkayit(farm,"appopen vip")
            return "vip"
        
        if kaynakyardim != -1:
            click(btn,kaynakyardim[0] + 10,kaynakyardim[1] + 10)
            time.sleep(bekleme_carpani*2)

        yolla = ara("./images/yolla.png")

        if yolla != -1:
            hata = 0
            pass
        else:
            hata += 1
            continue


        
        pyautogui.moveTo(115,275 + kacinci * 60)
        time.sleep(bekleme_carpani*2)
        pyautogui.dragTo(290,275 + kacinci * 60,1)
        time.sleep(bekleme_carpani*2)
        click(btn,165, 595)
        time.sleep(bekleme_carpani*1)
        
        odun_sinir =ara("./images/odun_sinir.png")
        durum_degisti = ara("./images/durum_degisti.png")
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi_dunya != -1:
            if odun_sinir != -1:
                logkayit(farm,"kullanici sinira ulasti")
                kacinci+= 1
            elif durum_degisti != -1:
                
                kacinci += 1
        else:
            kacinci += 1
            
            if kacinci == 4:
                click(btn,20,65)
                logkayit(farm,"kaynak gonderme bitti")
                break
            pyautogui.moveTo(115,275 + kacinci * 60)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(290,275 + kacinci * 60,1)
           
            time.sleep(bekleme_carpani*2)
            click(btn,165, 595)
            time.sleep(bekleme_carpani*2)
            girildi_dunya = ara("./images/girildi_dunya.png")
            if girildi_dunya == -1:
                click(btn,20,65)
                logkayit(farm,"kaynak gonderme hata")

def askergonder(btn,hangisi,kaynakseviye):
    ilksefer = True
    time.sleep(bekleme_carpani*2)
    hata = 0
    while True:
        send_heartbeat()
        devredisi = ara("./images/devredisi.png")
        if devredisi != -1:
            click(btn,devredisi[0]+10,devredisi[1]+10)
            x = mesajtoplaoteki(btn)
            if x =="appopen":
                return "appopen"
        girildi_dunya = ara("./images/girildi_dunya.png")

        if girildi_dunya == -1:
            isOkey = False
            for i in range(10):
                time.sleep(2)
                girildi = ara("./images/girildi.png")
                girildi_dunya = ara("./images/girildi_dunya.png")
                tamam = ara("./images/tamam.png")
                if tamam != -1:
                    logkayit(0,"asker gonder app ")
                    return "appopen"
                elif girildi_dunya != -1:
                    time.sleep(2)
                    isOkey = True
                    break
                elif girildi != -1:
                    click(btn,girildi[0]+10,girildi[1]+10)
                else: 
                    click(btn,20,60)
                    time.sleep(bekleme_carpani*2)
                
            if not isOkey:
                hata += 1
                if hata>2:
                    logkayit(0,"appopen isOkey 1")
                    return "appopen"
            

        senden = False
        
        time.sleep(bekleme_carpani*2)
        click(btn,255, 525)
        time.sleep(bekleme_carpani*1)
        click(btn,255, 525)
        time.sleep(bekleme_carpani*2)
            
        girildi_dunya = ara("./images/girildi_dunya.png")

        if girildi_dunya != -1:
            logkayit(0,"appopen askergonder")
            return "appopen"
            
        pyautogui.moveTo(260, 445)
        time.sleep(bekleme_carpani*2)
        pyautogui.dragTo(120, 445, 1)
        time.sleep(bekleme_carpani*2)
        click(btn,120+(60*hangisi), 445)
        time.sleep(bekleme_carpani*2)
        
        
        if ilksefer:
            for i in range(8):
                click(btn,40, 525)
                time.sleep(bekleme_carpani*0.2)
            for i in range(kaynakseviye):
                click(btn,205, 525)
                time.sleep(bekleme_carpani*0.2)
            ilksefer = False

        
        click(btn,165, 585)
        
        
            
        artibir = ara("./images/artibir.png")

        if artibir != -1:
            firstTime = True
            time.sleep(bekleme_carpani*2)
            return "exit"
            
        else:
            time.sleep(bekleme_carpani*3)
            click(btn,160, 320)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(120,320,1)
            time.sleep(bekleme_carpani*2)
            
        raid = ara("./images/raid.png")

        if raid != -1:
            time.sleep(bekleme_carpani*2)
            global bonusal

            if bonusal:
                click(btn,140,245)
                time.sleep(bekleme_carpani * 2)
                click(btn,240,320)
                time.sleep(bekleme_carpani * 2)
                kullan = ara("./images/kullan.png")
                if kullan != -1:
                    click(btn,kullan[0]+10,kullan[1]+10)
                    time.sleep(bekleme_carpani * 2)
                    tamam = ara("./images/tamam.png")
                    if tamam != -1:
                        click(btn,20,65)
                        time.sleep(bekleme_carpani * 1)
                        click(btn,20,65)
                        time.sleep(bekleme_carpani * 1)
                        click(btn,20,65)
                        time.sleep(bekleme_carpani * 1)
                    else:
                        click(btn,20,65)
                        time.sleep(bekleme_carpani * 1)
                        click(btn,20,65)
                        time.sleep(bekleme_carpani * 1)
                click(btn,135, 320)
                time.sleep(bekleme_carpani * 2)
                click(btn,raid[0] + 20, raid[1] + 20)
                bonusal = False
                senden = True
                
            else:
                click(btn,raid[0] + 20, raid[1] + 20)
                time.sleep(bekleme_carpani*2)
                senden = True
                
       
        if senden:
            pass
        else:
            continue


        targetHata = False
        for i in range(2):   
            time.sleep(bekleme_carpani*2)
            tamam = ara("./images/tamam.png")
            vip = ara("./images/vip.png")
            target = ara("./images/target.png",0.8)
            girildi_dunya = ara("./images/girildi_dunya.png")
            if target != -1:
                time.sleep(bekleme_carpani*2)
                break
    
            elif vip != -1:
                logkayit(farm,"bugday vip 1 hata")
                click(btn,265, 585)
                time.sleep(bekleme_carpani*2)
                return "vip"
            
            elif tamam != -1:
                click(btn,tamam[0]+20,tamam[1]+20)
                logkayit(farm,"bugday tamam 1 hata")
                return "vip"
                
            elif girildi_dunya != -1:
                click(btn,255, 530)
                time.sleep(bekleme_carpani*2)
                click(btn,20, 65)
                time.sleep(bekleme_carpani*2)
                click(btn,130, 320)
                time.sleep(bekleme_carpani*2)

                raid = ara("./images/raid.png")
                if raid != -1:
                    click(btn,raid[0]+20,raid[1]+20)
                    continue
                else:
                    logkayit(farm,"dondu 1")
                    return "appopen"
    
            else:
                logkayit(farm,"bugday target 1 hata")
                targetHata = True
                click(btn,20, 65)
                cancel = True
                break
        if targetHata:
            continue

        
        
        click(btn,265, 585)
        time.sleep(bekleme_carpani*2)

        tamam = ara("./images/tamam.png")
        vip = ara("./images/vip.png")
        iptal = ara("./images/iptal.png")
        
        time.sleep(bekleme_carpani*2)
        if tamam != -1:
            logkayit(farm,"bugday tamam 2 hata")
            click(btn,tamam[0],tamam[1])
            time.sleep(bekleme_carpani*2)
            click(btn,20, 65)
            time.sleep(bekleme_carpani*2)
            return "vip"
        elif iptal != -1:
            logkayit(farm,"bugday iptal 2 hata")
            time.sleep(bekleme_carpani*2)
            click(btn,iptal[0],iptal[1])
            time.sleep(bekleme_carpani*2)
            cancel = True
            continue
        elif vip != -1:
            logkayit(farm,"bugday vip 2 hata")
    
            return "vip"
        else:
            time.sleep(bekleme_carpani*1)    

def bul(btn):
    devredisi = ara("./images/devredisi.png")
    if devredisi != -1:
        click(btn,devredisi[0]+10,devredisi[1]+10)
        x = mesajtoplaoteki(btn)
        if x =="appopen":
            return "appopen"
    bulundu = -1
    for i in range(5):
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi_dunya == -1:
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
        else:
            break
    time.sleep(bekleme_carpani*2)
    girildi_dunya = ara("./images/girildi_dunya.png")
    if girildi_dunya == -1:
        return "appopen"
    
    for i in range(10):
        aranan = imagesearch.imagesearch("./images/altin.png",0.6)
        aranan2 = imagesearch.imagesearch("./images/altin2.png",0.6)
        if aranan[0] != -1:
            print(aranan)
            bulundu = aranan
            break
        if aranan2[0] != -1:
            print(aranan2)
            bulundu = aranan2
            break
    if(bulundu != -1):
        time.sleep(bekleme_carpani*2)
        click(btn,bulundu[0]+30,bulundu[1]+30)
        ilkkoordinat = [bulundu[0]+30,bulundu[1]+30]
        time.sleep(bekleme_carpani*2)
        raid = ara("./images/raid.png")
        detaylaraltin = ara("./images/detaylaraltin.png")
        if raid != -1 and detaylaraltin != -1:
            click(btn,detaylaraltin[0]+15,detaylaraltin[1]+15)
            time.sleep(bekleme_carpani*4)
            aramadeneme = ara("./images/aramadeneme.png",0.8)
            if aramadeneme == -1:
                click(btn,20,65)
                time.sleep(bekleme_carpani*2)
                bulundu =-1
                for i in range(10):
                    
                    aranan = imagesearch.imagesearch("./images/altin.png",0.6)
                    aranan2 = imagesearch.imagesearch("./images/altin2.png",0.6)
                    if aranan[0] != -1:
                        print(aranan)
                        bulundu = aranan
                        break
                    if aranan2[0] != -1:
                        print(aranan2)
                        bulundu = aranan2
                        break
                
                if bulundu != -1:
                    click(btn,bulundu[0]+30,bulundu[1]+30)
                    time.sleep(bekleme_carpani*2)
                else:
                    return "budegil"
                raid = ara("./images/raid.png")
                if raid != -1:
                    click(btn,raid[0]+15,raid[1]+15)
                    time.sleep(bekleme_carpani*2)
                    tamam = ara("./images/tamam.png")
                    vip = ara("./images/vip.png")
                    if vip != -1:
                        time.sleep(bekleme_carpani*2)
                        click(btn,20,65)
                        return "vip"
                    elif tamam != -1:
                        time.sleep(bekleme_carpani*2)
                        click(btn,20,65)
                        time.sleep(bekleme_carpani*2)
                        click(btn,20,65)
                        return "vip"
                        
                    
                    time.sleep(bekleme_carpani*2)
                    click(btn,300,590)
                    time.sleep(bekleme_carpani*2)
                    tamam = ara("./images/tamam.png")
                    if tamam != -1:
                        time.sleep(bekleme_carpani*2)
                        click(btn,20,65)
                        time.sleep(bekleme_carpani*2)
                        click(btn,20,65)
                        return "vip"
                print("başarılı")
                return "basarili"
            else:
                time.sleep(bekleme_carpani*2)
                click(btn,20,65)
                time.sleep(bekleme_carpani*2)
                return "budegil"
        else:
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(100,420,1)
            time.sleep(bekleme_carpani*2)
            raid = ara("./images/raid.png")
            detaylaraltin = ara("./images/detaylaraltin.png")
            if raid != -1 and detaylaraltin != -1:
                click(btn,detaylaraltin[0]+15,detaylaraltin[1]+15)
                time.sleep(bekleme_carpani*2)
                aramadeneme = ara("./images/aramadeneme.png",0.8)
                if aramadeneme == -1:
                    click(btn,20,65)
                    time.sleep(bekleme_carpani*2)
                    bulundu =-1
                    for i in range(10):
                        aranan = imagesearch.imagesearch("./images/altin.png",0.6)
                        aranan2 = imagesearch.imagesearch("./images/altin2.png",0.6)
                        if aranan[0] != -1:
                            print(aranan)
                            bulundu = aranan
                            break
                        if aranan2[0] != -1:
                            print(aranan2)
                            bulundu = aranan2
                            break
                    
                    if bulundu != -1:
                        click(btn,bulundu[0]+30,bulundu[1]+30)
                        time.sleep(bekleme_carpani*2)
                    else:
                        time.sleep(bekleme_carpani*2)
                        pyautogui.moveTo(100,420)
                        pyautogui.dragTo(ilkkoordinat[0],ilkkoordinat[1],1)
                        return "budegil"
                    raid = ara("./images/raid.png")
                    if raid != -1:
                        click(btn,raid[0]+15,raid[1]+15)
                        vip = ara("./images/vip.png")
                        if vip != -1:
                            time.sleep(bekleme_carpani*2)
                            click(btn,20,65)
                            return "vip"
                        time.sleep(bekleme_carpani*2)
                        click(btn,300,590)
                        time.sleep(bekleme_carpani*2)
                        tamam = ara("./images/tamam.png")
                        if tamam != -1:
                            time.sleep(bekleme_carpani*2)
                            click(btn,20,65)
                            time.sleep(bekleme_carpani*2)
                            click(btn,20,65)
                            return "vip"
                    return "basarili"
                else:
                    time.sleep(bekleme_carpani*2)
                    click(btn,20,65)
                    time.sleep(bekleme_carpani*2)
                    pyautogui.moveTo(100,420)
                    pyautogui.dragTo(ilkkoordinat[0],ilkkoordinat[1],1)
                    return "budegil"
            else:
                click(btn,200,200)
                time.sleep(bekleme_carpani*2)
                pyautogui.moveTo(100,420)
                pyautogui.dragTo(ilkkoordinat[0],ilkkoordinat[1],1)
                time.sleep(bekleme_carpani*2)

def altintopla(btn):
    girildi = ara("./images/girildi.png")
    if girildi != -1:
        sonrakidunya(btn)
        time.sleep(bekleme_carpani*2)
    girildi_dunya = ara("./images/girildi_dunya.png")
    if girildi_dunya == -1:
        logkayit(0,"appopen altintopla app ")
        return "appopen"
    time.sleep(bekleme_carpani*3)
    click(btn,200, 600)
    time.sleep(bekleme_carpani*2)
    click(btn,200, 600)
    time.sleep(bekleme_carpani*2)
    click(btn,165, 530)
    time.sleep(bekleme_carpani*2)
    click(btn,200, 170)
    time.sleep(bekleme_carpani*2)
    click(btn,125, 215)
    girildi_dunya = ara("./images/girildi_dunya.png")
    if girildi_dunya == -1:
        return "arkadasbos"
    
    time.sleep(bekleme_carpani*2)
    click(btn,200, 600)
    time.sleep(bekleme_carpani*2)
    click(btn,200, 600)
    time.sleep(bekleme_carpani*2)
    click(btn,250, 520)
    time.sleep(bekleme_carpani*3)
    click(btn,180,180)
    sol = 0
    yukari = 0
    sag = 0
    asagi = 0
    yanlis = 0
    for i in range(1,3):
        time.sleep(bekleme_carpani*2)
        if yanlis > 2:
            return "vip"
        for k in range((2*i)-1):#sol
            sol += 1
            pyautogui.moveTo(80,340)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(320,340,1)
            time.sleep(bekleme_carpani*2)
            x = bul(btn)
            if x == "vip":
                return "vip"
            elif x == "appopen":
                logkayit(0,"appopen altintopla app")
                return "appopen"
            elif x == "budegil":
                yanlis += 1
                time.sleep(bekleme_carpani*2)
            elif x == "basarili":
                yanlis = 0
                time.sleep(bekleme_carpani*2)
                click(btn,165, 530)
                time.sleep(bekleme_carpani*1)
                click(btn,200, 170)
                time.sleep(bekleme_carpani*1)
                click(btn,125, 215)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,250, 520)
                time.sleep(bekleme_carpani*3)
                click(btn,180,180)
                time.sleep(bekleme_carpani*3)
                for dikey in range(abs(yukari-asagi)):
                    if yukari>asagi:
                        pyautogui.moveTo(160,100)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,490,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(160,490)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,100,1)
                        time.sleep(bekleme_carpani*2)
                for yatay in range(abs(sol-sag)):
                    if sol>sag:
                        pyautogui.moveTo(80,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(320,340,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(245,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(5,340,1)
                        time.sleep(bekleme_carpani*2)
        for k in range((2*i)-1):#yukarı
            yukari += 1
            pyautogui.moveTo(160,100)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(160,490,1)
            time.sleep(bekleme_carpani*2)
            x = bul(btn)
            if x == "vip":
                return "vip"
            elif x == "appopen":
                logkayit(0,"appopen altintopla app")
                return "appopen"
            elif x == "budegil":
                yanlis += 1
                time.sleep(bekleme_carpani*2)
            elif x == "basarili":
                yanlis = 0
                time.sleep(bekleme_carpani*2)
                click(btn,165, 530)
                time.sleep(bekleme_carpani*1)
                click(btn,200, 170)
                time.sleep(bekleme_carpani*1)
                click(btn,125, 215)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,250, 520)
                time.sleep(bekleme_carpani*3)
                click(btn,180,180)
                time.sleep(bekleme_carpani*3)
                for dikey in range(abs(yukari-asagi)):
                    if yukari>asagi:
                        pyautogui.moveTo(160,100)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,490,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(160,490)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,100,1)
                        time.sleep(bekleme_carpani*2)
                for yatay in range(abs(sol-sag)):
                    if sol>sag:
                        pyautogui.moveTo(80,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(320,340,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(245,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(5,340,1)
                        time.sleep(bekleme_carpani*2)
        for k in range(2*i):#sag
            sag += 1
            pyautogui.moveTo(245,340)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(5,340,1)
            time.sleep(bekleme_carpani*2)
            x = bul(btn)
            if x == "vip":
                return "vip"
            elif x == "appopen":
                logkayit(0,"appopen altintopla app")
                return "appopen"
            elif x == "budegil":
                yanlis += 1
                time.sleep(bekleme_carpani*2)
            elif x == "basarili":
                yanlis = 0
                time.sleep(bekleme_carpani*2)
                click(btn,165, 530)
                time.sleep(bekleme_carpani*1)
                click(btn,200, 170)
                time.sleep(bekleme_carpani*1)
                click(btn,125, 215)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,250, 520)
                time.sleep(bekleme_carpani*3)
                click(btn,180,180)
                time.sleep(bekleme_carpani*3)
                for dikey in range(abs(yukari-asagi)):
                    if yukari>asagi:
                        pyautogui.moveTo(160,100)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,490,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(160,490)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,100,1)
                        time.sleep(bekleme_carpani*2)
                for yatay in range(abs(sol-sag)):
                    if sol>sag:
                        pyautogui.moveTo(80,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(320,340,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(245,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(5,340,1)
                        time.sleep(bekleme_carpani*2)
        for k in range(2*i):#aşşa
            asagi += 1
            pyautogui.moveTo(160,490)
            time.sleep(bekleme_carpani*2)
            pyautogui.dragTo(160,100,1)
            time.sleep(bekleme_carpani*2)
            x = bul(btn)
            if x == "vip":
                return "vip"
            elif x == "appopen":
                logkayit(0,"appopen altintopla app")
                return "appopen"
            elif x == "budegil":
                yanlis += 1
                time.sleep(bekleme_carpani*2)
            elif x == "basarili":
                yanlis = 0
                time.sleep(bekleme_carpani*2)
                click(btn,165, 530)
                time.sleep(bekleme_carpani*1)
                click(btn,200, 170)
                time.sleep(bekleme_carpani*1)
                click(btn,125, 215)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,200, 600)
                time.sleep(bekleme_carpani*2)
                click(btn,250, 520)
                time.sleep(bekleme_carpani*3)
                click(btn,180,180)
                time.sleep(bekleme_carpani*3)
                for dikey in range(abs(yukari-asagi)):
                    if yukari>asagi:
                        pyautogui.moveTo(160,100)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,490,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(160,490)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(160,100,1)
                        time.sleep(bekleme_carpani*2)
                for yatay in range(abs(sol-sag)):
                    if sol>sag:
                        pyautogui.moveTo(80,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(320,340,1)
                        time.sleep(bekleme_carpani*2)
                    else:
                        pyautogui.moveTo(245,340)
                        time.sleep(bekleme_carpani*2)
                        pyautogui.dragTo(5,340,1)
                        time.sleep(bekleme_carpani*2)

def gozcugonder(btn):
    kackisi = 0
    eskikackisi = 0
    kacincidayiz = 0
    kacincimesaj = 0
    girildi_dunya = ara("./images/girildi_dunya.png")
    if girildi_dunya == -1:
        logkayit(0,"appopen gozcu1")
        return "appopen"
    time.sleep(bekleme_carpani*2)
    click(btn,230,590)
    time.sleep(bekleme_carpani*2)
    click(btn,40, 110)
    while True:
        time.sleep(bekleme_carpani*2)
        bulundu = False
        gonderildi = False
        kackisi = 0
        mesaj = ara("./images/mesaj.png")
        if mesaj == -1:
            logkayit(0,"appopen gozcu 2")
            return "appopen"
        for kisi in range(9):
            x = pyautogui.pixel(40, 110+kisi*55)
            if x[0] >40 or x[1] >40 or x[2] >40:
                kackisi += 1 
        print(f"{kackisi} kisi bulundu")
        if kackisi == 0:
            eskikackisi = 0
            pyautogui.moveTo(200,200)
            pyautogui.dragTo(200,400,1)
            continue
        if eskikackisi == 0:
            print("ilk defa başladık")
            kacincidayiz = kackisi
            eskikackisi = kackisi
        elif kackisi != eskikackisi:
            print("yeni mesaj tespit edildi")
            
            kacincidayiz += 1
            eskikackisi = kackisi
        else:
            print(f"yeni mesaj yok {kacincidayiz}")
        time.sleep(bekleme_carpani*2)
        click(btn,40, 110+((kacincidayiz-1)*55))
        time.sleep(bekleme_carpani*2)
        click(btn,200,190+(kacincimesaj*78))
        time.sleep(bekleme_carpani*2)
        kacincimesaj += 1
        girildi_dunya = ara("./images/girildi_dunya.png")
        if girildi_dunya != -1:
            print("bulundu")
            
            bulundu = True
        else:
            print(f"fake mesaj {kacincidayiz-1}")
            click(btn,20, 65)
            time.sleep(bekleme_carpani*2)
            click(btn,300,595)
            time.sleep(bekleme_carpani*2)
            click(btn,40, 110+((kacincidayiz-1)*55))
            time.sleep(bekleme_carpani*2)
            click(btn,160,595)
            time.sleep(bekleme_carpani*2)
            click(btn,160,370)
            time.sleep(bekleme_carpani*2)
            click(btn,300,595)
            kacincidayiz -= 1
            kacincimesaj = 0
        if bulundu:
            time.sleep(bekleme_carpani*2)
            gozcu = ara("./images/gozcu.png")
            goc = ara("./images/goc.png")
            
            if goc != -1:
                print("göc varsa")
                time.sleep(bekleme_carpani*2)
                click(btn,goc[0]+10,goc[1]+10)
                time.sleep(bekleme_carpani*2)
                click(btn,220,315)
                time.sleep(bekleme_carpani*2)
                click(btn,160,375)
                time.sleep(bekleme_carpani*2)
                click(btn,230,590)
                time.sleep(bekleme_carpani*2)
                click(btn,40, 110)
            elif gozcu != -1:
                print("gozcu bulduk")
                time.sleep(bekleme_carpani*2)
                click(btn,gozcu[0]+10,gozcu[1]+10)
                time.sleep(bekleme_carpani*2)
                click(btn,120,400)
                time.sleep(bekleme_carpani*2)
                
                vip = ara("./images/vip.png")
                if vip!= -1:
                    vipbol = True
                    click(btn,20,65)
                    time.sleep(bekleme_carpani*2)
                    break
                time.sleep(bekleme_carpani*2)
                click(btn,120,120)
                time.sleep(bekleme_carpani*2)
                for i in range(20):
                    gozcu_kullan= ara("./images/gozcu_kullan.png")
                    time.sleep(bekleme_carpani*2)
                    print("gözcü bass")
                    if gozcu_kullan!= -1:
                        click(btn,gozcu_kullan[0]+10,gozcu_kullan[1]+10)
                        time.sleep(bekleme_carpani*2)
                    else:
                        break
                gonderildi = True
                print("gözcü bass sonrası")
            else:
                print("tanımsız")
                time.sleep(bekleme_carpani*2)
                click(btn,230,590)
                time.sleep(bekleme_carpani*2)
                click(btn,40, 110)
        if gonderildi:
            print("Başarıyla tamamlandı")
            time.sleep(bekleme_carpani*2)
            click(btn,230,590)
            time.sleep(bekleme_carpani*2)
            click(btn,40, 275)
            time.sleep(bekleme_carpani*2)
            click(btn,35, 110)
            time.sleep(bekleme_carpani*2)
            click(btn,310, 100)
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            click(btn,20,65)
            time.sleep(bekleme_carpani*2)
            click(btn,40, 110)
   
def sonrakihesap(btn,mail,sifre,hesapsayisi):
    global farm
    farmread= open("./data/data.txt")
    username = farmread.readline().rstrip()
    password = farmread.readline().rstrip()
    hesapsayisi = farmread.readline().rstrip()
    farmread.close()

    farmwrite = open("./data/data.txt","w")
    if farm == int(hesapsayisi) -1:
        farm = 0
        farmwrite.write(str(username).rstrip()+"\n")
        farmwrite.write(str(password).rstrip()+"\n")
        farmwrite.write(str(hesapsayisi).rstrip()+"\n")
        farmwrite.write(str("0").rstrip()+"\n")
    else:
        farm += 1
        farmwrite.write(str(username).rstrip()+"\n")
        farmwrite.write(str(password).rstrip()+"\n")
        farmwrite.write(str(hesapsayisi).rstrip()+"\n")
        farmwrite.write(str(farm).rstrip()+"\n")
    farmwrite.close()
    time.sleep(bekleme_carpani*2)
    time.sleep(bekleme_carpani*2)
    click(btn,20,75)
    for i in range(5):
        time.sleep(bekleme_carpani*2)
        ayarlar = ara("./images/ayarlar.png")
        if ayarlar != -1:
            imageclick(btn,"./images/ayarlar.png")
            break
        else:
            click(btn,20,65)
    time.sleep(bekleme_carpani*2)
    click(btn,290,585)
    time.sleep(bekleme_carpani*2)
    lonca = ara("./images/lonca.png")
    if lonca != -1:
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)
        click(btn,290,585)
        time.sleep(bekleme_carpani*2)
    imageclick(btn,"./images/hesaplar.png")
    time.sleep(bekleme_carpani*2)
    click(btn,50,150)
    time.sleep(bekleme_carpani*2)
    imageclick(btn,"./images/hesapdegistir.png")
    time.sleep(bekleme_carpani*2)
    click(btn,110,227)
    time.sleep(bekleme_carpani*2)
    click(btn,110,227)
    time.sleep(bekleme_carpani*2)

    for i in mail[farm]:
        if i == "@":
            pyautogui.hotkey("altright","q")
        else:
            pyautogui.write(i)
    time.sleep(bekleme_carpani*2)
    time.sleep(bekleme_carpani*2)
    click(btn,165,320)
    time.sleep(bekleme_carpani*2)
    click(btn,165,320)
    time.sleep(bekleme_carpani*2)
    click(btn,165,320)
    time.sleep(bekleme_carpani*2)
    time.sleep(bekleme_carpani*2)
    
    for i in sifre[farm]:
        if i == "@":
            pyautogui.hotkey("altright","q")
        else:
            pyautogui.write(i)
    time.sleep(bekleme_carpani*2)
    time.sleep(bekleme_carpani*2)
    click(btn,170,390)
    time.sleep(bekleme_carpani*2)
    click(btn,170,390)
    time.sleep(bekleme_carpani*2)
    hesap_giris_hata = ara("./images/hesap-giris-hata.png")
    if hesap_giris_hata != -1:
        click(btn,20,55)
        time.sleep(bekleme_carpani*2)
        time.sleep(bekleme_carpani*1)
        
        click(btn,20,55)
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)
        click(btn,20,65)
        time.sleep(bekleme_carpani*2)

    
    #stop
    

def main(btn,frm):
    send_heartbeat()
    global farm
    global username
    farmread = open("./data/data.txt")
    username = farmread.readline().rstrip()
    password = farmread.readline().rstrip()
    hesapsayisi = int(farmread.readline().rstrip())
    bu = farmread.readline().rstrip()
    farmread.close()
    now = datetime.datetime.now()
    log = f"{now.strftime("%d.%m.%Y %H:%M")} BOT BAŞLATILDI"
    try:
        r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/logs",json={"username":username,"log":log}, timeout=(3, 20))
    except:
        pass
    try:
        if bu =="":
            farm = 0
        else:
            farm = int(bu)
    except:
        farm = 0

    if farm > hesapsayisi:
        farm = 0
    farmwrite = open("./data/data.txt","w")
    farmwrite.write(str(username).rstrip()+"\n")
    farmwrite.write(str(password).rstrip()+"\n")
    farmwrite.write(str(hesapsayisi).rstrip()+"\n")
    farmwrite.write(str(farm).rstrip()+"\n")
    farmwrite.close()
    print("başla")

    global hesapgir
    hesapgir = True
    x = ""
    while True:
        try:
            send_heartbeat()
            data = collectdata()
            now = datetime.datetime.now()
            if x == "appopen":
                log = f"{now.strftime("%d.%m.%Y %H:%M")} Farm {farm}. ATLANDI"
                logkayit(farm, "ATLANDI")
                farmwrite = open("./data/data.txt","w")
            
                hesapgir = True
                if farm == data.get("hesapsayisi") -1:
                    farm = 0
                    farmwrite.write(str(username).rstrip()+"\n")
                    farmwrite.write(str(password).rstrip()+"\n")
                    farmwrite.write(str(hesapsayisi).rstrip()+"\n")
                    farmwrite.write(str("0").rstrip()+"\n")
                else:
                    farm += 1
                    farmwrite.write(str(username).rstrip()+"\n")
                    farmwrite.write(str(password).rstrip()+"\n")
                    farmwrite.write(str(hesapsayisi).rstrip()+"\n")
                    farmwrite.write(str(farm).rstrip()+"\n")
                try:
                    r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/logs",json={"username":username,"log":log}, timeout=(3, 20))
                except:
                    print("Atlandı")
                farmwrite.close()
            x = ""
            global btn_dur
            btn_dur = Button( text="Durdur",command= lambda:arawork(btn), height=2, width=10, background="IndianRed2",activebackground="IndianRed3",font=("Helvetica",10,"bold",))
            btn_dur.place(x=575,y = 455)

        
            btn.config(state=DISABLED)

            
            frame = None
            print(farm)
            if farm < 15:
                frame = frm[0]
            elif farm < 30:
                frame = frm[1]
            elif farm < 45:
                frame = frm[2]
            elif farm < 60:
                frame = frm[3]
            elif farm < 75:
                frame = frm[4]
            elif farm < 90:
                frame = frm[5]
            elif farm < 105:
                frame = frm[6]
            elif farm < 120:
                frame = frm[7]
            
            labeltime = Label(frame,text=now.strftime("%H:%M"),background="DarkSlateGray4", borderwidth=2, relief="groove",font='Helvetica 10 bold')
            labeltime.grid(row = (farm%15)+1,column = 5,ipadx = 15,ipady = 5)

            hesapsayisi = data.get("hesapsayisi") 
            kaynak_gonder = data.get("kaynak_gonder") 
            loncatech_yap = data.get("loncatech_yap") 
            ganimet_yap = data.get("ganimet_yap") 
            ic_kaynak_bonus = data.get("ic_kaynak_bonus") 
            dis_kaynak_bonus = data.get("dis_kaynak_bonus") 
            hazine_topla = data.get("hazine_topla") 
            lonca_topla = data.get("lonca_topla") 
            mesaj_topla = data.get("mesaj_topla") 
            hasat_et = data.get("hasat_et") 
            hizli_topla = data.get("hizli_topla") 
            tampon_hasat = data.get("tampon_hasat") 
            gonderilcekList = data.get("gonderilcekList") 
            gozculist = data.get("gozculist")
            askeregitlist = data.get("askeregitlist")
            kvk_kalkan = data.get("kvkkalkan")
            arttirici_al = data.get("arttirici_al")
            ifritlist = data.get("ifritlist")
            mail =data.get("mail")
            sifre = data.get("sifre")
            kaynakseviye = data.get("kaynakseviye")
            global bonusal
            bonusal = dis_kaynak_bonus

            global appopen
            appopen = False
            time.sleep(5)
            oyunac()
            x = hesapgiris(btn,mail,sifre)
            if x == "appopen":
                girdimi = cikis(btn)
                if girdimi == "girildi":
                    x = ""
                    continue
                else:
                    continue
            logkayit(farm,"Liman Yapılıyor")
            x = liman(btn)
            if x == "bulunamadi":
                pass
            

            if gozculist[farm]:
                sonrakidunya(btn)
                while True:
                    x = gozcugonder(btn)
                    if x == "appopen":
                        cikis(btn)
                        time.sleep(bekleme_carpani*5)
                        oyunac()
                        sonrakidunya(btn)
                        continue
                    
                

            if ic_kaynak_bonus:
                logkayit(farm,"İç Kaynak Bonus")
                x = ickaynakbonusu(btn,arttirici_al)
                if  x == "appopen":
                    cikis(btn)
                    continue
                if x == "limanyok":
                    pass


            if mesaj_topla:
                logkayit(farm,"Mesaj Topla")
                x = mesajtopla(btn)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        x = ""
                        pass
                    else:
                        continue
                
            if lonca_topla:     
                logkayit(farm,"Lonca Topla")
                x = loncatopla(btn,loncatech_yap)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        x = ""
                        pass
                    else:
                        continue
                if x == "lonca yok":
                    lonca_topla = False
                    loncatech_yap = False

            if loncatech_yap:
                logkayit(farm,"Lonca Tech")
                x = loncatek(btn)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        x = ""
                        pass
                    else:
                        continue
            
            if askeregitlist[farm] == "Max":
                logkayit(farm,"Asker Egit")
                x = trainsoldier(btn,False)
                if x == "appopen":
                    cikis(btn)
                    continue
            elif askeregitlist[farm] == "Tahil Arabasi":
                logkayit(farm,"Asker Egit")
                x =trainsoldier(btn,True)
                if x == "appopen":
                    cikis(btn)
                    continue

            if hazine_topla:
                logkayit(farm,"Hazine Topla")
                x = hazinetopla(btn,ganimet_yap)
                if x == "appopen":
                    cikis(btn)
                    continue

            if ganimet_yap:
                logkayit(farm,"Ganimet Karavani")
                x = ganimet_karavani(btn)
                if  x == "appopen":
                    cikis(btn)
                    continue
                if x == "gece":
                    pass

            if hizli_topla or tampon_hasat or hasat_et:  
                logkayit(farm,"Hızlı Tampon Hasat")
                hizlitamponhasat(btn,hizli_topla,tampon_hasat,hasat_et)
            
            kontrol = sonrakidunya(btn)
            send_heartbeat()
            if kontrol != "basarili":
                x = "appopen"
                logkayit(0, f"SONRAKİ DUNYA BAŞARISIZ")
                click(btn,300,300)
                cikis(btn)
                continue
            if ifritlist[farm]:
                while True:
                    x = ifrit(btn)
                    if x == "appopen":
                        cikis(btn)
                        oyunac()
                        for i in range(200):
                            time.sleep(bekleme_carpani*1)
                            girildi_dunya = ara("./images/girildi_dunya.png")
                            girildi = ara("./images/girildi.png")
                            xtus = ara("./images/xtus.png")
                            devredisi = ara("./images/devredisi.png")
                            click(btn,150, 440)
                            if devredisi != -1:
                                click(btn,devredisi[0]+10,devredisi[1]+10)
                            elif xtus != -1:
                                click(btn,xtus[0]+5,xtus[1]+5)
                            elif girildi != -1:
                                break
                            elif girildi_dunya != -1:
                                break
                        sonrakidunya(btn)
                        x = ""
                        continue
                    elif x =="energy":
                        pass
                    elif x == "vip":
                        pass
            if (kvk_kalkan):
                kvkkalkan(btn)

            if kaynak_gonder:
                x = kaynakgonder(btn)        
                if x == "appopen":
                    cikis(btn)
                    continue
                elif x =="vip":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
                elif x =="attack":
                    pass

            if gonderilcekList[farm] == "Bugday" or gonderilcekList[farm] == "Grain":
                logkayit(farm,"Bugday Gonderiliyor")
                x = askergonder(btn,0,kaynakseviye)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        hesapgir = False
                        sonrakihesap(btn,mail,sifre,hesapsayisi)
                        x = ""
                        continue
                    continue
                elif x == "exit":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
                elif x == "vip":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue

            if gonderilcekList[farm] == "Odun" or gonderilcekList[farm] == "Lumber":   
                logkayit(farm,"Odun GÖnderiliyor")
                x = askergonder(btn,1,kaynakseviye)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        hesapgir = False
                        sonrakihesap(btn,mail,sifre,hesapsayisi)
                        x = ""
                        continue
                    continue
                elif x == "exit":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
                elif x == "vip":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue

            if gonderilcekList[farm] == "Demir" or gonderilcekList[farm] == "Iron":   
                logkayit(farm,"Demir GÖnderiliyor")
                x = askergonder(btn,2,kaynakseviye)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        hesapgir = False
                        sonrakihesap(btn,mail,sifre,hesapsayisi)
                        x = ""
                        continue
                    continue
                elif x == "exit":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
                elif x == "vip":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue

            if gonderilcekList[farm] == "Kuvars" or gonderilcekList[farm] == "Quartz":  
                logkayit(farm,"Kuvars Gönderiliyor")
                x = askergonder(btn,3,kaynakseviye)
                if x== "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        hesapgir = False
                        sonrakihesap(btn,mail,sifre,hesapsayisi)
                        x = ""
                        continue
                    continue

                elif x == "exit":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue

                elif x == "vip":
                    
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
            if gonderilcekList[farm] == "Altin":
                x = altintopla(btn)
                if x == "vip":
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
                elif x == "appopen":
                    girdimi = cikis(btn)
                    if girdimi == "girildi":
                        hesapgir = False
                        sonrakihesap(btn,mail,sifre,hesapsayisi)
                        x = ""
                        continue
                    continue
                elif x == "arkadasbos":
                    click(btn,20,65)
                    hesapgir = False
                    sonrakihesap(btn,mail,sifre,hesapsayisi)
                    continue
            hesapgir = False
            sonrakihesap(btn,mail,sifre,hesapsayisi)
        except Exception as e:
            logkayit(0, f"Hata: {str(e)}")
            r = requests.post("https://us-central1-my-awesome-3e5e8.cloudfunctions.net/api/logs",json={"username":username,"log":str(e)}, timeout=(3, 20))
            continue
