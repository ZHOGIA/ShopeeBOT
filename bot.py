from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import datetime
import time

link_produk = time_target=None
sekarang = datetime.datetime.now()

def Banner() :
    print('╭━━━┳╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╭━━╮')
    print('┃╭━╮┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╭╯╰╮╱╱╱┃╭╮┃')
    print('┃╰━━┫╰━┳━━┳━━┳━━┳━━╮┃┃╱┃┣╮┣╮╭╋━━╮┃╰╯╰┳╮╭┳╮╱╭╮')
    print('╰━━╮┃╭╮┃╭╮┃╭╮┃┃━┫┃━┫┃╰━╯┃┃┃┃┃┃╭╮┃┃╭━╮┃┃┃┃┃╱┃┃')
    print('┃╰━╯┃┃┃┃╰╯┃╰╯┃┃━┫┃━┫┃╭━╮┃╰╯┃╰┫╰╯┃┃╰━╯┃╰╯┃╰━╯┃')
    print('╰━━━┻╯╰┻━━┫╭━┻━━┻━━╯╰╯╱╰┻━━┻━┻━━╯╰━━━┻━━┻━╮╭╯')
    print('╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃')
    print('╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯')
    print('')
    print('(c) XOGDEV (https://github.com/XOGDEV)')
    print('(!) Instagram @zhogia')
    print('')

def InputData() :
    global link_produk,time_target,sekarang
    link_produk = input('(#) Link Produk Shopee : ')
    ### Jam keberapa
    jam = int(input('(#) Jam Beli : '))
    ### Menit keberapa
    menit = int(input('(#) Menit Beli : '))
    ### Detik keberapa
    detik = int(input('(#) Detik Beli : '))
    time_target=datetime.datetime(sekarang.year,sekarang.month,sekarang.day,jam,menit,detik)

def SetupSelenium():
    ### Inisialisasi Awal
    #binary=FirefoxBinary('System/Mozilla/firefox.exe')
    binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\firefox.exe')
    selenium = r'System/Mozilla/geckodriver.exe'

    ### Setup Profil
    firefox_profile = webdriver.FirefoxProfile('System/Profile')

    ### Buka Browser
    browser = webdriver.Firefox(executable_path=selenium,firefox_binary=binary,firefox_profile=firefox_profile)

    ### Clear Cache & Cookie
    browser.delete_all_cookies()
    
    return browser

def click(browser,element_css):
    WebDriverWait(browser, 60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    browser.find_element_by_css_selector(element_css).click()

Banner()
InputData()
browser = SetupSelenium()
# buka halaman login
browser.get("https://shopee.co.id/buyer/login")
wait = WebDriverWait(browser, 60)
print('(#) Login... ')

# cek udah login
WebDriverWait(browser, 120).until(
    ec.visibility_of_element_located((By.CSS_SELECTOR, '.shopee-avatar__img'))
)

# buka produk
browser.get(link_produk)

# delay Waktu
selisih = time_target-datetime.datetime.now()
print('(#) Harap Menunggu... ')
time.sleep(selisih.seconds)
browser.refresh()
print('(#) Browser Refresh... ')

# Varian
click(browser, '#main > div > div._193wCc > div.page-product > div.container > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div._2nr4HE > div > div.flex._3AHLrn._2XdAdB > div > div:nth-child(1) > div > button:nth-child(5)')

# Button Beli
click(browser,'button.btn--l:nth-child(2)')
WebDriverWait(browser, 60).until(
    ec.invisibility_of_element((By.CSS_SELECTOR, '.action-toast'))
)

# Button checkout
click(browser,'.shopee-button-solid')
WebDriverWait(browser, 60).until(
    ec.invisibility_of_element((By.CSS_SELECTOR, '.loading-spinner-popup'))
)

# Metode Ubah Pengiriman
#click(browser,'._26DEZ8')
#click(browser,'div.stardust-radio:nth-child(2)')
#click(browser,'.-T3OGq')
#WebDriverWait(browser, 60).until(
#    ec.invisibility_of_element((By.CSS_SELECTOR, '.loading-spinner-popup'))
#)

# Metode Pembayaran
click(browser,'.checkout-payment-setting__payment-methods-tab > span:nth-child(1) > button:nth-child(1)')
#click(browser,'div.bank-transfer-category:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
WebDriverWait(browser, 60).until(
    ec.invisibility_of_element((By.CSS_SELECTOR, '.loading-spinner-popup'))
)
print('(#) Berhasil Menggunakan Metode Pembayaran ShopeePay ')

# Buat Pesanan
click(browser,'.stardust-button')
print('(#) Barang Berhasil dibeli ')
browser.delete_all_cookies()
time.sleep(5)
print('(#) Cookies Berhasil diBersihkan... ')
time.sleep(5)
exit()