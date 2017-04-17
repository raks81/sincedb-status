# sincedb-status [WIP]

A simple REST interface to check the status of sincedb that logstash maintains to track the status of files processed. This is useful when parsing log files that were exported out from some application. It can also be used when during performance/system testing logstash implementations where one needs to monitor the progress of the logstash's pipeline.

## Prerequisites
* python 3.6

## Installation

* Clone the repository on the server where logstash is running
* Run `python app.py`
* Access the status by running: `http://127.0.0.1:5000/status?sincedb={path_to_sincedb_on_server}&path={path_to_root_of_log_folder}`
    * eg: `http://127.0.0.1:5000/status?sincedb=/opt/elk_input/sincedb&path=/opt/elk_input/logs/`
    