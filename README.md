# CLOG

A simple CLI logging tool. 
Created for sake of organising notes, and as a personal work journal.

## Commands
All commands come with some predefined options. 
Check `help` for more options.

### init
Start by running `clog init`. 

Creates a base directory(`~/.clog`) where log files will be stored, and a common log file inside.

### ls
Lists all log files found in the base directory.

### create
Creates a new log file.

### write
Writes a log in the specified file, or in the common one by default. 

### read
Reads from the specified log files.

## How to install

Clone this repo locally.
`git clone https://github.com/vernierm/clog.git`

Position in the cloned repo.

Make `clog` file executable.
`chmod +x clog`

Add repo path to your PATH environment variable, so you can run it from anywhere.
`export PATH=$PATH:/path/to/cloned/repo`
