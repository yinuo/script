#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pexpect
import sys

'''
远程文件自动打包并下载
'''

ip = '10.30.37.113'
user = 'samba'
passwd = 'samba'
target_file = '/home/lwang/BM1682/server/zl/boot.log'

child = pexpect.spawn('ssh', [user+'@'+ip])
fout = open('mylog', 'wb')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('$')
    child.sendline('cd /home/lwang/BM1682/server/zl/')
    child.expect('$')
    child.sendline('tar zcf test.tar.gz '+ target_file)
    child.expect('$')
    print(child.before)
    child.sendline('exit')
    fout.close()
#except EOF:
#    print('expect EOF!')
except Exception as e:
    print('except 1TIMEOUT!')

'''
#child = pexpect.spawn('scp ' + user + '@' + '/home/lwang/BM1682/server/zl/test.tar.gz' + '.')
child = pexpect.spawn('scp samba@10.30.37.113:/home/lwang/BM1682/server/zl/test.tar.gz' + '.')
fout = open('scplog', 'ab')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
#except EOF:
#    print('expect EOF!')
except Exception as e:
    print('expect 2TIMEOUT!')
'''