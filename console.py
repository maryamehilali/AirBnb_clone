#!/usr/bin/python3
"""command interpreter"""
import cmd
from base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter for the AirBnb-clone the console project"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True
    
    def do_EOF(self, args):
        """Exit the command interpreter when typing "control-D"\n"""
        print ('\n')
        return True
    
    def emptyline(self):
        """a method called to make sure that an empty line + ENTER
        shouldn't execute anything\n"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        arguments = args.split()
        if len(arguments) >= 1:
            if arguments[0] == "BaseModel":
                instance = BaseModel()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id"""
        arguments = args.split()
        if len(arguments) >= 1:
            if arguments[0] == "BaseModel":
                if len(arguments) >= 2:
                    if arguments[1]: 
                        """if id exists print the instance"""
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    