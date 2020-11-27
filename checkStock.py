import sys,re,requests,argparse,time,calendar#,urllib
from lxml import html
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup

parser=argparse.ArgumentParser()
parser.add_argument('-start','--start',help="Epoch format 1603825200 =10/27",required=False)
parser.add_argument('-end','--end',help="Epoch format 1604343600 =11/2",required=False)
parser.add_argument('-delta',help="604800 ,one week incremental")
args=parser.parse_args()

#def Reserve(UID):

#def getLogin(UID):
  
def BestBuy(model_number):
  target = ("https://www.bestbuy.com/button-state/api/v5/button-state?skus=%s&conditions=&storeId=&destinationZipCode=&context=pdp&consolidated=false&source=buttonView&xboxAllAccess=false") %model_number
  
  headers= {
  #'GET':'/button-state/api/v5/button-state?skus=6429442&conditions=&storeId=&destinationZipCode=&context=pdp&consolidated=false&source=buttonView&xboxAllAccess=false HTTP/1.1',
  'Host': 'www.bestbuy.com',
  'Connection': 'close',
  'Accept': 'application/json',
  'X-CLIENT-ID': 'FRV',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
  'X-REQUEST-ID': 'BROWSE',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442&ref=186&loc=nvidia_6429442',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'en-US,en;q=0.9',
  }
  cookies= {
 'UID':'fab1758b-b418-4f7f-a87e-01d0e37ec828',
 'pst2':'851|N', 'physical_dma':'807', 'customerZipCode':'95050|N', 'ltc':'20', 'oid':'1483169735', 'vt':'99d07853-3008-11eb-9fb1-0a1f17ca9b6f', 
 'partner':'186%26nvidia_6429442%262020-11-26+10%3a58%3a26.000', 
 'bm_sz':'284D6F9E6970C16902B546956C569237~YAAQj3tBF5iIqvh1AQAAcOh9BQm0NWTx3yV4hH7UujnJO8B/PXQ2yc8PdeLBX4hq8Y+uCdqsWBAABXoPdhoZ3kD3/5+++8ZBlLdYiUsNjCGrMU0lqZUw+GWG1wsNdVECLsshkZ+DWnUpjh/CFF32lFJpIx+Qn/XIz8lV46+bNh33K7I09vZZe8/8pA6YfLmjCg==', 'bby_rdp':'l', 'bby_cbc_lb':'p-browse-w', 
  'CTT':'6d52cdc5720cb48d78f878966bfaf96a', 'SID':'40feae25-2554-4a17-a268-36647b1bc5b6', 'optimizelyEndUserId':'oeu1606409907742r0.5218536508470109', 
  'dtCookie':'20$OB9JGU8980DJ082JSP5HG5B45LAEUNUR', 'rxVisitor':'160640990797139LHBAVNBS7CHBBO043VLRNHGQRVIIB1', 'dtSa':'dtLatC:80', 
  'rxvt':'1606411708022|1606409907981', 'dtPC':'20$209907943_418h1vUTHTAASEWPHUPRMCAAHBPECUOJQOJBMI-0e1', 'COM_TEST_FIX':'2020-11-26T16%3A58%3A30.105Z', 
  '_abck':'645112C549477A69E9BAB817EC3268FE~-1~YAAQhntBF2EJwN91AQAA6gF+BQQQMr/cKm9MGNAK8yHtCj/uNmLoQh1bsnNJ8fo+0hDuJTKTQBQJsQcldAJAQPw4bsDSh0lvoOqRGRw4T5TkePcYNkpCVI4j6w+V7nzTnpWRFz5IpR1Yl8uRHwaC0JXdPf4YIbKL2MfFdGQ0hEaztLplId1DBqz2SaQc94opJXi2wpJe3xaV6liAn313iP8e9jl1cKo2BPM/G9ncoTY7Erp3GrSnbV0p7qeg8AA9aVxPXpU5oS8yNtOG4KRSAXjXxvpBOvj0KKf6j80SjEqI8KASaiQALDTntZYD0iIpaM35MF6cbrcx~-1~||1-HygykynXTZ-1-10-1000-2||~-1', 'CTE22':'T'
  }

  #try:
  r = requests.get(target,headers=headers, cookies=cookies)
  s = BeautifulSoup(r.text, 'lxml')
  print( "[+] Checking %s on BestBuy") %model_number
  ExtractHref = re.search(r'(.*SOLD_OUT.*)',str([ _ for _ in s ]).replace("{","\n").replace("}","\n")) # Extrct between {} :
  #print(s.prettify())
  if ExtractHref:
        print("[-] "+ str(ExtractHref.group(1)))
        print('\n')
        #time.sleep(1)
  else:
        print("URL: https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442&ref=186&loc=nvidia_6429442 ")
  error = re.search("Invalid argument", s.text)
  if error:
    print("[-] Error found in response")
  return#(UID.group(1))


def NewEgg(model_number):
  target = ("https://www.newegg.com/%s") %model_number 


  headers = {
  #'GET':'/evga-geforce-rtx-3070-08g-p5-3751-kr/p/N82E16814487528?cm_mmc=vendor-nvidia HTTP/1.1',
  'Host':'www.newegg.com',
  'Connection':'close',
  'Upgrade-Insecure-Requests':'1',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site':'cross-site',
  'Sec-Fetch-Mode':'navigate',
  'Sec-Fetch-User':'?1',
  'Sec-Fetch-Dest':'document',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'en-US,en;q=0.9',
  }
  cookies={}
  r = requests.get(target,headers=headers, cookies=cookies)
  s = BeautifulSoup(r.text, 'lxml')
  #print( "[+] Checking %s on NewEgg") %(re.search(r'(.*geforce.*)',str([ _ for _ in model_number])))
  print( "[+] Checking %s on NewEgg") %(model_number.strip('/'))
  ExtractHref = re.search(r'(availability.*OutOfStock)',str([ _ for _ in s ]).replace("{","\n").replace("}","\n")) # Extrct between {} :
  #print(s.prettify())
  if ExtractHref:
        print("[-] "+ str(ExtractHref.group(1)))
        print('\n')
        #time.sleep(1)
  else:
        print("URL: "+target)
  error = re.search("Invalid argument", s.text)
  if error:
    print("[-] Error found in response")
  return#(UID.group(1))

BestBuy(6429442)
BestBuy(6429440)

NewEgg("zotac-geforce-rtx-3070-zt-a30700e-10p/p/N82E16814500501?cm_mmc=vendor-nvidia")
NewEgg("asus-geforce-rtx-3070-dual-rtx3070-8g/p/N82E16814126460?cm_mmc=vendor-nvidia")
NewEgg("evga-geforce-rtx-3070-08g-p5-3751-kr/p/N82E16814487528?cm_mmc=vendor-nvidia")
NewEgg("asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?cm_mmc=vendor-nvidia")
NewEgg("msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?cm_mmc=vendor-nvidia")
NewEgg("zotac-geforce-rtx-3080-zt-a30800d-10p/p/N82E16814500502?cm_mmc=vendor-nvidia")
NewEgg("gigabyte-geforce-rtx-3080-gv-n3080eagle-oc-10gd/p/N82E16814932330?cm_mmc=vendor-nvidia")
NewEgg("evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522?cm_mmc=vendor-nvidia")
NewEgg("zotac-geforce-rtx-3080-zt-t30800j-10p/p/N82E16814500504/?cm_mmc=vendor-nvidia")
NewEgg("msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?cm_mmc=vendor-nvidia")
NewEgg("asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?cm_mmc=vendor-nvidia")
NewEgg("gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329?cm_mmc=vendor-nvidia")
