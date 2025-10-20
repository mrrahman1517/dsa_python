"""
Timer Library - A comprehensive timing utility for measuring code execution time.

This module provides a Timer class with exception handling for measuring
elapsed time of code execution with high precision.

Author: DSA Python Project
Date: October 2025
"""

import time


class TimerException(Exception):
    """A custom exception used to report errors when using Timer class."""
    pass


class Timer:
    """
    A high-precision timer class for measuring code execution time.
    
    This class provides functionality to start timing, stop timing,
    and retrieve elapsed time with proper error handling and state management.
    
    Attributes:
        _start_time (float or None): Stores the start time or None if not started
        _elapsed_time (float or None): Stores the elapsed time or None if not measured
    
    Example:
        >>> timer = Timer()
        >>> timer.start()
        >>> # Some code to time
        >>> timer.stop()
        >>> print(f"Elapsed: {timer.elapsed():.4f} seconds")
        >>> print(timer)  # Uses __str__ method
    """
    
    def __init__(self):
        """
        Initialize the Timer with default values.
        
        Sets both start time and elapsed time to None to indicate
        the timer has not been used yet.
        """
        self._start_time = None
        self._elapsed_time = None
    
    def start(self):
        """
        Start the timer by recording the current time.
        
        Uses time.perf_counter() for the highest available resolution timer.
        
        Raises:
            TimerException: If the timer is already running (start() called twice).
        
        Example:
            >>> timer = Timer()
            >>> timer.start()
        """
        if self._start_time is not None:
            raise TimerException("Timer is running, use stop() before starting again")
        self._start_time = time.perf_counter()

    def stop(self):
        """
        Stop the timer and calculate the elapsed time.
        
        Calculates the difference between current time and start time,
        then resets the start time to None for next use.
        
        Raises:
            TimerException: If the timer is not running (stop() called before start()).
        
        Example:
            >>> timer = Timer()
            >>> timer.start()
            >>> # Some work here
            >>> timer.stop()
        """
        if self._start_time is None:
            raise TimerException("Timer is not running, use start() first")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """
        Return the elapsed time in seconds.
        
        Returns:
            float: The elapsed time between the last start() and stop() calls.
        
        Raises:
            TimerException: If the timer has not been run yet (no start/stop cycle).
        
        Example:
            >>> timer = Timer()
            >>> timer.start()
            >>> # Some work
            >>> timer.stop()
            >>> print(f"Time taken: {timer.elapsed():.4f} seconds")
        """
        if self._elapsed_time is None:
            raise TimerException("Timer has not run yet, use start() and stop() first")
        return self._elapsed_time
    
    def reset(self):
        """
        Reset the timer to initial state.
        
        Clears both start time and elapsed time, allowing the timer
        to be used fresh again.
        
        Example:
            >>> timer = Timer()
            >>> timer.start()
            >>> timer.stop()
            >>> timer.reset()  # Now timer is like new
        """
        self._start_time = None
        self._elapsed_time = None
    
    def is_running(self):
        """
        Check if the timer is currently running.
        
        Returns:
            bool: True if timer is running (start() called but not stop()), False otherwise.
        
        Example:
            >>> timer = Timer()
            >>> print(timer.is_running())  # False
            >>> timer.start()
            >>> print(timer.is_running())  # True
            >>> timer.stop()
            >>> print(timer.is_running())  # False
        """
        return self._start_time is not None
    
    def __str__(self):
        """
        Return a string representation of the elapsed time.
        
        Returns:
            str: Formatted elapsed time with 6 decimal places or status message.
        
        Example:
            >>> timer = Timer()
            >>> timer.start()
            >>> timer.stop()
            >>> print(timer)  # "0.001234 seconds"
        """
        if self._elapsed_time is None:
            return "Timer has not run yet"
        return f"{self._elapsed_time:.6f} seconds"
    
    def __repr__(self):
        """
        Return a detailed string representation for debugging.
        
        Returns:
            str: Detailed representation showing internal state.
        """
        return (f"Timer(running={self.is_running()}, "
                f"elapsed={self._elapsed_time})")

    def __enter__(self):
        """
        Context manager entry - start the timer.
        
        Returns:
            Timer: The timer instance for use in with statement.
        
        Example:
            >>> with Timer() as timer:
            ...     # Some code to time
            ...     pass
            >>> print(f"Elapsed: {timer.elapsed()}")
        """
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit - stop the timer.
        
        Args:
            exc_type: Exception type (if any)
            exc_val: Exception value (if any) 
            exc_tb: Exception traceback (if any)
        """
        self.stop()


# Utility functions for common timing operations

def time_function(func, *args, **kwargs):
    """
    Time the execution of a function call.
    
    Args:
        func: The function to time
        *args: Positional arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
    
    Returns:
        tuple: (result, elapsed_time) where result is the function's return value
               and elapsed_time is the time taken in seconds.
    
    Example:
        >>> result, time_taken = time_function(sum, range(1000000))
        >>> print(f"Sum: {result}, Time: {time_taken:.4f}s")
    """
    timer = Timer()
    timer.start()
    result = func(*args, **kwargs)
    timer.stop()
    return result, timer.elapsed()


def compare_functions(func1, func2, *args, **kwargs):
    """
    Compare the execution time of two functions with the same arguments.
    
    Args:
        func1: First function to time
        func2: Second function to time
        *args: Positional arguments to pass to both functions
        **kwargs: Keyword arguments to pass to both functions
    
    Returns:
        dict: Dictionary containing results and timing information
    
    Example:
        >>> def method1(n): return sum(range(n))
        >>> def method2(n): return n*(n-1)//2
        >>> comparison = compare_functions(method1, method2, 10000)
        >>> print(f"Method 1: {comparison['time1']:.6f}s")
        >>> print(f"Method 2: {comparison['time2']:.6f}s")
    """
    result1, time1 = time_function(func1, *args, **kwargs)
    result2, time2 = time_function(func2, *args, **kwargs)
    
    faster = "func1" if time1 < time2 else "func2"
    speedup = max(time1, time2) / min(time1, time2)
    
    return {
        'result1': result1,
        'result2': result2,
        'time1': time1,
        'time2': time2,
        'faster': faster,
        'speedup': speedup
    }