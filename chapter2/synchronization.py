import threading
import time

# Define the semaphore with a limit (e.g., allowing up to 2 threads to access the resource simultaneously)
sem = threading.Semaphore(2)

def access_resource(thread_name):
    sem.acquire()
    print(f"{thread_name} accessing the resource")
    time.sleep(2)
    print(f"{thread_name} done")
    sem.release()

threads = []

for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
