#!/usr/bin/env python
import os
import requests
import magic
import time

from bs4 import BeautifulSoup 


def download_image(image_url, image_path):
    if not image_url == "/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif":
        response = requests.get(image_url, stream=True)
        print("Downloading: ", image_url, " to ", image_path)
        #print("")
        if response.ok:
            with open(image_path, 'wb') as f:
                f.write(response.content)


def getdata(url):
    # r = requests.get(url, verify=False) 
    r = requests.get(url) 
    return r.text 


# Prepare lists of features
def main():
    o = open("FEATURES.md", "r")
    num_user_features = ""
    num_root_features = ""
    num_total_features = ""

    try:
        with open("FEATURES.md", "r") as o:
            lines = o.readlines()

        with open("FEATURES.md", "r") as q:
            first_line = q.readline().split("features")
            for i in first_line[0]:
                if i.isdigit():
                    num_user_features = num_user_features + str(i)
            for i in first_line[1]:
                if i.isdigit():
                    num_root_features = num_root_features + str(i)
            for i in first_line[2]:
                if i.isdigit():
                    num_total_features = num_total_features + str(i)
            q.close()
    finally:
        o.close()

    num_user_features = int(num_user_features)
    num_root_features = int(num_root_features)
    num_total_features = int(num_total_features) 

    features = []
    user_features = []
    root_features = []

    for i in lines:
        features.append(i)

    a = 5
    b = num_user_features + a
    for i in range(a, b):
        user_features.append(features[i] + "\n")

    b = user_features.index(user_features[-2]) + 12
    for i in range(b, len(features)):
        root_features.append(features[i] + "\n")


    user_features_names = []
    for i in range(len(user_features)):
        user_features_names.append(user_features[i].split("|"))
    del user_features_names[-1]
    user_feature_names = []
    for i in user_features_names:
        user_feature_names.append(i[1])

    root_features_names = []
    for i in range(len(root_features)):
        root_features_names.append(root_features[i].split("|"))
    del root_features_names[-1]
    root_feature_names = []
    for i in root_features_names:
        root_feature_names.append(i[1])

    # Trim software folder names
    for i in range(len(root_feature_names)):
        for j in root_feature_names[i]:
            # Respect Code::Blocks
            if j == ":" or j == "/" or j == "\\" or j == "*" or j == "?" or j == "\"" or j == "<" or j == ">" or j == "|" or j == "`":
                root_feature_names[i] = root_feature_names[i].replace(":", "").replace("/", "").replace("\\", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "").replace("`", "")
        root_feature_names[i] = root_feature_names[i][1:]
    for i in range(len(user_feature_names)):
        for j in user_feature_names[i]:
            if j == ":" or j == "/" or j == "\\" or j == "*" or j == "?" or j == "\"" or j == "<" or j == ">" or j == "|" or j == "`":
                user_feature_names[i] = user_feature_names[i].replace(":", "").replace("/", "").replace("\\", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "").replace("|", "").replace("`", "")
        user_feature_names[i] = user_feature_names[i][1:]
    #Prepare folder structures

    main_dir = [user_feature_names, root_feature_names]
    root_folder_dir = "images"
    main_dir_names = ["user", "root"]
    for i in range(len(main_dir)):
        for j in range(len(main_dir[i])):
            dirName = str(root_folder_dir) + '/' + str(main_dir_names[i]) +'/' + str(main_dir[i][j])[:-1]
            # Create target Directory if don't exist
            try:
                os.makedirs(dirName.replace(" ", "_"))
                #print("Directory ", dirName,  " Created ") 
            except:
                #print("Directory ", dirName,  " already exists")
                pass
    
    '''   
    for i in url_list:
        print(i)
    '''
    picture_names = []
    picture_paths = []
    for i in user_feature_names:
        pic_name = i[:-1] + "_icon.svg"
        pic_path = "images/user/" + i[:-1] + "/"
        picture_names.append(pic_name)
        picture_paths.append(pic_path.replace(" ", "_"))
    # print(picture_names, picture_paths)
    user_pictures = picture_names.extend(picture_paths), picture_names.extend(picture_names)
    #print(user_pictures)

    for i in range(len(user_feature_names)):
        #print(user_feature_names[i])
        #print(picture_paths[i])
        pass

    
    web_server = "wikipedia.org"
    #feature_name = "whatsapp"
    pic_format = "svg"
    #download_image_url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + feature_name + "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=" + web_server + "&safe=images&tbs=iar:s,ift:" + pic_format
    mime = magic.Magic(mime=True)

    
    #pic_url = "http://google.com/favicon.ico"
    #current_dir = os.getcwd()
    #pic_path = current_dir + "/images/user/Google/"
    url_list = []
    for i in range(len(picture_paths)):
        # Elaborate url repartition, almost done
        imgurl = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + user_feature_names[i][:-1].replace(" ", "+") + "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=" + web_server + "&safe=images&tbs=iar:s,ift:" + pic_format
        htmldata = getdata(imgurl)
        soup = BeautifulSoup(htmldata, 'html.parser')
        u = 1
        for item in soup.find_all('img'):
            url_list.append(item['src'])
            #print(item['src'])
            pic_path = picture_paths[i] + picture_names[i][:-4] + "_" + str(u) + picture_names[i][-4:]
            for img in os.listdir(str(picture_paths[i])):
                if mime.from_file(picture_paths[i] + img) != pic_format:
                    pic_path = picture_paths[i] + picture_names[i][:-4] + "_" + str(u) + picture_names[i][-4:][:-3] + mime.from_file(picture_paths[i] + img).replace("image/", "")
            download_image(str(item['src']), pic_path)
            time.sleep(0.4)
            u += 1
    
    # Solve right mimetype of images
    '''
    example_path = "images/user/Function a/"
    print(os.listdir(example_path))
    for img in os.listdir(example_path):
        if mime.from_file(example_path + img) != pic_format:
            print(mime.from_file(example_path + img).replace("image/", ""))
            print(img)
    '''
    
    # Perform search
    images = []

    search_words = [
        " icon",
        " logo",
        " emblem",
        " symbol",
        " badge",
        " brand",
        " logotype"
    ]

    c = 0
    for line in user_feature_names:
        c += 1
        #print("{}".format(line.strip()))
        images.append("{}".format(line.strip()))

    for z in range(len(search_words)):
        for y in range(len(images)):
            #print(images[y] + search_words[z])
            pass

if __name__ == "__main__":
    main()
