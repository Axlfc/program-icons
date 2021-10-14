#!/usr/bin/env python

o = open("FEATURES.md", "r")
try:
    first_line = o.readline().split("features")
    num_user_features = int(filter(str.isdigit, first_line[0]))
    num_root_features = int(filter(str.isdigit, first_line[1]))
    num_total_features = int(filter(str.isdigit, first_line[2]))
    lines = o.readlines()[4:]
    #print(lines)
    feature_list = []
    root_feature_list = []
    for i in range(num_user_features):
        feature_list.append(lines[i].split("|"))
    with open('user_programs', 'w') as w:
        k = 0
        while k <= len(feature_list) - 2:
            w.write(feature_list[k][1] + '\n')
            if k == num_user_features:
                break
            k += 1
        w.close()
    '''
    with open('root_programs', 'w') as x:
        k = num_user_features + 1
        #print("skip lines here to trim data...")
        h = 0
        for j in range(k, num_total_features):
            print(h)
            thing = lines[h].split("|")
            print(thing[1])
            root_feature_list.append(thing)
            #print(thing[1])
            x.write(thing[h] + '\n')
            h += 1
        x.close()'''
finally:
    o.close()


images = []

search_words = [
    " icon",
    " symbol"
]

#print(search_words)
o = open("user_programs", "r")
lines = o.readlines()
c = 0
for line in lines:
    c += 1
    #print("{}".format(line.strip()))
    images.append("{}".format(line.strip()))

for z in range(len(search_words)):
    for y in range(len(images)):
        print(images[y] + search_words[z])
