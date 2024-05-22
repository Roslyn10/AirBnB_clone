#!/usr/bin/pyhon3
"""Implementing the HBHBC console/ Entry point for the console"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


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
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string rep of an instance based on class name"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] no in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0].{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes the instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
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
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if not args:
            instances = [str(obj) for obj in storage.all().values()]
        else:
            instances = {
                    [str(obj) for key,
                        obj in storage.all().items() if key.startwith(args[0])]
                    }
            print(instances)

    def do_update(self, arg):
        """Updates an instance base on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0].{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print(" 88 attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')

        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            attr_value = attr_type(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** attribute doesnt exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
