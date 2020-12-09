# This is the template code for the CNA337 Final Project
# Michael Horton
# CNA 337 Fall 2020
#Worked with Dylan McCormack,  Eric Yevenko
#Received help from Luma and Hasan
## This link helped me with the "Bad Authentication type; allowed types['pubilickey'] Error:
# https://stackoverflow.com/questions/2224066/how-to-convert-ssh-keypairs-generated-using-puttygen-windows-into-key-pairs-us
## This website showing how to use paramiko:
# https://mainlydata.kubadev.com/python/using-paramiko-to-control-an-ec2-instance/
##https://myarch.com/public-private-key-file-formats
#This webiste helped me with understanding the file formats

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Michael Horton")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    Michael_is_a_Wizard = Server('3.21.97.118')
    # TODO - Call Ping method and print the results
    print(Michael_is_a_Wizard.ping())
