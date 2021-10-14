#!/usr/bin/env python

o = open("FEATURES.md", "r")
try:
    first_line = o.readline().split("features")
    num_user_features = int(filter(str.isdigit, first_line[0]))
    num_root_features = int(filter(str.isdigit, first_line[1]))
    lines = o.readlines()[4:]
    #print(lines)
    feature_list = []
    for i in range(num_user_features):
        feature_list.append(lines[i].split("|"))
    with open('user_programs', 'w') as w:
        k = 0
        while k <= len(feature_list) - 2:
            w.write(feature_list[k][1] + '\n')
            if k == num_user_features:
                break
            k += 1
    with open('root_programs', 'w') as w:
        k = 0
        while k <= len(feature_list) - 2:
            w.write(feature_list[k][1] + '\n')
            if k == num_user_features:
                break
            k += 1
finally:
    o.close()
