from queue import Queue
import random
import time


def generate_request(queue, request_body, request_id):
    new_request = f"Request-{request_id}: {request_body}"
    if random.random() > 0.5:
        queue.put(new_request)
        print(f"Згенеровано нову заявку: {new_request}")
        time.sleep(1)
        return i + 1
    return i


def process_request(queue):
    if not queue.empty():
        current_request = queue.get()
        time.sleep(1)
        print(f"Оброблюю заявку {current_request}")
        time.sleep(1)
    else:
        print(f"Черга заявок пуста")


possible_requests = ["Urgent", "Warning", "General", "Info"]

i = 0
queue = Queue()

try:
    while True:
        for _ in range(random.randint(1, 2)):
            i = generate_request(queue, random.choice(possible_requests), i)
        process_request(queue)
except KeyboardInterrupt:
    print("Stopped")
