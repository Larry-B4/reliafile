# Reliafile
> Simply observe and sort your folders

Reliafile is a project with the goal of making it easier for our users to observe a folder and copy and sort the files into a second folder. There's multiple settings our users can choose from to define what happens to the files.

## Installation

Windows:

Simply use the project_settings.json file to define the settings you would like to use in your project.
Then define a task in the task scheduler and add an action with the reliafile.bat file with your desired trigger.

The task scheduler is optional, you can also simply execute the reliafile.bat script and stop executing it with CTRL+C.

## Usage example

Use reliafile when working on projects that require a large amount of files you would like the program to automatically sort into folders according to the file endings. You can use this project while working and it will continuously keep track of your files.

## Development setup

To run this project you will need to install python and watchdog.
Install the newest version of python on the Microsoft Store and then install watchdog through a terminal:

```sh
pip install watchdog
```

## Release History

* 1.0.0
    * Initial release
* 0.0.1
    * Work in progress

## Meta

Nathan Widmer - nathan.widmer@edu.tbz.ch and Larissa Bosshard - larissa.bosshard@edu.tbz.ch