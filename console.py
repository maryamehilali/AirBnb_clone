#!/usr/bin/python3
"""command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """command interpreter for the AirBnb-clone the console project"""
    prompt = '(hbnb) '
    classes = ["Amenity", "BaseModel", "City", "Place", "Review",
               "State", "User"]

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Exit the command interpreter when typing "control-D"\n"""
        print('\n')
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
            class_name = arguments[0]
            if class_name in HBNBCommand.classes:
                instance = eval(class_name)()
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
            class_name = arguments[0]
            if class_name in HBNBCommand.classes:
                if len(arguments) >= 2:
                    try:
                        print(storage.all()["{}.{}".format(class_name,
                                                           arguments[1])])
                    except Exception:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        arguments = args.split()
        if len(arguments) >= 1:
            class_name = arguments[0]
            if class_name in HBNBCommand.classes:
                if len(arguments) >= 2:
                    try:
                        del storage.all()["{}.{}".format(class_name,
                                                         arguments[1])]
                        storage.save()
                    except Exception:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        arguments = args.split()
        if not arguments or arguments[0] in HBNBCommand.classes:
            list_obj = []
            for key, value in storage.all().items():
                list_obj.append(str(value))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        arguments = args.split()
        if len(arguments) >= 1:
            class_name = arguments[0]
            if class_name in HBNBCommand.classes:
                if len(arguments) >= 2:
                    obj_id = "{}.{}".format(class_name, arguments[1])
                    if obj_id in storage.all():
                        if len(arguments) >= 3:
                            if len(arguments) >= 4:
                                attr_name = arguments[2]
                                attr_value = arguments[3]
                                setattr(storage.all()[obj_id],
                                        attr_name, attr_value)
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
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
