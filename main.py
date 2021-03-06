#!/usr/bin/python
# -*- coding: utf-8 -*-ㅋ
import pandas as pd
import json
import csv
import sys
import os

# import os
# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# fname, ext = os.path.split(__file__)
# print(fname,ext)

def isNaN(num):
        return num != num

# 시작 가능한지 확인
# .csv 파일일 경우에만 시작 할 수 있음장
# --- argv 입력목록 ---
# [0] = main.py
# [1] = 입력할 csv 파일의 경로
# [2] = 저장될 json파일의 경로
# -------------------
def checkStart(input):
    _path_csv = input[1]
    _path_json = input[2]
    fname, ext = os.path.splitext(_path_csv)
    # 첫번째 인자가 정상적인 파일일 경우
    if os.path.isfile(_path_csv):
        # 첫번쨰 인자가 .csv파일인 경우
        if ext == '.csv':
            # 두번째 인자가 경로인 경우
            if os.path.isdir(_path_json):
                # 두번째 인자의 맨 끝에 /가 없는경우
                if not _path_json.endswith('/'):
                    _path_json = _path_json+"/"
                return _path_csv, _path_json, True
            # 두번째 인자가 경로가 아닌경우
            else:
                print("Enter the correct json path\n")
        # 첫번쨰 인자가 .csv파일이 아닌경우
        else:
            print("Recheck the path of the csv file\n")
    # 첫번째 인자가 정상적인 파일이 아닌경우
    else:
        print("Enter the csv file path correctly\n")

input = sys.argv
path_csv, path_json, canStart = checkStart(input)

if canStart == True:

    # 파일을 불러옴
    csv_data = pd.read_csv(path_csv)

    # 열(세로)
    col = csv_data.shape[0]
    # 국가코드 갯수
    len_lang = 0
    # 추가할 Json 파일
    file_data = {}
    lang_data = []
    name_data = []

    # csv 파일의 맨 윗줄을 읽음
    rd = csv.reader(csv_data)
    for line in rd:
        lang_data.extend(line)
    # 앞에 3개 필요없는 데이터는 제거해줌
    for i in range(0,3):
        lang_data.pop(0)
    # 국가코드의 총 갯수
    len_lang = len(lang_data)

    print("")
    print("Number of words to convert : ",col)
    print("Language list :",lang_data)
    print("Converting Now...\n")
    
    # csv에 있는 언어의 수만큼 반복됨
    for j in range(0, len_lang):
        PAGE = KEY = APPNAME = LANG = ''
        # csv에 있는 단어의 갯수만큼 반복됨(세로줄)
        for i in  range(0, col):
            # 페이지칸이 공백이 아닐경우 json 맨 앞의 값은 해당 값이됨
            if isNaN( csv_data['PAGE'][i] ) == False :
                PAGE = csv_data['PAGE'][i]
                file_data[PAGE] = {}
            # Key 칸이 공백이 아닐경우 json 두번째 값은 해당값이 됨
            if isNaN( csv_data['KEY'][i] ) == False :
                KEY = csv_data['KEY'][i]
                file_data[PAGE][KEY] = {}
            
            # json['page']['app_name'][i] 와 같은 형식으로 저장됨
            # i 의 값은 총 단어의 갯수임
            APPNAME = csv_data['APP_NAME'][i]
            LANG = csv_data[lang_data[j]][i]
            file_data[PAGE][KEY][APPNAME] = LANG

        # 첫번째 언어가 기본이라서 만약 첫번째 언어면 파일명을 Strings로
        # 아니라면 string_en 같은 형식으로 파일이름을 저장
        language_name = "strings" if j == 0 else "string_"+lang_data[j]
        json_file_name = path_json+language_name + ".i18n.json"
        name_data.append(json_file_name)

        #with open(json_file_name, 'w') as outfile:
        with open(json_file_name, 'w') as outfile:
            #json.dump(file_data, outfile,ensure_ascii = False)
            json.dump(file_data, outfile,ensure_ascii = False,indent="\t")

    print("Completed convert!!\n")
    print("List of generated json files : ")
    for list in name_data:
        print(list)
