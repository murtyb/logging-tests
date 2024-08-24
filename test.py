from function_loggers import LogFunctionCallAndCompletion
import time

class test_class:
    def __init__(self):
        self.x = 6

    @LogFunctionCallAndCompletion
    def change_x_to(self, y):
        time.sleep(1.25)
        self.x = y

TestClass = test_class()
TestClass.change_x_to(10)