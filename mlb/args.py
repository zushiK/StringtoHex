# coding: utf-8

import sys

# 第1引数を返す
# 引数の数   : 返り値
# 引数無し   : None
# 引数1以上　: 第1引数
def getArgsFirst():
    args = sys.argv

    if len(args) <= 1:
        return None
    else:
        return args[1]

def main():
    print(getArgsFirst())

if __name__ == '__main__':
    main()
