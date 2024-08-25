from function_loggers import LogFunctionCallAndCompletion
import time
from thread_wrapper import RunInSeperateThread

class test_class:
    def __init__(self):
        self.x = 6

    @LogFunctionCallAndCompletion
    def change_x_to(self, y):
        time.sleep(1.25)
        self.x = y

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
@LogFunctionCallAndCompletion
def slow_fibonacci2(n):
    if n <= 1:
        return n
    return slow_fibonacci2(n - 1) + slow_fibonacci2(n - 2)

@RunInSeperateThread
@LogFunctionCallAndCompletion
def timing_function():
    print("started_timing")
    time.sleep(3)
    print("finished_timing")

for i in range(10):
    timing_function()
