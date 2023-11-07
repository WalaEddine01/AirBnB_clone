import cmd

class MyCmd(cmd.Cmd):
    intro = "Welcom to my cmd, type 'help' for more commands.\n"
    prompt = "(mycmd)"

    def do_great(self, *args):
        """Greets the user"""
        print("Hey there, how may I help you?")

    def do_sum(self, *args):
        """Sum Two nums"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 + num2
            print(f"The sum is {result}")
        except ValueError:
            print("Invalid input. Usage sum <num1> <num2>")

    def do_multiply(self, *args):
        """Multiplies two numbers"""
        try:
            num1, num2 = map(float, args.split())
            result = num1 * num2
            print(f"The product is {result}")
        except ValueError:
            print("Invalid input. Usage multiply <num1> <num2>")

        def do_exit(self, *args):
        """Exits the console"""
        print("Exiting the console.")
        return True  # This is the signal to exit the command line interface

if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()

