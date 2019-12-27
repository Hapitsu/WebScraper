from selenium import webdriver

def loadPrices():
    url = 'https://www.nordpoolgroup.com/Market-data1/Dayahead/Area-Prices/FI/Hourly/?dd=FI&view=table'
    csvList = []
    headerList = ['']
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    print('Parsing data')

    for x in range(2, 10):
        try:
            element = browser.find_element_by_css_selector('#datatable > thead:nth-child(1) > tr:nth-child(1) > th:nth-child('+str(x)+')')
            headerList.append(element.get_attribute('innerHTML'))
        except:
            break
    print(headerList)
    csvList.append(headerList)
    
    for y in range(1, 32):
        priceList = []
        if(y!=25):
            for x in range(1, 10):
                try:
                    element = browser.find_element_by_css_selector('tr.data-row:nth-child('+str(y)+') > td:nth-child('+str(x)+')')
                    string = element.get_attribute('innerHTML')
                    if(x==1 and y<25):
                        string = string[:2] + '-' + string[-2:]
                    priceList.append(string)
                except:
                    break
            print(priceList)
            csvList.append(priceList)
            
    browser.quit()
    return csvList