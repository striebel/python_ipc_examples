import os
import sys
import subprocess
from itertools import count


def start_child():
    
    print('parent: starting child', file=sys.stderr)
    
    popen_object = subprocess.Popen(
        ['python', 'child.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    
    print('parent: done starting child', file=sys.stderr)
    
    return popen_object


def parent_ipc_loop(popen_object):
    
    for index in count():
       
       print(f'parent: begin iteration {index}', file=sys.stderr)
       
       sys.stdout.write('Enter some n to obtain the nth Fibonacci number > ')
       sys.stdout.flush()
       while True:
           input_str = sys.stdin.readline().strip()
           if 0 < len(input_str):
               break
           sys.stdout.write('> ')
           sys.stdout.flush()
       
       try:
           input_int = int(input_str)
       except ValueError:
           input_int = -1
       
       # covert the n, which is represented as a Python int object,
       # to a sequence of 8 bytes
       input_bytes = input_int.to_bytes(8, byteorder='big', signed=True)
       
       os.write(popen_object.stdin.fileno(), input_bytes)
       
       # read the 8-byte response from the child
       output_bytes = os.read(popen_object.stdout.fileno(), 8)
       
       # convert the Fibonacci number from its representation as a
       # sequence of 8 bytes to a Python in object
       output_int = int.from_bytes(output_bytes, byteorder='big', signed=True)
       
       print(
           f'parent: checking if iteration {index} is the last',
           file=sys.stderr
       )
       
       if 0 <= output_int:
           assert 0 <= input_int
           suffix = 'th'
           if '1' == input_str[-1] and '11' != input_str[-2:]:
               suffix = 'st'
           elif '2' == input_str[-1] and '12' != input_str[-2:]:
               suffix = 'nd'
           elif '3' == input_str[-1] and '13' != input_str[-2:]:
               suffix = 'rd'
           print(f'The {input_int}{suffix} Fibonacci number is {output_int}')
       else:
           assert input_int < 0
           print(f'"{input_str}" is not a non-negative integer, exiting')
           break


def main():
    print('parent: starting', file=sys.stderr)
    popen_object = start_child()
    parent_ipc_loop(popen_object)
    print('parent: exiting', file=sys.stderr)


if '__main__' == __name__:
    main()
