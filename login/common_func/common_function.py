#判断是否为数字

def is_number(number):
    try:
        number1 = int(number)
    except Exception as e:
        return False
    
    return number

def getTime():
    from datetime import datetime
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time

#循环判断这个这个端口有没有被暂用,还有就是是否空闲的,直接可以利用的.!
def is_used_port(port_numer):
    estimate_info = get_running_node()
    port_run = [int(x['port']) for x in estimate_info]

    for x in range(int(port_numer),int(port_numer)+9):
        if x in port_run:
            if is_set_est_info():
                #已经被占用,跳到下一个条件继续循环
                continue
            else:
                #设置
                return x
        else:
            #先启动node.js程序(评价程序)
            start_estimate(x)
            return x


#这个是用于判断这个已经启动的评价程序对应的端口是否已经设置评价信息
def is_set_est_info():
    import requests
    import json
    x1 = requests.post("http://127.0.0.1:8081/grade/init").json()
    #if "teacherName" not in 
    return x1.json()


    # 'Content-Type: application/json',
    # 'Content-Length: ' 

##停止评价
def stop_estimate(x):

    import requests
    import json

    x1 = requests.post("http://127.0.0.1:8081/grade/commit")
    return  x1.json()

#启动nodejs评价程序
def start_estimate(port):
    pass

#检测目前有哪些node在运行
def get_running_node():
    import os
    import re

    x1 = os.popen("netstat -ntlp|grep -E '0.0.0.0:80[6-9][0-9]'").read()
    x2 = x1.split("\n")
    validInfo = [ x  for x in x2 if x ]
    print(validInfo)
    program = []
    if validInfo:
        for x in validInfo:
            info = {}
            port = re.search("0.0.0.0:80\d\d",x)[0].split(":")[1]
            info['port'] = port
            info['pid'] = re.search("\d+/",x)[0].split("/")[0]
            program.append(info)
    return program

