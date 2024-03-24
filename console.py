#!/usr/bin/python3
"""Implementing the HBHBC console/ Entry point for the console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quites the console"""
        return True

    def do_end_of_file(self,arg):
        """Indicates the end of the file"""
        return True

    def do_empty_line(self):
        """Doesnt do anything"""
        pass

if __name__ == '__main__':
HBNBCommand().cmdloop()
