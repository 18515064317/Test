#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
import sys
if os.getuid() == 0:
   print('请以root用户运fsfdsfds行')
   pass
else:
    print('请以root用户运行')
    sys.exit(1)
version = int(raw_input('请输入要下载的版本号2/3:'))
if version == 2:
    url = 'ftp://newsfan:cms3013@172.16.149.210/TS/iperf-3.5.tar.gz'
elif version == 3:
    url = 'ftp://newsfan:cms3013@172.16.149.210/TS/iperf-3.5.tar.gz'
else:
    print('输入错误')
    sys.exit(1)
cmd = 'wget ' + url
res = os.system(cmd)
if res != 0 :
    print(' 请检查URL连接以及FTP目录权限！！！')
    sys.exit(1)

if version == '2':
    package_name = 'iperf-2.0.2'
else:
    package_name = 'iperf-3.5'
cmd = 'tar -zxvf ' + package_name + '.tar.gz'
res = os.system(cmd)
if res != 0:
    print('解压失败！！！')
    sys.exit(1)

cmd = 'cd ' + package_name + ' && chmod 755 configure && ./configure --prefix=/usr/local/iperf && make && make install'
res = os.system(cmd)
if res != 0:
    print('编译失败！请检查是否缺少依赖库！！')
    sys.exit(1)
cmd = 'cd /usr/local/iperf && iperf -s'
res = os.system(cmd)
if res != 0:
    print('安装失败！运行失败！')
    sys.exit(1)
