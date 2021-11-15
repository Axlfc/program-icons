#!/usr/bin/env python
import os
import requests
import sys  # We need to read arguments
import time
import subprocess
from bs4 import BeautifulSoup 

def download_image(image_url, image_path):
    if image_url == "/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif":
        return False

    response = requests.get(image_url, stream=True)
    print("Downloading: ", image_url, " to ", image_path)

    if response.ok:
        with open(image_path, 'wb') as f:
            f.write(response.content)
            return True
    else:
        return False



# - Description: Downloads n icons using provided therm
# - Arguments: 
#    * Argument 1: Therm used to search for images
#    * Argument 2: Directory where we will create the directory containing the icons of this program
# - Output: List of program names
def download_icons(program_name, download_dir):
    directory = download_dir + "/" + program_name
    if not os.path.isdir(directory) and not os.path.exists(directory):
        os.makedirs(directory)
    
    web_server = "commons.wikimedia.org"
    pic_format = "svg"
    
    imgurl = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + program_name.replace("_", "+") + "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=" + web_server + "&safe=images&tbs=iar:s,ift:" + pic_format
    htmldata = requests.get(imgurl).text
    soup = BeautifulSoup(htmldata, 'html.parser')

    i = 0
    for image in soup.find_all('img'):
        current_image_path = directory + "/" + program_name + "_" + str(i)

        if download_image(str(image['src']), current_image_path):
            subprocess.check_call(['convert', '-background', 'none', '-define', 'icon:auto-resize=256,128,96,64,48,32,24,16', current_image_path, current_image_path + '.ico'])
        time.sleep(0.4)  # Limit network traffic
        i += 1


# - Description: Returns a list of key names regarding custom format in FEATURES.MD 
# - Arguments: 
#    * Argument 1: Path to file
# - Output: List of program names
def readKeyNames(file_path):
    keyname_list = []
    with open("FEATURES.md", "r") as features_file:
        for line in features_file.readlines():
            if line.count("|") != 6:
                continue
            if line.split("|")[1].count("-") > 6:
                continue
            if line.split("|")[1].strip() == "Name":
                continue

            keyname_list.append(line.split("|")[1].strip().replace(":", ""). replace(" ", "_"))
    return keyname_list


if __name__ == "__main__":
    if len(sys.argv) == 1:
        download_dir = "images"
        file_path = "FEATURES.md"
    elif len(sys.argv) == 2:
        download_dir = sys.argv[1]
        file_path = "FEATURES.md"
    else:
        download_dir = sys.arv[2]
        file_path = sys.argv[1]

    if not os.path.isdir(download_dir) and not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    program_names = readKeyNames(file_path)
    for program_name in program_names:
        download_icons(program_name, download_dir)
