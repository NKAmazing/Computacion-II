# CONSTANTS

# paths
PATH_ENC = "/home/nk-nicolas/Documentos/Computacion-II/Proyecto Final/data/target_folder/"

# data

MATRIX = '''1, 2, 3
4, 5, 6'''

# errors - out of range - empty messages
ARGS_ERR = "Need more arguments to execute the program."
UNK_OP = "ERROR. Unknown operation."
ARGS_ERR_2 = "There was an error with the argument you entered."
SV_ERR = "Failed to create a socket."
SV_ERR_CHECK = "ERROR ON CMD..."

# messages
INPUT_MSG = "Enter a String: "
SQP_MSG = "calculating the square power of: "
SQRT_MSG = "calculating the square root of: "
LOG_MSG = "calculating the logarithm of: "
PS_PID_MSG = "Process"
RESULT_MSG = "Result of the operation: "
END_MSG = "We're done here."
PUT_Q_MSG = "Putting item in queue: "
L_ADDING_MSG = "Adding element to list: "
Q_ADDING_MSG = "Adding element to queue: "
THREAD_MSG = "Thread working on "
THREAD_MSG_2 = "Thread finished "
THREAD_MSG_3 = "Thread reading "
READ_MSG = "Reading... "
READ_PIPE_MSG = "Reading from pipe... "
EXIT_PROCESS = "Finishing process..."
LAUNCH_SVT = "Launching Server with Threads..."
LAUNCH_SVP = "Launching Server with Process..."
SV_MSG = "SERVER REPLY: "
CLIENT_MSG = "ENTER COMMAND TO SEND: "
SV_CHECK = "OK..."

# Server args, msgs, addrs
ADDR_CS = "Address: "
RCV_MSG = "Received: "

# arguments
ARG_STR = "break"
ARG_2_STR = "bye"
ARG_ROT_13 = "rot13"
CHAR_CODE = "ascii"
HOST_ARG = "localhost"

# titles
OP_TITLE = "Solving operation: "


# argparse - click  messages
POOL_ARG_DESCR = "Command line of Pool Example."
PROC_ARG_HELP = "Indicates number of process."
PATH_ARG_HELP = "Indicates path of the file."
OP_ARG_HELP = '''Indicates calculation function.
                    - pot (Square Power)
                    - raiz (Square Root)
                    - log (Logarithm)
'''
TYPE_CONC_HELP = '''Argument to choose a type of concurrency. --> 
                            Threading (t) | Process (p)  
'''
CMD_INFO_HELP = "The command to execute."
PORT_INFO_HELP = "The port where the server will attend."
HOST_INFO_HELP = "The host where the server will attend."

# help messages
HELP_MSG = "To more details, use -h or --help to receive more help."

# operators
JUMP_LINE = "\n"