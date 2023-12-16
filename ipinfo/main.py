import requests
import folium
import os
import time
import sys
import random
import colors
from colors import c, b, s

clear = lambda: os.system("clear")
clear()
print(c.blue + "IP INFO" + c.endc)
print("Developer: @soglopr")

def get_info_by_ip(ip="127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        st = str(response.get("status"))
        if st == "fail":
            print(c.red + "[!] Nothing could be found." + c.endc)
        else:
            data = {
                "[IP]": response.get("query"),
                "[Status]": response.get("status"),
                "[Country]": response.get("country"), 
                "[CountryCode]": response.get("countryCode"),
                "[Region]": response.get("region"),
                "[RegionName]": response.get("regionName"),
                "[City]": response.get("city"),
                "[Zip]": response.get("zip"),
                "[Latitude]": response.get("lat"),
                "[Longitude]": response.get("lon"),
                "[Timezone]": response.get("timezone"),
                "[Isp]": response.get("isp"),
                "[Org]": response.get("org"), 
                "[As]": response.get("as")
            }
            print()
            for k, v in data.items():
                print(c.green + f"{k}:" + c.orange + f" {v}" + c.endc)
            what = input(str("[#] Do I need to save the coordinates? (y/n): "))
            if what == "y" or what == "Y":
                ip_map = f'{response.get("query")}_{response.get("country")}'
                area = folium.Map(location=[response.get("lat"), response.get("lon")])
                area.save(f'{ip_map}.html')
                if not os.path.isdir("Maps"):
                    os.mkdir("Maps")
                os.replace(f'{ip_map}.html', f'Maps/{ip_map}.html')
            elif what == "n" or what == "N":
                pass
            else:
                print(c.red + "[!] You clicked on the wrong symbol!" + c.endc)
    except requests.exceptions.ConnectionError:
        print(c.red + "[!] Check your internet connection!" + c.endc)
           
def main():
    print()
    ip = input(c.yellow + "[Input]" + c.endc + " >> ")
    if ip == "Cl" or ip == "cl" or ip == "Clear" or ip == "clear":
        clear()
        print(c.blue + "IP INFO" + c.endc)
        print("Developer: @soglopr")
    else:
        get_info_by_ip(ip=ip)
     
if __name__ == "__main__":
    while True:
        main()