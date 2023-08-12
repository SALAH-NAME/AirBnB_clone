#!/usr/bin/python3
"""
This module defines the HBNBCommand class,
which is the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter."""
    # Set the custom prompt
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Args:
            self (HBNBCommand): the current instance
            arg (str): not used here
        Returns:
            bool: True to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        Args:
            self (HBNBCommand): the current instance
            arg (str): not used here
        Returns:
            bool: True to exit the program
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything.
        Args:
            self (HBNBCommand): the current instance
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
