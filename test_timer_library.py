#!/usr/bin/env python3
"""
Simple test script to verify the Timer library works correctly

Author: Muntasir Raihan Rahman
"""

# Test basic import
try:
    from timer_lib import Timer, TimerException, time_function, compare_functions
    print("SUCCESS: Successfully imported Timer library!")
except ImportError as e:
    print(f"ERROR: Import failed: {e}")
    exit(1)

# Test basic functionality
try:
    import time
    
    print("\nTEST: Testing basic Timer functionality:")
    timer = Timer()
    timer.start()
    time.sleep(0.1)  # Sleep for 100ms
    timer.stop()
    print(f"   Elapsed time: {timer.elapsed():.4f} seconds")
    print(f"   Timer string: {timer}")
    
    print("\nTEST: Testing context manager:")
    with Timer() as ctx_timer:
        sum_result = sum(range(100000))
    print(f"   Sum result: {sum_result}")
    print(f"   Time taken: {ctx_timer}")
    
    print("\nTEST: Testing utility functions:")
    result, timing = time_function(sum, range(50000))
    print(f"   sum(range(50000)) = {result}")
    print(f"   Time taken: {timing:.6f} seconds")
    
    print("\nSUCCESS: All tests passed! Timer library is working correctly.")
    
except Exception as e:
    print(f"ERROR: Test failed: {e}")
    import traceback
    traceback.print_exc()