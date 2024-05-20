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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split[0]
        if class_name not in self.class_map:
            print("** class doesn't exist **")
            return


    def do_show(self, arg):
        """Prints the string rep of an instance based on class name"""
        if not arg:
            print("** class name missing **")
            return

    def do_destroy(self, arg):
        """Deletes the instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

    def do_all(self, arg):
        """Prints all string rep of all instances based on the class name"""


    def do_update(self, arg):
        """Updates an instance base on the class name and id"""
        print("** class name missing **")
        return



if __name__ == '__main__':
    HBNBCommand().cmdloop()
