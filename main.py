# This is the template code for the CNA337 Final Project
# Michael Horton
# CNA 337 Fall 2020
#Worked with Dylan McCormack,  Eric Yevenko
#Received help from Luma
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
