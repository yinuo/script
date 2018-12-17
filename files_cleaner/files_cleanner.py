#!/usr/bin/env python3
#-*-coding: utf-8 -*-

import os
import re
import shutil
import send2trash

MOVED_DIR = '/home/lwang/zl/script/files_cleaner/move'
TARGET_DIR = '/home/lwang/zl/script/files_cleaner/daemon'
DELETED_FILES_NAME = '/home/lwang/zl/script/deleteFiles.txt'
DELETED_PATTERN = re.compile('daemon-\w*\.out')
COUNT = 0

def do_operation(target_file_path):
    #write file
    #record_deleted_files_name(target_file_path)
    #move_file
    #move_file_to_new_dir(target_file_path)
    #delete file
    saved_delete_file(target_file_path)
    #rename file
    #rename_file(target_file_path)

def rename_file(target_file_path):
    global COUNT
    if os.path.isfile(target_file_path):
        extension = os.path.splitext(target_file_path)[1]

        new_name = (os.path.dirname(target_file_path) + '/rename_ %s' + extension) % (COUNT)
        COUNT += 1
        try:
            shutil.move(target_file_path, new_name)
        except IOError:
            print('[[文件被占用] = ]' + target_file_path)

def saved_delete_file(target_file):
    if os.path.isfile(target_file):
        try:
            send2trash.send2trash(target_file) #使用send2trash安全删除（丢到回收站）
        except IOError:
            print('[文件被占用] = ' + target_file)

def move_file_to_new_dir(target_file):
    if not os.path.exists(MOVED_DIR):
        os.mkdir(MOVED_DIR)
    try:
        shutil.move(target_file, MOVED_DIR)
    except IOError:
        print('[文件被占用] = ' + target_file)

def record_deleted_files_name(target_file):
    print('Deleted File] = ' + target_file)
    write_file = open(DELETED_FILES_NAME, 'a')
    write_file.write(target_file)
    write_file.write('\n')
    write_file.close()


def delete_file(target_path):
    #print(target_path)
    #print(os.path.basename(target_path))
    result = DELETED_PATTERN.match(os.path.basename(target_path))
    print (result)
    if result is not None:
        do_operation(target_path)

def find_delete_file(root_dir):
    for root, dirs, files in os.walk(root_dir): #os.walk()方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下
        #print(root, dirs, files)
        for f in files:
            #print(f)
            #print(os.path.join(root, f))
            delete_file(os.path.join(root, f)) #os.path.join()函数用于路径拼接文件路径

if __name__ == '__main__':
    find_delete_file(TARGET_DIR)