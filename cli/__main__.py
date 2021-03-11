import sys
from .classmodule import MyClass
from .welcome import wel

def main():
    args = sys.argv[1:]
    # print(args)
    try:
        if args[0] == "deepak":
            try:
                if args[1] == "-h":
                    print("no help command has been set yet")
            except:
                wel("Dupeeer")
    except:
        print('Expected atleast one argument.')

    # my_object = MyClass('Thomas')
    # my_object.say_name()

if __name__ == '__main__':
    main()