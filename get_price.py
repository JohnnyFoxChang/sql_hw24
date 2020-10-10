import time
from selenium import webdriver
from bs4 import BeautifulSoup

def add_row(row_list,name,price,supplier):
    data = {}
    data['name'] = name
    data['price'] = price
    data['supplier'] = supplier
    data['time'] = time.strftime("%Y/%m/%d %H:%M")
    row_list.append(data)
    return row_list

#大潤發抓取價格
def price_rtmart(name):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://www.rt-mart.com.tw/direct/')
    search_input = driver.find_elements_by_css_selector('#product_keyword')[0]
    search_btn = driver.find_elements_by_css_selector('#btn_submit')[0]
    search_input.send_keys(name)
    search_btn.click()
    time.sleep(10)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    #商品包裝在 class= 'indexProList' 內
    items = soup.select('.indexProList')  
    #設定寫檔列表  
    row_list = []
    for item in items:
        #商品名稱包裝在 class= 'for_proname' 內
        name = item.select('.for_proname')[0].text.strip().replace('\n','')
        #商品名稱包裝在 class= 'for_priceboxe' 內, 有時會有原價和折扣價, 只要記錄折扣價即可
        price_text = item.select('.for_pricebox')[0].text
        if '$' in price_text:
            price = int(price_text.split('$')[-1])
        else:
            price = 99999999
        row_list = add_row(row_list,name,price,'大潤發')
    driver.quit()
    return row_list

#取得頂好價格
def price_wellcome(name):
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://sbd-ec.wellcome.com.tw/product/listByKeyword?searchCategoryId=all&skeyword='+ name
    driver.get(url)    
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    #商品包裝在 class= 'item' 內
    items = soup.select('.item')  
    #設定寫檔列表  
    row_list = []
    for item in items:
        #商品名稱包裝在 class= 'item-name' 內
        name = item.select('.item-name')[0].text.strip().replace('\n','')
        #商品名稱包裝在 class= 'item-price' 內
        price_text = item.select('.item-price')[0].text
        price = int(price_text)        
        row_list = add_row(row_list,name,price,'頂好')
    driver.quit()
    return row_list  

#取得大買家價格
def price_savesafe(name):
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://www.savesafe.com.tw/Products/SearchList.aspx?k='+ name + '&ssid=0'
    driver.get(url)    
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    #商品包裝在 class= 'SSet_txt' 內
    items = soup.select('.SSet_txt')  
    #設定寫檔列表  
    row_list = []
    for item in items:
        #商品名稱包裝在 class= 'SSet_name' 內
        name = item.select('.SSet_name')[0].text.strip().replace('\n','')
        #商品名稱包裝在 class= 'SSet_price' 內 
        price_text = item.select('.SSet_price')[0].text
        price = int(price_text)
        row_list = add_row(row_list,name,price,'大買家')
    driver.quit()
    return row_list


#取得家樂福價格
def price_carrefour(name):
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://online.carrefour.com.tw/tw/search?key='+ name + '&categoryId='
    driver.get(url)    
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    #商品名稱和價格分別包裝在 class= 'commodity-desc' 和 'current-price' 內
    names = soup.select('.commodity-desc')
    prices = soup.select('.current-price')
    #設定寫檔列表  
    row_list = []

    for i in range(0,len(names)):      
        name = names[i].text.strip().replace('\n','')        
        price_text = prices[i].text
        if '$' in price_text:
            price = int(price_text.split('$')[-1])
        else:
            price = 99999999        
        row_list = add_row(row_list,name,price,'家樂福')
    driver.quit()
    return row_list    

#取得愛買價格
def price_feamart(name):
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://shopping.friday.tw/ec2/search?device=desktop&rows=20&page=1&keyword='+ name + '&sid=699'
    driver.get(url)    
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    #商品包裝在 class= 'ga-event singleprod ' 內
    #商品名稱和價格分別包裝在 class= 'commodity-desc' 和 'current-price' 內
    names = soup.select('.prod_name')
    prices = soup.select('.prod_price')
    #設定寫檔列表  
    row_list = []
    for i in range(0,len(names)):      
        name = names[i].text.strip().replace('\n','')        
        price_text = prices[i].text
        price = int(price_text)
        row_list = add_row(row_list,name,price,'愛買')
    driver.quit()
    return row_list    