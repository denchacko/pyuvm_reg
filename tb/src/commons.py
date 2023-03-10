import enum

DEBUG = 1

@enum.unique
class Opcode(enum.IntEnum):
    READ = 1
    WRITE = 2

# To print multiline strings and remove any leading tabspaces
def print_multiline(string, return_val = False):
    '''
    If return_val == False, just print the string
    Else don't print, return the formatted string
    '''
    _ = [line.strip() for line in string.split("\n")]
    if(DEBUG):
       print(f"print_multiline : {_}")

    formatted_string = "\n".join(_)

    if(return_val):
        return formatted_string
    else:
        print(formatted_string)

def fatal_exit(msg = "", status = 1):
    print(f"FATAL: {msg}. exit_status = {status}")
    exit(status)
