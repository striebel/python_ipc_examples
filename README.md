# Python Interprocess Communication Examples

## `int` Example

This example shows communication between a parent and child process.
The parent creates the child processes and then submits requests
to the child, where each request is one `int`, and the child responds
to the request, where each response is also one `int`.

When the example is run, after the parent creates the child process, the
child blocks until it receives a request from the parent.
The parent first prompts the user for input.
Once the parent gets the input from the user, the parent makes its
request to the child, and the parent blocks until it receives a
response from the child.
Once the child receives the request from the parent, the child calculates
its response and sends it to the parent; then the child goes back
to the top of its loop and blocks again until it receives the next
request.
The parent reads the response from the child and then displays the
response to the user.
Then the parent goes back to the top of its own loop and displays the
same prompt to the user again.

A request made to the child is one `int` obj *n* and the response is the
*n*th Fibonacci number. The example can be invoked from a bash prompt as
```sh
$ python int_example/parent.py 2> /dev/null
```
If you would like to see debugging output, and a trace in case an exception
occurs, you can omit `2> /dev/null`. An example interactive run is the
following
```sh
Enter some n to obtain the nth Fibonacci number > 
> 
> 
> 0
The 0th Fibonacci number is 0
Enter some n to obtain the nth Fibonacci number > 1
The 1st Fibonacci number is 1
Enter some n to obtain the nth Fibonacci number > 2
The 2nd Fibonacci number is 1
Enter some n to obtain the nth Fibonacci number > 3
The 3rd Fibonacci number is 2
Enter some n to obtain the nth Fibonacci number > 7
The 7th Fibonacci number is 13
Enter some n to obtain the nth Fibonacci number > 10
The 10th Fibonacci number is 55
Enter some n to obtain the nth Fibonacci number > 3
The 3rd Fibonacci number is 2
Enter some n to obtain the nth Fibonacci number > -1
"-1" is not a non-negative integer, exiting
```
Type something other than a non-negative integer, such as `-1`, to exit.
