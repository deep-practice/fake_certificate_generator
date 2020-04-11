#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''生成身份证字段'''
#1.身份证由17位数字本体码和1位校验码组成。排列顺序从左至右依次为：6位数字地址码，8位数字出生日期码，3位数字顺序码和1位数字校验码。
#2.6位地址码:省(2位)+市(4位)
from datetime import datetime, timedelta
import random,re

# 十五位身份证号表达式
ID_NUMBER_15_REGEX = r"^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$"

# 十八位身份证号表达式 identity_util
ID_NUMBER_18_REGEX = r"^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$"

def get_check_digit(id_number):
    """通过身份证号获取校验码"""
    check_sum = 0
    for i in range(0, 17):
        check_sum += ((1 << (17 - i)) % 11) * int(id_number[i])
    check_digit = (12 - (check_sum % 11)) % 11
    return check_digit if check_digit < 10 else 'X'


def verify_id(id_number):
    """校验身份证是否正确"""
    if re.match(ID_NUMBER_18_REGEX, id_number):
        check_digit = get_check_digit(id_number)
        return str(check_digit) == id_number[-1]
    else:
        return bool(re.match(ID_NUMBER_15_REGEX, id_number))


def generate_id(area_code,sex=0):
    """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""
    # 随机生成一个区域码(6位数)
    id_number = area_code
    # 限定出生日期范围(8位数)
    start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2050-12-30", "%Y-%m-%d")
    birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
    id_number += str(birth_days)
    # 顺序码(2位数)
    id_number += str(random.randint(10, 99))
    # 性别码(1位数)
    id_number += str(random.randrange(sex, 10, step=2))
    # 校验码(1位数)
    return id_number + str(get_check_digit(id_number))

class IDCard():

    def __init__(self,name,nation,addr,id_number,province_name,city_name):
        super(IDCard, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])
        self.addr = addr
        self.name = name
        self.nation = nation
        self.province_name = province_name
        self.city_name = city_name

    def get_id(self):
        return self.id

    def get_addr(self):
        return self.addr

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_month

    def get_birth_day(self):
        return  self.birth_day

    def get_sex(self):
        """通过身份证号获取性别， 女生：0，男生：1"""
        return ["男","女"][int(self.id[16:17]) % 2]

    def get_nation(self):
        return self.nation

    def get_name(self):
        return self.name

    def get_province_name(self):
        return self.province_name

    def get_city_name(self):
        return self.city_name








