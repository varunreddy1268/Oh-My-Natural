import os
import numpy as np 
def dict_maker():
    res_list1=[]
    with open("/Users/chandrapavan1104/Harvestify/app/cure.txt") as cure:
        lines=cure.readlines()
        res_list1.append(lines)
    while "\n" in res_list1:
        res_list1.drop("\n")
    main_dict={}
    #print(res_list1)
    for i in range(len(res_list1[0])-1):
        if len(res_list1[0][i])>1:
            s=res_list1[0][i].split("-")
            #print(s[0][1:])
            main_dict[s[0][1:]]=s[1].split(".")[:-1]
            #print(s[1].split("."))
    return main_dict
def organic_adviser(label):
    dict1=dict_maker()
    return dict1[label]
        