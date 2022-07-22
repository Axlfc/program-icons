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


# - Description: Downloads 1 icon using provided term
# - Arguments: 
#    * Argument 1: Therm used to search for images
#    * Argument 2: Directory where we will create the directory containing the icons of this program
# - Output: List of pro
def download_icons(programName, download_dir, expectedFormat, webServer):
    directory = download_dir + "/" + programName
    if not os.path.isdir(directory) and not os.path.exists(directory):
        os.makedirs(directory)

    imgurl = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + programName.replace("_", "+") + "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=" + webServer + "&safe=images&tbs=iar:s,ift:" + expectedFormat
    htmldata = requests.get(imgurl).text
    soup = BeautifulSoup(htmldata, 'html.parser')

    i = 0
    for image in soup.find_all('img'):
        current_image_path = directory + "/" + programName + "_" + str(i)

        if download_image(str(image['src']), current_image_path):
            subprocess.check_call(
                ['convert', '-background', 'none', '-define', 'icon:auto-resize=256,128,96,64,48,32,24,16',
                 current_image_path, current_image_path + '.ico'])
        if i == 1:
            break
        i += 1


if __name__ == "__main__":
    program_example = "Audacity"
    web_server = "commons.wikimedia.org"
    pic_format = "svg"
    download_dir = "images"

    download_icons(program_example, download_dir, pic_format, web_server)
