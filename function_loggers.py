from logging_src import logger
import inspect
import time

def LogFunctionCall(func):
    def function_with_logs(*args, **kwargs):
        arg_names_and_values = get_arg_names_and_values(func, args, kwargs)
        logger.debug(f"{func.__name__} was called" , extra=arg_names_and_values)
        return func(*args, **kwargs)
    function_with_logs.__name__ = func.__name__
    return function_with_logs

def LogFunctionCompletion(func):
    def function_with_logs(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        end_time = time.time()
        logger.debug(f"{func.__name__} has completed" , extra={"completion time": round(end_time - start_time, 2)})
        return output
    function_with_logs.__name__ = func.__name__
    return function_with_logs

def LogFunctionCallAndCompletion(func):
    return LogFunctionCompletion(LogFunctionCall(func)) 


def get_arg_names_and_values(func, args, kwargs):
    func_args = inspect.signature(func).parameters
    arg_names_and_values = {name: value for name, value in zip(func_args, args)}
    arg_names_and_values.update(kwargs)
    remove_self(arg_names_and_values)
    return arg_names_and_values

def remove_self(arg_names_and_values):
    if "self" in arg_names_and_values.keys():
        del arg_names_and_values["self"]