import cmd

class AddressBook(cmd.Cmd):
    intro = "Welcome to my Address Book. Type 'help' for more info.\n")
    prompt = "(Address Book> )"

    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """Adds a new contact. Usage: add <name> <phonenumber>"""
        name, phone = args.split()
        if name not in self.contacts:
            self.contacts[name] = phone
            print(f"Contact added: {name} - {phone}")

