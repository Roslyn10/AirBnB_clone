#!/usr/bin/python3
"""Implementing the HBHBC console/ Entry point for the console"""

import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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
        elif arg not in storage.classes:
            print("** class doesn't exist **")
            return
        new_instance = storage.classes[arg]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        """Prints the string rep of an instance based on class name"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    """def __init__(self, classes):"""
    """Allows the console to run classes"""
    """self.classes = classes"""

    def do_destroy(self, arg):
        """Deletes the instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found**")
            return
        del storage.all()[key]
        storage.save()


    def do_all(self, arg):
        """Prints all string rep of all instances based on the class name"""
        args = arg.split()
        objects = storage.all()
        if args and args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if not args:
            instances = [str(obj) for obj in storage.all().values()]
        else:
            instances = [str(obj) for key, obj in storage.all().items() if key.startswith(args[0])]
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            keys = arg[0] + '.' + arg[1]
            if keys in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[keys],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[keys].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
