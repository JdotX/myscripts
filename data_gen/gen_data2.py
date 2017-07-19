# Generate spark-level data
# For Chukonu evaluation

import random, math, sys, time

def gen_single_data_piece(feature_no, step):
    ans = ""
    feature_set = []
    a = []
    # decide the class
    for ft in range(1,feature_no):
        sp = random.random()
        ans = ans + str(ft) + ":" + str(sp) + " "
    ans = ans + "\n"
    return ans


def gen_data_and_write(sample_no, feature_no, output_txt_path, step_size = 2000):
    f = open(output_txt_path, 'w')
    for i in range(sample_no):
        if i % 1 == 0:
            print (i)
        str_to_write = gen_single_data_piece(feature_no, step_size)
        f.write(str_to_write)
    f.close()
    return


if __name__ == '__main__':
    t1 = time.time()
    sample_no = 50
    feature_no = 200000
    output_txt_path = "synthetic_lr_data2.txt"
    gen_data_and_write(sample_no, feature_no, output_txt_path)
    print time.time() - t1
