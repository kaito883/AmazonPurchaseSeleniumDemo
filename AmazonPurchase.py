from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import csv
from selenium.webdriver.support.ui import Select

chromeOptions = webdriver.ChromeOptions()

SITE_LOGIN_URL = 'https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_custrec_signin&switch_account='
SITE_LOGIN_ID = '***'
SITE_LOGIN_PW = '***'

#Chrome driverの設定
##保存先のパス変更はココ↓
today = datetime.date.today()
todayString = today.strftime('%Y%m%d')
prefs = {"download.default_directory" : "C:\\Python\\Programing demo amazon\\download" + todayString}
chromeOptions.add_experimental_option("prefs",prefs)
##Chrome diriverのインストールパス
chromedriver = "C:\\driver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

#Web siteへのログイン
##ログインパスワードはよしなに。
def doLogin(SITE_LOGIN_URL, SITE_LOGIN_ID, SITE_LOGIN_PW):
	driver.get(SITE_LOGIN_URL)
	time.sleep(2)
	driver.find_element_by_name("email").clear()
	driver.find_element_by_name("email").send_keys(SITE_LOGIN_ID)
	driver.find_element_by_name("password").clear()
	driver.find_element_by_name("password").send_keys(SITE_LOGIN_PW)
	time.sleep(2)
	driver.find_element_by_id("signInSubmit").click()
	print('ログインプロセス完了しました。')
#/Web siteへのログイン

#サイト内検索し、商品を選択
def doSearchByKeyword(searchWord):
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[0])
	driver.find_element_by_name("field-keywords").clear()
	driver.find_element_by_name("field-keywords").send_keys(searchWord)
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='nav-search']//form//div[2]//div//input").click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="result_0"]/div/div[3]/div[1]/a').click()	
	print('検索プロセス完了しました。')

#商品詳細ページでカート投入
def addToCart():
	time.sleep(2)
	driver.find_element_by_id("add-to-cart-button").click()
	print('カート投入プロセス完了しました。')

def CompletePurchase():
	time.sleep(2)
	driver.get('https://www.amazon.co.jp/gp/buy/spc/handlers/display.html?hasWorkingJavascript=1')
	time.sleep(2)
	driver.find_element_by_name("placeYourOrder1").click()

#Main処理
doLogin(SITE_LOGIN_URL, SITE_LOGIN_ID, SITE_LOGIN_PW)
doSearchByKeyword('冷たい肉そば 山形')
driver.switch_to.window(driver.window_handles[1])
addToCart()
doSearchByKeyword('龍上海 山形')
driver.switch_to.window(driver.window_handles[2])
addToCart()
CompletePurchase()