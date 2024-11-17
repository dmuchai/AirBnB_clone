#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from shlex import split
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for hbnb"""
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            }

    def emptyline(self):
        """
        Do nothing when an empty line + ENTER is entered
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF (Ctrl+D)
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        args = split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        """
        args = split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        args = split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representations of all instances
        """
        args = split(args)
        all_objects = models.storage.all()
        if args:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            print([
                str(obj)
                for key, obj in all_objects.items()
                if key.startswith(args[0])
                ])
        else:
            print([str(obj) for obj in all_objects.values()])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """
        args = split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = models.storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif attr_value.replace('.', '', 1).isdigit():
                attr_value = float(attr_value)
            else:
                attr_value = attr_value.strip('"')
            setattr(instance, attr_name, attr_value)
            instance.save()
        except Exception:
            print("** value error **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
