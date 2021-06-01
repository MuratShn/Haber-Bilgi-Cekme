import requests
from bs4 import BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
isim = input("Kişinin tam ismini ismini giriniz (Elon Musk vs.) : ")

def wiki(isim):
    isim = isim.title().split()

    for i in range (len(isim)):
        if(isim[-1] == isim[i]):
            continue
        isim[i] = isim[i] +"_"
    isim = "".join(isim)

    
    response = requests.get(f"https://tr.wikipedia.org/wiki/{isim}") #wiki
    if(response.ok):
        print("KİŞİNİN BİOGRAFİSİ")
        print("*"*50+"")
        soup = BeautifulSoup(response.content,"html.parser")
        bio = soup("table",{"class": "infobox"})
        for i in bio:
            h = i.find_all("tr")
            for j in h:
                baslık = j.find_all("th")
                icerik = j.find_all("td")
                if(baslık is not None and icerik is not None):
                    for x,y in zip(baslık,icerik):
                        y = (y.text).strip()
                        x = x.text
                        print (x + "::" + y)
    else:
        print("Wikipediada kayıt bulunamamıştır")
    
    print("\n\nKİŞİNİN ÖZGEÇMİŞİ")
    print("*"*50+"")
    
    
    
    bilgi = soup.find("p").text
    for i in range(30):
        y = f"[{i}]"
        if ( y in bilgi ):
            bilgi = bilgi.replace(y,"")
    
    print(bilgi)
    
def bbc(isim):
    driver = webdriver.Chrome(r"C:\Users\murat\Desktop\AA\PYTHON\Selenium\chromedriver")

    driver.get("https://www.bbc.com/news")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='orb-search-q']").send_keys(isim)
    driver.find_element_by_css_selector("#orb-search-button").click()
    try:
        driver.find_element_by_xpath("//*[@id='main-content']/div[1]/div[3]/div/div/ul/li[1]/div/div/div[1]/div[1]/a").click()
        time.sleep(1)
        baslık = driver.find_element_by_css_selector("#main-heading")
        icerik = driver.find_elements_by_css_selector("p")

        baslık = baslık.text.upper()
        iceri = ""
        for i in range(5):
            iceri += icerik[i].text
        driver.close()
        return print(f"----------------{baslık}----------------\n{iceri}")
    except:
        driver.close()
        return "BBC de haber bulunamadı"

wiki(isim)
print("\n\n")
bbc(isim)

print("**"*50)





