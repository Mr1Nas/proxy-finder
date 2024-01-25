from bs4 import BeautifulSoup
import pandas as pd
import requests
from icecream import ic
import colorama
from tabulate import tabulate
from prettytable import PrettyTable
# t = PrettyTable(['Name','Family','Phone']) 
# listm = ['s','ss']
# p = ['nim',listm,'tim']
# m = ['amin','ali','ahmad']
# t.add_row(p)
# t.add_row(m)
# print(t)


port = input(colorama.Fore.YELLOW+"ENTER PORT:")
type_of_proxy = input(colorama.Fore.GREEN+"ENTER TIPE OF PROXY (example:http) :")
speed = input(colorama.Fore.YELLOW+"ENTER PROXY SPEED:")
page= input("ENTER PAGE OF PROXY(default = 1):")
if page == "":
    page = 1

print("""██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗        ███╗   ███╗██████╗         ███╗   ██╗ █████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝        ████╗ ████║██╔══██╗        ████╗  ██║██╔══██╗██╔════╝
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝         ██╔████╔██║██████╔╝        ██╔██╗ ██║███████║███████╗
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝          ██║╚██╔╝██║██╔══██╗        ██║╚██╗██║██╔══██║╚════██║
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████╗██║ ╚═╝ ██║██║  ██║███████╗██║ ╚████║██║  ██║███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                                                       """)
x = f"https://www.freeproxy.world/?type{type_of_proxy}=&anonymity=&country=&speed={speed}&port={port}&page={page}"
response = requests.get(x)
parser = BeautifulSoup(response.text , "html.parser")
post = parser.find_all("td",attrs={"class":"show-ip-div"})
# ic(post)
proxy_list=[]
for i in range(1,12):
    proxy_list.append(post[i])
print(proxy_list)
ic(len(proxy_list))
x = proxy_list[0]
# x = str(x)
# print(x[24:-5])
list_prox = []
for i in range(1,11):
    m = proxy_list[i]
    m = str(m)
    s = m[24:-5]
    list_prox.append(s)
ic(list_prox)
list_port = [port,port,port,port,port,port,port,port,port,port,port,port]
list_server =[type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy,type_of_proxy]
for i in range(0,11):
    my_table= PrettyTable(['ip','port','server'])
    ip_table = [list_prox[i],list_port[i],list_server[i]]
    my_table.add_row(ip_table)
    print(my_table)