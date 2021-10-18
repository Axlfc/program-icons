#!/usr/bin/env python
import os
import requests

def download_image(image_url, image_path):
    with open(image_path, 'wb') as handle:
        response = requests.get(image_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

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

    #print(user_feature_names)
    #print(root_feature_names)

    # Trim software folder names
    for i in range(len(root_feature_names)):
        for j in root_feature_names[i]:
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
                os.makedirs(dirName)
                print("Directory ", dirName,  " Created ") 
            except:
                print("Directory ", dirName,  " already exists")

    # Perform search
    images = []

    search_words = [
        " icon",
        ".svg",
        " logo",
        " emblem",
        " symbol",
        " badge",
        " brand",
        " logotype",
        ".svg wikipedia"


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

    pic_url = 'http://google.com/favicon.ico'
    pic_name = "google_icon.ico"
    pic_path = "images/user/Google/" + pic_name
    download_image(pic_url, pic_path)


if __name__ == "__main__":
    main()
