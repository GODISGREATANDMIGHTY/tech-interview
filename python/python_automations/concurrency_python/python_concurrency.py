
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def task():
    print("task now")
    time.sleep(1)
    return "done"

def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(task) for _ in range(4)]

    for future in as_completed(futures):
        result = future.result()
        print("Task completed: ", result)



if __name__ == '__main__':
    main()