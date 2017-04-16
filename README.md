# sincedb-status [WIP]

A simple REST interface to check the status of sincedb that logstash maintains to track the status of files processed.

## Prerequisites
* python 3.6

## Installation

* Clone the repository on the server where logtash is running
* Run `python app.py`
* Access the status by running: `http://127.0.0.1:5000/status?sincedb={path_to_sincedb_on_server}&path={path_to_root_of_log_folder}`
    * eg: `http://127.0.0.1:5000/status?sincedb=/opt/elk_input/sincedb&path=/opt/elk_input/logs/`
    