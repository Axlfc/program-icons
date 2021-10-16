#!/usr/bin/env python

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

images = []

search_words = [
    " icon",
    " symbol"
]

c = 0
for line in user_feature_names:
    c += 1
    #print("{}".format(line.strip()))
    images.append("{}".format(line.strip()))

for z in range(len(search_words)):
    for y in range(len(images)):
        print(images[y] + ".svg" + search_words[z])
