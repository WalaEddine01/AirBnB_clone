#!/usr/bin/python3
"""
This modual contains the HBNBCommand class that represants the HBNB console
"""
import cmd
from models.base_model import BaseModel
import models
import re


class HBNBCommand(cmd.Cmd):
    """
    This class for the hbnb console
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """
        This method used to creat an instance from BaseModel class
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                name = f'{args[0]}.{args[1]}'
                a = 0
                for k in models.storage.all().keys():
                    if k == name:
                        print(models.storage.all()[k])
                        a = 1
                if a == 0:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        This method to Deletes an instance based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                name = f'{args[0]}.{args[1]}'
                a = 0
                for k in models.storage.all().keys():
                    if k == name:
                        a = 1
                        del models.storage.all()[k]
                        models.storage.save()
                        break
                if a == 0:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based on the cls name
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            if line != "BaseModel":
                print("** class doesn't exist **")
            else:
                con = models.storage.all()
                li = []
                for k, v in con.items():
                    if type(v).__name__ == "BaseModel":
                        li.append(str(v))
                print(li)

    def do_update(self, line):
        """
        This method used to Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            patr = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-.{4}-[0-9a-f]{12}$'
            if len(args) < 2 or re.match(patr, args[1]) is None:
                print("** instance id missing **")
                return
            name = f"{args[0]}.{args[1]}"
            if name not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            con = models.storage.all()
            try:
                args[3] = int(args[3])
            except ValueError:
                try:
                    args[3] = float(args[3])
                except ValueError:
                    pass
            setattr(con[name], args[2], args[3])
            models.storage.all()[name].save()

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
