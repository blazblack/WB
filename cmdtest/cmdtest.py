# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:16:20 2017
@author: ict
"""

import subprocess
import sys 
from os import path
import time
import concurrent.futures

def automatic(progname):
    
    #問題番号が存在するかの確認
  #  if path.exists(progname + "_data.txt") == False:
  #      return 1
        
    prog_execution = "gcc " + progname + ".c " + "-Wall"
    #DBからプログラム名を引数に探し出す
    check = subprocess.run((prog_execution), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    print("実行名　　　" + check.args)
    print("実行判定　 " + str(check.returncode))# ここでの返り値は実行ファイルを問題なく実行できたかが返ってくる　成功は0 失敗は１である
    if check.returncode != 0:
        print("コンパイルエラー\n" + check.stderr.decode('utf-8'))# ここに実行時問題が発生した場合、エラー文が書き込まれる
        return 2
    
    if check.stderr != b'':
        print("実行時警告\n" + check.stderr.decode('utf-8'))
        return 3
        
    #print("実行字入力" + check.stdout)
    
    return execution(progname)


def execution(progname):
    
    #executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    
    with open(progname + "_data.txt",'r') as prog_data:
        num_data = int(prog_data.read())
            
    for i in range(1, num_data + 1):
        with open (progname + "_case_" + str(i) +".txt",'r',encoding = 'cp932') as prog_case: #DB化不可能である
            exe = subprocess.Popen('./a.out', shell = True, stdin = prog_case, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

            try:
                stdout_data, stderr_data = exe.communicate(timeout=1)
             
                #subprocess.call("taskkill /im a.exe /f")
                subprocess.call("pkill -KILL -f a.exe")
                outs, errs = exe.communicate()
                return 4
            
        stdout_data, stderr_data = exe.communicate()
        str_case = stdout_data.decode(sys.stdin.encoding)
        
        str_case = str_case.replace('\n','')
        str_case = str_case.replace('\r','')
            
        with open (progname + "_answer_"+ str(i) +".txt",'r') as prog_answer: #DB化可能である
            str_answer = prog_answer.read()
            str_answer = str_answer.replace('\n','')
            str_answer = str_answer.replace('\r','')
                
         
                subprocess.call("killall a.out", shell=True)
                outs, errs = exe.communicate()
                return 4
            
        #stdout_data, stderr_data = exe.communicate()
        str_case = stdout_data.decode('cp932')

        str_case = str_case.replace('\n','')
        str_case = str_case.replace('\r','')
    
        with open (progname + "_answer_"+ str(i) +".txt",'r',encoding = 'cp932') as prog_answer: #DB化可能である
            str_answer = prog_answer.read()
            str_answer = str_answer.replace('\n','')
            str_answer = str_answer.replace('\r','')

        #現状は疑似的にファイル操作を行ってデータを取り出しているが、DB上ｆではデータを探し出して当てはめることでできる
        #prog_caseにデータを入れる際はデータ形式に気をつける
        #多分だけど、ダイレクトじゃないとテストケースを実行ファイルに読み込めないっぽいので、テストケースはテキストファイルで保存する形になると思います。
            
        print("実行名　　　" + exe.args)       #実行ソースタイトル
        print("テキスト回答" +str_answer)     #テキストの回答
        print("実行回答　 " + str_case)       #実行exeのprintf 
        print("mian返り値 " + str(exe.returncode)) #ソースの名関数返り値
        print("実行時警告" + stderr_data.decode('utf-8'))     #標準入出力先へのパイプ指定
                
        if str_answer == str_case:
            print("正解")
        else:
            print("不正解")
            
    return 0
    
    
    
def time_limit():
    time.sleep(0.1)
    
    
    
    
def main():
    while (True):#デーモン化した場合の動きは想定していない
        progname = input(">>")
        if progname == "end":
            break
        result_code = automatic(progname)
        if result_code == 1:
            print("その問題は存在しません")
        elif result_code == 2:
            print("コンパイルエラー")
        elif result_code == 3:
            print("ランタイムエラー")
        elif result_code == 4:
            print("時間足りません")
    
            
if __name__ == '__main__':
    main()
