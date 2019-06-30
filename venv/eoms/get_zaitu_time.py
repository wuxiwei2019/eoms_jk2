# coding=utf-8
import time
import datetime


class GetZaiTuTime(object):
    def __init__(self, data_list):
        self.data_list = data_list

    def get_data(self, set_time):
        cur_time = datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        print("----start-------")
        new_list = []
        for v_str in self.data_list:
            time_str = v_str.split("\t")[1]
            gd_time = datetime.datetime.strptime(time_str,  '%Y-%m-%d %H:%M:%S')
            diff_time = cur_time - gd_time
            if diff_time.days * 24 * 60 * 60 >= int(set_time) * 60:
                print(gd_time)
                new_list.append(v_str)
        return new_list

