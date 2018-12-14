#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
import itertools

passwd = 'e10adc3949ba59abbe56e057f20f883e'

seed_dict = range(10)
print seed_dict

for i in itertools.product(seed_dict, repeat=6):    # 对 0-9 进行排列组合，取6位
    result = ''.join(map(str, i)) # 转化为字符串
    print result
    value = hashlib.new("md5", result).hexdigest() #加密
    #print value

    '''
    if result == '123456':
        print result

    if value == passwd:
        print '==', passwd
        print 'value:', value
    '''