# Name: Adam Kaci
# Date: 11/15/2023
# File Purpose: To act as a bot in charge of managing the Tuffy inventory

import threading
import time
import json


def bot_fetcher(item_numbers, cart, lock, inventory):
    for item_num in item_numbers:
        time.sleep(inventory[item_num][1])  # Simulate fetching time
        item_info = [item_num, inventory[item_num][0]]
        with lock:
            cart.append(item_info)

def bot_clerk(items, inventory=None):
    # Load inventory from file if not provided
    if inventory is None:
        with open('inventory.dat', 'r') as file:
            inventory = json.load(file)

    if not items:  # Check if the list is empty
        return []  # Return an empty cart if no items are provided

    cart = []
    lock = threading.Lock()

    # Split items into up to 3 lists
    fetcher_lists = [[] for _ in range(min(3, len(items)))]
    for i, item in enumerate(items):
        fetcher_lists[i % len(fetcher_lists)].append(item)

    # Start a thread for each fetcher
    threads = []
    for fetcher_list in fetcher_lists:
        thread = threading.Thread(target=bot_fetcher, args=(fetcher_list, cart, lock, inventory))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return cart
