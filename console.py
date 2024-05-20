#!/usr/bin/python3
"""Implementing the HBHBC console/ Entry point for the console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on an empty line"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the progam"""
        return True

    def do_EOF(self, arg):
        """Exit the console on EOF (Ctrl+D"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
