# Generate spark-level data
#

import random, math, sys

def gen_single_data_piece(feature_no):
    ans = ""
    feature_set = []
    # decide the class
    sample_class = random.randint(0, 1)
    ans = ans + str(sample_class) + " "
    # decide the feature set
    for i in range(1, feature_no+1):
        se = random.uniform(0,1)
        if se < 0.08:
            feature_set.append(i)
    for ft in feature_set:
        sp = random.randint(1,100)
        ans = ans + str(ft) + ":" + str(sp) + " "
    ans = ans + "\n"
    return ans


def gen_data_and_write(sample_no, feature_no, output_txt_path):
    f = open(output_txt_path, 'w')
    for _ in range(sample_no):
        str_to_write = gen_single_data_piece(feature_no)
        f.write(str_to_write)
    f.close()
    return


if __name__ == '__main__':
    sample_no = 100
    feature_no = 500
    output_txt_path = "synthetic_lr_data.txt"
    gen_data_and_write(sample_no, feature_no, output_txt_path)
