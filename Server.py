# This is the template code for the CNA337 Final Project
# Michael Horton
# CNA 337 Fall 2020
#Worked with Dylan McCormack,  Eric Yevenko
#Received help from Luma and Hasan
# This link helped me with the "Bad Authentication type; allowed types['pubilickey'] Error:
# https://stackoverflow.com/questions/2224066/how-to-convert-ssh-keypairs-generated-using-puttygen-windows-into-key-pairs-us
## This website showing how to use paramiko:
# https://mainlydata.kubadev.com/python/using-paramiko-to-control-an-ec2-instance/

import os
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        server = os.system("ping -n 4 " + self.server_ip)
        return self.server_ip

# NEXT steps are to:  
# 1.Automate SSH:
# 2. Connect to my Ec2 Instance using my SSH key
# 3. Run Update and Upgrade commands in the package manager
# 4. Disconnect from server

import paramiko
# create client ssh object so we can use it to connect to the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Missing key will be added here #

ssh.connect('3.21.97.118', port=22, username='ubuntu', password='', key_filename='Michael-key.Exported')

stdin, stdout, stderr = ssh.exec_command('''sudo apt-get update
                                         sudo apt-get upgrade -y
                                         ''')  # site to force the upgrade: https://itsfoss.com/update-ubuntu/
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()
