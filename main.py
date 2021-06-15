# -*- coding: utf-8 -*-
# @Date    : 2021-06-12 17:41:21
# @Author  : Nora Yao(norayao0817@gmail.com)
# @Link    :
# @Version : Python3.7

import os
import sys
import json
import requests
import random
import re
import tkinter as tk
from tkinter import filedialog, Label

# google_trans_new 依赖于 json, requests, random, re
from google_trans_new import google_translator

from openpyxl import Workbook


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.getFile_btn = tk.Button(self)
        self.filePath_entry = tk.Entry(self, width=30)
        self.master = master
        self.pack()
        self.translator = google_translator()
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.create_widgets()

    def trim(self, text):
        result = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", ",", text)
        return result

    def refactor(self, text):
        # 此处的'，'为中文字符，Google translate自动转换了符号
        result = text.replace('，', '_')
        return result

    def create_widgets(self):
        # 显示文件路径
        self.filePath_entry.grid(row=1, column=1, padx=0, pady=10)
        self.filePath_entry.delete(0, "end")
        self.filePath_entry.insert(0, "请选择文件")

        # 获取文件
        self.getFile_btn['width'] = 15
        self.getFile_btn['height'] = 1
        self.getFile_btn["text"] = "打开"
        self.getFile_btn.grid(row=1, column=2, padx=5, pady=10)
        self.getFile_btn["command"] = self.select_dir

        # 显示结果


    # 打开文件并显示路径
    def select_dir(self):
        default_dir = r"文件路径"
        self.pathValue = tk.filedialog.askdirectory(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        self.filePath_entry.delete(0, "end")
        self.filePath_entry.insert(0, self.pathValue)
        filenames = self.achieve_filenames(self.pathValue)

        self.worksheet['A1'] = '原文件名'
        self.worksheet['B1'] = '翻译'
        self.worksheet['C1'] = '完整文件名'
        self.worksheet['D1'] = '路径'
        n = 2
        for file in filenames:
            if len(file) > 1:
                name_src = file[0]
                name_dest = self.refactor(self.filename_translation(self.trim(name_src)))
                fullname_src = name_src + "." + file[1]
                fullname_dest = name_src + "-" + name_dest + "." + file[1]
                fullpath_src = os.path.join(self.pathValue, fullname_src)
                fullpath_dest = os.path.join(self.pathValue, fullname_dest)
                os.rename(fullpath_src, fullpath_dest)
                self.worksheet['A'+str(n)] = name_src
                self.worksheet['B'+str(n)] = name_dest
                self.worksheet['C'+str(n)] = fullname_dest
                self.worksheet['D'+str(n)].value = fullpath_dest
                self.worksheet['D'+str(n)].hyperlink = fullpath_dest
                n += 1
        catalog = self.pathValue + '.xlsx'
        self.workbook.save(catalog)

        label_text = self.pathValue+" done"
        self.result_lable = tk.Label(self, text=label_text)
        self.result_lable.grid(row=2, column=1, padx=5, pady=10)


    def achieve_filenames(self, path):
        filenames = []
        for file in os.listdir(path):
            name = file.split('.')
            filenames.append(name)
        return filenames

    def filename_translation(self, text):
        translate_text = self.translator.translate(self.trim(text), lang_tgt='zh')
        return self.refactor(translate_text)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("文件名翻译")
    root.geometry("500x300+600+300")

    app = Application(master=root)
    app.mainloop()



