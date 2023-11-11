#!/usr/bin/python3
"""
This modual contains the HBNBCommand class that represants the HBNB console
"""
import cmd
from models.base_model import BaseModel
import models

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
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
