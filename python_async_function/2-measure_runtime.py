
#!/usr/bin/env python3
'''2. Measure the runtime'''


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
'module'


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
