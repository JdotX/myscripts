'''
' Reads output of collectl
'''

'''
This file reads a specific kind of collectl output
'''


import numpy as np

# already done: get an entry on a line
# given the data, attribute, and attribute list
# checked: read the complete file
def get_attr_pos(data, attr, attr_list):
    if attr in attr_list:
        return attr_list.index(attr)
    else:
        return -1

# This returns a single line indicating the lines names
def gen_attr_list(f_path):
    f = open(f_path, "r")
    line = f.readlines()[3].split(" ")
    while "" in line:
        line.remove("")
    f.close()
    print line
    return line

# This returns a 2D array
# Containing the data lines returned by collectl only
def read_file(f_path, f_type):
    #if f_type == "net":
    f = open(f_path, "r")
    result_data = []
    for line in f.readlines():
        if len(line) < 5:
            continue
        if line[0] == '#' or line[0] == 'w':
            continue
        line = line.strip().split(" ")
        while "" in line:
            line.remove("")
        result_data.append(line)
    f.close()
    return result_data

# retrieves information of certain item, i.e., eth3
# save it in an array with name
def retrieve_item(item_name, attr_pos):
    ans = []
    for line in net_data:
        if item_name in line:
            ans.append(line[attr_pos])
    return ans

if __name__ == "__main__":
    f_path = "Net_1"
    f_type = "net"
    net_data = read_file(f_path, f_type)
    attr_list = gen_attr_list(f_path)
    attr_pos = get_attr_pos(net_data, "KBIn", attr_list)
    ans = retrieve_item("eth2", attr_pos)
    print ans
    ans = retrieve_item("eth3", attr_pos)
    print ans
