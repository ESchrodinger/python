# 使用方法：在cmd中输入 python的index 需要运行的脚本index 该脚本需要的参数
import os
import subprocess
import sys
import time

adb = 'adb -s '
shell = ' shell'
pslist = []
tasklist = []
appresult = "App,Pid,Task\n"

class Info_ps:
    def __init__(self):
        self.USER = ''
        self.PID = 0
        self.PPID = 0
        self.VSZ = 0
        self.RSS = 0
        self.WCHAN = ''
        self.ADDR = 0
        self.S = ''
        self.NAME = ''

class Info_task:
    def __init__(self):
        self.task = ''
        self.activities = []



def getps(device):

    # cmd是指令
    cmd = adb + device + shell + " ps -A"
    allps = subprocess.check_output(cmd)

    allps = allps.decode().split('\r\n')
    # print(allps)

    listsize = len(allps)

    print ("allps count " + str(listsize))

    for ps in allps:

        ps = ps.split()
        if len(ps) == 0 or ps[0] == 'USER':
            continue

        print(ps[1])
        # 接下来就是创建一个存ps信息的类实例
        psitem = Info_ps()

        psitem.USER = ps[0]
        psitem.PID = int(ps[1])
        psitem.PPID = int(ps[2])
        psitem.VSZ = int(ps[3])
        psitem.RSS = int(ps[4])
        psitem.WCHAN = ps[5]
        psitem.ADDR = int(ps[6])
        psitem.S = ps[7]
        psitem.NAME = ps[8]

        # 判断是否是英文字母，加到pslist里面
        if psitem.NAME.isalpha():
            pslist.append(psitem)

def getactivities(device):

    cmd = adb + device + shell + " dumpsys activity activities"
    alltasks = subprocess.check_output(cmd)
    alltasks = alltasks.decode().split('\r\n')
    # print(alltasks)

    # 防止空定义，java习惯了
    task = Info_task()
    for line in alltasks:

        if line.find('* Task{') != -1:
            task = Info_task()
            task.task = line
            tasklist.append(task)
            print(line)

        if line.find(('* Hist ')) != -1:
            task.activities.append(line)
            print(line)

        if line.find('Resumed activities in task display areas') != -1 :
            # time.sleep(1000)
            break

if __name__ == '__main__':
    devices = subprocess.check_output('adb devices')
    # \r是将光标移到行的开始，\n是换行
    devices = devices.decode('utf-8').split("\r\n")
    print(devices)
    devicesize = len(devices) - 1

    if devicesize == 0:
        exit(0)

    # sys.argv[1]其实就是我在命令行输入的参数，sys.argv[0]是脚本文件的地址
    # sys.argv[1:]是该脚本的全部参数以list存起来
    # appfile = sys.argv[1]

    appfile = r'C:\\Users\\zjiang.li\\Desktop\\applist.txt'

    applist = open(appfile, 'r', encoding='UTF-8', errors='ignore').read()

    applist = applist.split('\n')
    print("app count " + str(len(applist)))

    # print(applist)

    # 接下来就是对每个device都执行预定好的指令
    for i in range(1, devicesize):

        if (len(devices[i]) < 2):
            continue
        end = devices[i].find('\t')
        # print(end) # end是\t的结束
        device = (devices[i])[0:end]
        # print(device)

        # 得到了process和task的信息，接下来汇总
        getps(device)
        getactivities(device)

        for app in applist:

            pid = -1
            ptask = None

            for ps in pslist:
                # 判断名字
                if ps.NAME == app:
                    pid = ps.PID
                    break

            for task in tasklist:
                # 判断task那行有没有出现app包名
                if task.task.find(app) != -1:
                    ptask = task
                    break

            if ptask == None:
                print(app + ' pid: ' + str(pid) + '\n' + 'None' + '\n')
                appresult += (app + ',' + str(pid) + ',' + 'None' + '\n')
            else:
                print(app + ' pid: ' + str(pid) + '\n' + ptask.task)
                appresult += (app + ',' + str(pid) + ',' + ptask.task)

                for activity in ptask.activities:
                    print('\n' + activity)
                    appresult += (',' + activity)

                print('\n')
                appresult += '\n'

        timeStr = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
        if  os.path.exists(device) == False:
            # 创建一个device为名的文件夹
            os.makedirs(device)

        # with和open搭配使用可以在改动完文件后自动关闭
        with open(device + os.sep + timeStr + '.csv', 'a') as file:
            file.write(appresult + '\n')

        # 参数：读取的文件名，读取模式
        # 读取的不同模式：
        # 'w':打开一个文件只用于写入，如果该文件已存在则打开文件，并且从头开始编辑，即原有内容会被删除。如果该文件不存在，则创建新文件。
        # 'r':以只读的方式打开文件。文件的指针将会放在文件的开头。
        # 'b':二进制模式
        # '+':打开一个文件进行更新，可读可写
        # 'a':打开一个文件用于追加，如果该文件已经存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件进行写入。
        # 注意：还有两两合并的一些模式，是两种单一模式的作用相加。
        # 对象方法：
        # read(size):返回整个文件, 如果指定size则返回size个字符。
        # readline():返回一行
        # readlines(): 返回全部行的一个列表
        # write(): 写入字符
        # close(): 关闭文件
