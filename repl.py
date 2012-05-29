#!/usr/bin/python

from sparse import sprint
from SInterpreter import SInterpreter

def main():
    """Run the REPL."""
    interp = SInterpreter()
    while True:
        try:
            sprint(interp.seval(input('>>> ')))
        except IndexError:
            print('Index error: are you missing a closing parenthesis?')
        except EOFError:
            print('Bye')
            return
        except Exception as e:
            print('Error: ' + str(e))
    

if __name__ == '__main__':
    main()
