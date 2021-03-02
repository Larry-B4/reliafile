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

def copy_file(f): # Function to copy file from one folder to another

def create_folder(f): # Function to create folders when needed

def delete_file(f): # Function to delete file

def update_file(f): # Function to update file in destination folder when it's modified in observed folder

# Check if initial files need to be copied

if observe_settings['copy_initial_files']:
    allFiles = os.listdir(observed_folder)
    if observe_settings['sort_files']:
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

def make_folders():
    outputFolderPath = ".\Output"
    pdfFolderPath = ".\Output\PDF_Files"
    imageFolderPath = ".\Output\Image_Files"
    txtFolderPath = ".\Output\TXT_Files"
    docxFolderPath = ".\Output\docx_Files"
    otherFolderPath = ".\Output\other"
    # Create destination folder
    if not os.path.exists(outputFolderPath):
        os.makedirs(outputFolderPath)
    # Create folder for PDF files
    if not os.path.exists(pdfFolderPath):
        os.makedirs(pdfFolderPath)
    # Create folder for PNG files
    if not os.path.exists(imageFolderPath):
        os.makedirs(imageFolderPath)
    # Create folder for TXT files
    if not os.path.exists(txtFolderPath):
        os.makedirs(txtFolderPath)
    # Create folder for docx files
    if not os.path.exists(docxFolderPath):
        os.makedirs(docxFolderPath)
    # Create folder for all other files
    if not os.path.exists(otherFolderPath):
        os.makedirs(otherFolderPath)


def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    make_folders()


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
