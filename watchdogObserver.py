import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os

if __name__ == "__main__":
    patterns = "*" # Patterns that we want to handle
    ignore_patterns = "" # Patterns that will be ignored
    ignore_directories = False
    case_sensitive = True # Patterns are treated case-sensitive
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)

# Methods to be called when a specific event is raised
def on_created(event):
    print(f"hey, {event.src_path} has been created!")


def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")


def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")


def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

# Define which method is called on which event
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "." # Monitored Path
go_recursively = True # Subdirectories are monitored as well
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
