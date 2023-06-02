import os
import sys
from itertools import count


# 0, 1, 1, 2, 3, 5, 8, ...
def get_nth_fibonacci_number(n):
    a = 0
    b = 1
    if n < 0:
        return -1 # error
    elif 0 == n:
        return a
    
    for _ in range(1, n):
        tmp_a = a
        a = b
        b = tmp_a + b
    return b


def child_ipc_loop():
    
    print('child: started', file=sys.stderr)
    
    for index in count():
    
        print(f'child: begin iteration {index}', file=sys.stderr)
        
        # read 8 bytes of binary data from stdin;
        # these 8 bytes are the binary representation of an integer
        # that will be submitted to the child by its parent;
        # this call to os.read will block until the parent writes the 8 bytes
        input_bytes = os.read(sys.stdin.fileno(), 8)
        
        # covert the bytes to a Python int object
        input_int = int.from_bytes(input_bytes, byteorder='big', signed=True)
        
        output_int = get_nth_fibonacci_number(input_int)
        
        # convert the Fibonacci number from its representation as a Python
        # int object to a sequence of 8 bytes
        output_bytes = output_int.to_bytes(8, byteorder='big', signed=True)
        
        os.write(sys.stdout.fileno(), output_bytes)
        
        print(
            f'child: checking if iteration {index} is the last',
            file=sys.stderr
        )
        
        if output_int < 0:
            break

    print('child: exiting', file=sys.stderr)


if '__main__' == __name__:
    child_ipc_loop()
