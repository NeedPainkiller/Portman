import sys
import subprocess
from subprocess import Popen, PIPE

class Shell:

    def openPort(self, listenPort,listenAddress, connectPort, connectAddress):
        self.execute("netsh interface portproxy add v4tov4 listenport={0} listenaddress={1} connectport={2} connectaddress={3}".format(listenPort,listenAddress,connectPort,connectAddress))

    def closePort(self, listenPort,listenAddress):
        self.execute("netsh interface portproxy delete v4tov4 listenport={0} listenaddress={1}".format(listenPort,listenAddress))

    def showAll(self):
        self.execute("netsh interface portproxy show all")
        
    def execute(self, command):
        self.stdout_data = subprocess.Popen(command, shell=True, stdout=PIPE, stderr=PIPE).communicate()
       
    def getStdout(self):
        #stdout = str(self.stdout_data).split('\\n')
        #stdout = stdout[5:len(stdout)-2]
        return self.stdout_data

def run():
    shell = Shell()
    flag = sys.argv[1]

    if flag == "SHOW":
        shell.showAll()
        print(shell.getStdout())
    elif flag == "ADD":
        listenPort = sys.argv[2]
        listenAddress = sys.argv[3] 
        connectPort = sys.argv[4]
        connectAddress = sys.argv[5]
        shell.openPort(listenPort,listenAddress,connectPort,connectAddress)
        shell.showAll()
        print(shell.getStdout())
    elif flag == "DELETE":
        listenPort = sys.argv[2]
        listenAddress = sys.argv[3]
        shell.closePort(listenPort,listenAddress)
        shell.showAll()
        print(shell.getStdout())

run()