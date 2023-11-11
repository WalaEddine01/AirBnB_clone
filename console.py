#!/usr/bin/python3
"""
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
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
        pass

    def do_show(self, line):
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
