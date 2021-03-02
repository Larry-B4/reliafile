import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import shutil
import os
import json

# Read project_settings.json file and insert information into global variables
with open("project_settings.json") as json_data_file:
    settings = json.load(json_data_file)

observed_folder = settings['observed_folder']
destination_folder = settings['destination_folder']
observe_settings = settings['observe_settings'] # delete_files: default(false), sort_files: default(true), copy_initial_files: default(false)

# All custom methods

def get_file_extension(sourcePath):
    # Get filename extension
    filename, file_extension = os.path.splitext(sourcePath)

    if file_extension == ".txt":
        txtFolderPath = destination_folder + "\\TXT_Files"
        create_folder(txtFolderPath)
        move_file(sourcePath, txtFolderPath)
    elif file_extension == ".pdf":
        pdfFolderPath = destination_folder + "\\PDF_Files"
        create_folder(pdfFolderPath)
        move_file(sourcePath, pdfFolderPath)
    elif file_extension == ".png":
        imageFolderPath = destination_folder + "\\Image_Files"
        create_folder(imageFolderPath)
        move_file(sourcePath, imageFolderPath)
    elif file_extension == ".docx":
        docxFolderPath = destination_folder + "\\docx_Files"
        create_folder(docxFolderPath)
        move_file(sourcePath, docxFolderPath)
    else:
        otherFolderPath = destination_folder + "\\other"
        create_folder(otherFolderPath)
        move_file(sourcePath, otherFolderPath)

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(sourcePath, destinationPath):
    shutil.copy(sourcePath, destinationPath)

def delete_file(f):
    print() # Function to delete file

def update_file(f):
    print() # Function to update file in destination folder when it's modified in observed folder

# Check if initial files need to be copied

if observe_settings['copy_initial_files']:
    allFiles = os.listdir(observed_folder)
    if observe_settings['sort_files']:
        print()
        # Write some code to sort the files into folders
    else:
        for f in allFiles:
            shutil.copy(observed_folder + '\\' + f, destination_folder)

# Start observing the folder

if __name__ == "__main__":
    patterns = "*"  # Patterns that we want to handle
    ignore_patterns = ""  # Patterns that will be ignored
    ignore_directories = False
    case_sensitive = True  # Patterns are treated case-sensitive
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)

# Methods to be called when a specific event is raised

def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    get_file_extension(event.src_path)


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

path = observed_folder  # Monitored Path
go_recursively = True  # Subdirectories are monitored as well
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
