# Log Analysis
Udacity full stack web development nanodegree program project

## Project Overview
The task is to create a reporting tool that prints out reports based on the data in the database 'newsdata'. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Prerequisites
If these applications are not installed in your computer, you can download and install them from the links.
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)
* [Git](https://git-scm.com/)


##  Steps to access the project

 1. If not already installed in your system, download the latest version of python from the above link.
 2. Download and install Vagrant and VirtualBox.
 3. Clone this repository by running `git clone https://github.com/gowriprathap/Log_Analysis.git` in your terminal.
 4. Download [the newsdata database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into the vagrant folder.
 5. cd into the vagrant folder using your bash interface.
 6. Launch the virtual machine with `vagrant up` using git bash.
 7. This may take a long time depending on the speed of your internet. After the necessary files have been downloaded and installed, use `vagrant ssh` to log in with your SSH.
 8. The command line will now start with vagrant in a linux environment.
 9. cd into the /vagrant folder.
 10. To load the database run `psql -d news -f newsdata.sql` in your terminal.
 11. In the future to run the database, type `psql -d news`.
 12. Run the commands from the Create views section in the README file here in the terminal (with vagrant running) to run the python program.
 13. Run command `python log.py` to run the python program that displays the query results.
