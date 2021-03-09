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
# delete_files: default(false), sort_files: default(true), copy_initial_files: default(false)
destination_folder = settings['destination_folder']
observe_settings = settings['observe_settings']

# All custom methods


def create_file(curr_file_src):
    if(observe_settings['sort_files']):
        file_extension = get_file_extension(curr_file_src)

        if file_extension == ".txt":
            txtFolderPath = destination_folder + "\\TXT_Files"
            create_folder(txtFolderPath)
            move_file(curr_file_src, txtFolderPath)
        elif file_extension == ".pdf":
            pdfFolderPath = destination_folder + "\\PDF_Files"
            create_folder(pdfFolderPath)
            move_file(curr_file_src, pdfFolderPath)
        elif file_extension == ".png":
            imageFolderPath = destination_folder + "\\Image_Files"
            create_folder(imageFolderPath)
            move_file(curr_file_src, imageFolderPath)
        elif file_extension == ".docx":
            docxFolderPath = destination_folder + "\\docx_Files"
            create_folder(docxFolderPath)
            move_file(curr_file_src, docxFolderPath)
        else:
            otherFolderPath = destination_folder + "\\other"
            create_folder(otherFolderPath)
            move_file(curr_file_src, otherFolderPath)
    else:
        move_file(curr_file_src, destination_folder)


def get_file_extension(sourcePath):
    # Get filename extension
    filename, file_extension = os.path.splitext(sourcePath)
    return file_extension


def create_folder(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


def move_file(sourcePath, destinationPath):
    shutil.copy(sourcePath, destinationPath)

    if(observe_settings['delete_files']):
        delete_file(sourcePath)


def delete_file(curr_file_src):  # Function to delete file
    # Wait a few seconds, so the user has time to rename the file
    time.sleep(5)
    base = os.path.basename(curr_file_src)

    for root, dirs, files in os.walk(observed_folder):
        for name in files:
            if name.endswith((base)):
                os.remove(os.path.join(root, name))


# Function to delete old file after rename
def delete_file_after_rename(old_file_src):
    base = os.path.basename(old_file_src)

    for root, dirs, files in os.walk(destination_folder):
        for name in files:
            if name.endswith((base)):
                os.remove(os.path.join(root, name))


# Check if initial files need to be copied
if observe_settings['copy_initial_files']:
    for subdir, dirs, files in os.walk(observed_folder):
        for f in files:
            if os.path.isfile(os.path.join(subdir, f)):
                create_file(os.path.join(subdir, f))

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
    if os.path.isfile(event.src_path):
        create_file(event.src_path)


def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")


def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
    if os.path.isfile(event.src_path):
        create_file(event.src_path)


def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

    # If a file has been renamed it needs to be copied
    if os.path.isfile(event.dest_path):
        create_file(event.dest_path)
    # Delete the old file after renaming
    delete_file_after_rename(event.src_path)


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
