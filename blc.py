import paramiko
import time

#gssh = paramiko.channel.Channel();
pros = ["DBReaderServer", "DBWServer", "DBReader", "DBWriter", "PttTrans","TransServ"]

class Test:
    def __init__(self, id):
        self.id = id;
        print("Test init")
    def __del__(self):
        print("Test del")
    def print(self):
        print(self.id)
        
def newTest():
    t = Test(2132);
    return t
    
def inputTest(t):
    print("input test")


def new_ssh(host,username,password,port,root_pwd):
    s=paramiko.SSHClient()  
    #s.load_system_host_keys()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = host,port=int(port),username=username, password=password)
   
    gssh = s.invoke_shell()
    time.sleep(0.1)
    print("root login......")
    gssh.send('su - \n')
    buff = ""
    while not buff.endswith('Password: '):
        resp = gssh.recv(9999)
        buff += resp.decode()  
    gssh.send(root_pwd)
    gssh.send("\n\n")
    buff = ''
    while not buff.endswith('# '):
        resp = gssh.recv(9999)
        buff +=resp.decode()
        
    print(buff)

    #exec(ssh, "mkdir /usr/old.bak")
    #exec(ssh, "cp /usr/admin")
    

    return [gssh]

def exec(ssh, cmd):
    #ssh = s.invoke_shell()
    time.sleep(2);
    print(">>>>>" + cmd)
    ssh.send(cmd);
    ssh.send('\n');
    buff = ''
 
    while not buff.endswith('# '):
        resp = ssh.recv(9999)
        buff +=resp.decode()
        if buff.endswith('? '):
            print("?????????")
            ssh.send("yes\n")
        
    print(buff)
    

def ssh_exec(ssh, cmd):
    ssh.exec_command(cmd)
    
#client = new_ssh("139.。。。。。。。", "。。。", "..", 2222, "...")
#print(type(client))
#while true:
  # cmd = input(">>>>")
  # exec(client, cmd)
#t = paramiko.Transport(("....13", 2222))
#t.connect(username = "...", password = "..")
#sftp = paramiko.SFTPClient.from_transport(t)
#sftp.put("F:/server/国外/",'/home//')

#t.close()
#

pttservers = [".."]
import os
import os.path
import os.path
rootdir ="F:\\PTT_NEW" #指明被遍历的文件夹
outdir = "/home/"
target = "/usr"#


for serv in pttservers:
    print("----------------" + serv + "----------------")
    s=paramiko.SSHClient()  
    #s.load_system_host_keys()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = serv,port=int(22),username="", password="")
   
    gssh = s.invoke_shell()
    time.sleep(0.1)
    print("root login......")
    gssh.send('su - \n')
    buff = ""
    while not buff.endswith('Password: '):
        resp = gssh.recv(9999)
        buff += resp.decode()
    print("input pass pwd")
    gssh.send("pwd...\n")
    buff = ''
    while not buff.endswith('# '):
        resp = gssh.recv(9999)
        buff +=resp.decode()
    print(buff)#


    #exec(gssh, 'kill -9 $(pgrep )')

    exec(gssh, "mkdir " + outdir +'/'+ rootdir.split('\\')[-1])

    exec(gssh, 'chmod a+w '+ outdir +'/'+ rootdir.split('\\')[-1])
    t = paramiko.Transport((serv, 22))
    t.connect(username = "...", password = "...")
    sftp = paramiko.SFTPClient.from_transport(t)
    exec(gssh, 'cd /usr/blc')
    #exec(gssh, 'rm -f dgetMonitor*')
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:                        #输出文件信息
            file = os.path.join(parent,filename) #输出文件路径信息
            print(file)
            file2 = file.replace("\\", "/")
            newPath = file2.replace(rootdir.replace("\\","/"), outdir +'/' + rootdir.split('\\')[-1])
            
            
            print(file+'---->'+newPath)
            sftp.put(file,newPath)
            #exec(gssh, "cp " + newPath +" "+target +"/"+ filename)
            if (file.split(".")[-1] == "monitor" or file.split(".")[-1] == "sh" or file.split(".")[-1] == "server" or filename == "blc"):
                ssh_exec(s, "chmod a+x " +newPath)
        for dir in dirnames:                        #输出文件信息
            file = os.path.join(parent,dir) #输出文件路径信息+ rootdir.split('\\')[-1]
            file = file.replace("\\", "/")
            newPath = file.replace(rootdir.replace("\\","/"), outdir +'/' + rootdir.split('\\')[-1])
            print(newPath)
            ssh_exec(s, 'mkdir '+newPath)

    ssh_exec(s, 'cp -r '+outdir +rootdir.split('\\')[-1]+'/. '+ target+"/")
    t.close()#

    s.close()#
