from bs4 import BeautifulSoup
import urllib
import urllib.request

#For Extracting Url
import tldextract


from urllib.parse import urlparse
# from urlparse import urlparse  # Python 2

a=[]
o=[]
o2=[]
mainArray=[]
k=[]
UrlList=[]
inputUrl=input("Enter Url:")
resp = urllib.request.urlopen(inputUrl)
#https://www.publicationprinters.com/clients.html
#http://ilp.mit.edu/webpub.jsp
#http://www.msrit.edu/department/ise.html
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    a.append(link['href'])


#print (type(a[0]))
for item in a:
    if ".pdf" in item:
        o.append(str(item))

print(o)


for item in o:
    if not (("http") or ("https")) in item:
        o2.append(str(item))


list = tldextract.extract(inputUrl)
domain_name = list.domain + '.' + list.suffix
MainUrl=list.subdomain+'.'+domain_name

#print(o)
for item in o2:
    if (item[0]=="/"):
        DownloadableUrl=MainUrl+item
        UrlList.append(DownloadableUrl)
    else:
        DownloadableUrl=MainUrl+"/"+item
        UrlList.append(DownloadableUrl)

#print (UrlList)

#Download From UrlList

k=1

for item in UrlList:
    data=urllib.request.urlretrieve ("http://"+ item, str(k) + ".pdf")
    print (item)
    k=k+1



#parsed_uri = urlparse("http://ilp.mit.edu/webpub.jsp" )
#print (type(parsed_uri))
#resultUrl = "{uri.scheme}://{uri.netloc}/".format(uri=parsed_uri)
#result=str(resultUrl)


#print (result)

#print(type(result))
#q="http://ilp-www.mit.edu"

#print(type(q))
#for item in o:
#    if result not in item:
#        print(type(item))
#        k.append(item)
        
#print (o)

#print ("\n\n\n")
#print (k)
