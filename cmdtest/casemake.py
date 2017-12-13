# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:16:20 2017
@author: ict
"""

import subprocess
import sys
import os.path
import time
import concurrent.futures

def automatic(progname):
    
    #問題番号が存在するかの確認
    if os.path.exists(progname + "_data.txt") == False:
        return 1
        
    prog_execution = "gcc " + progname + ".c " + "-Wall"
    #DBからプログラム名を引数に探し出す
    check = subprocess.run((prog_execution), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    print("実行名　　　" + check.args)
    print("実行判定　 " + str(check.returncode))# ここでの返り値は実行ファイルを問題なく実行できたかが返ってくる　成功は0 失敗は１である
    if (check.returncode != 0):
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
                outs, errs = exe.communicate(timeout=1)
                
            except subprocess.TimeoutExpired:
                #exeid = exe.pid
                subprocess.call("killall a.out" ,shell=True)
                outs, errs = exe.communicate()
                return 4
            
        str_case = outs.decode('cp932')
            
        print("実行名　　　" + exe.args)       #実行ソースタイトル
        print("実行回答　 " + str_case)       #実行exeのprintf 
        print("mian返り値 " + str(exe.returncode)) #ソースの名関数返り値
        with open (progname + "_answer_"+ str(i) +".txt",'w') as case_answer:
            case_answer.write(str_case)
        
        print("実行時警告" + errs.decode('utf-8'))     #標準入出力先へのパイプ指定
            
            
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
