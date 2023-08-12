#!/usr/bin/python3
"""
This module defines the HBNBCommand class,
which is the entry point of the command interpreter.
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter."""
    # Set the custom prompt
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        Args:
            self (HBNBCommand): the current instance
            arg (str): the class name
        """
        if not arg:
            print("** class name missing **")
        elif arg not in  ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel"
                # Create a new instance of BaseModel
                obj = BaseModel()
            elif arg == "User"
                # Create a new instance of User
                obj = User()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Usage: show <class name> <id>
        Args:
            self (HBNBCommand): the current instance
            arg (str): the class name and id separated by a space
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Create the key by concatenating the class name and id
            key = "{}.{}".format(args[0], args[1])
            # Get the object from storage
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                # Print the string representation of the object
                print(obj)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class name> <id>
        Args:
            self (HBNBCommand): the current instance
            arg (str): the class name and id separated by a space
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Create the key by concatenating the class name and id
            key = "{}.{}".format(args[0], args[1])
            # Get the object from storage
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                # Delete the object from storage
                del storage.all()[key]
                # Save changes to storage
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all [class name]
        Args:
            self (HBNBCommand): the current instance
            arg (str): optional, the class name
        """
        if arg and arg not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            objs = []
            for key, value in storage.all().items():
                if not arg or key.startswith(arg + "."):
                    # Add string representation of object to list
                    objs.append(str(value))
            # Print list of string representations
            print(objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Args:
            self (HBNBCommand): the current instance
            arg (str): arguments separated by spaces
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Create key by concatenating class name and id
            key = "{}.{}".format(args[0], args[1])
            # Get object from storage
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                # Get attribute name
                attr_name = args[2]
                # Get attribute value
                attr_value = args[3]
                if attr_name in ["id", "created_at", "updated_at"]:
                    return
                if hasattr(obj, attr_name):
                    # Get attribute type
                    attr_type = type(getattr(obj, attr_name))
                    # Cast attribute value to attribute type
                    attr_value = attr_type(attr_value)
                # Set attribute on object
                setattr(obj, attr_name, attr_value)
                # Save changes to storage
                obj.save()

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