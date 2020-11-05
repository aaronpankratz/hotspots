# hotspots
simple python script for detecting hotspots of technical debt in source code

## requirements
Python3 `brew install python3`
cloc `brew install cloc`
git `brew install git`

## usage
copy this script into your source code repository
run the script with `python3 hotspts.py`
the script will create a sqlite db `hotspots.db`
connect to the db to analyze your files
`sqlite3 hotspots.db`

`select name, change_frequency, code from files order by change_frequency desc, code desc;`

look for large files that have a high change frequency and consider refactoring these files.
