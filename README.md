# hotspots
simple python script for detecting hotspots of technical debt in source code

## requirements
Python3 `brew install python3`  
cloc `brew install cloc`  
git `brew install git`  

## usage
1. copy this script into your source code repository
1. run the script with `python3 hotspots.py`  
1. the script will persist a sqlite db `hotspots.db` to your file system, connect to the db to analyze your files `sqlite3 hotspots.db`

The database has one table, `files`, with columns `name, change_frequency, blank, comment, code`

`name` is the name of the file, including the path

`change_frequency` is the number of git commits the file is included in

`blank` is the number of blank lines in the file

`comment` is the number of comment lines in the file

`code` is the number of code lines in the file

For example run the following query:
```
select name, change_frequency, code from files order by change_frequency desc, code desc;
```
Then, look for large files that have a high change frequency and consider refactoring these files.  
