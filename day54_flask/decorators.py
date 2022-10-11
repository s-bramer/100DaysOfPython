import time

def speed_calc_decorator(function):
    """decorator function"""
    function_name = function.__name__
    #print (function_name)
    def calculate_runtime():
        """wrapper function"""
        start_time = time.time()
        function()
        end_time = time.time()
        passed_time = end_time - start_time
        print(f"{function_name} run speed: {passed_time}s")
    return calculate_runtime

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator  
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()