# Sites Monitoring Utility

Allows to bulk check health of given websites

## Usage
```
pip install -r requirements.txt
python check_sites_health.py -i --input_file [-d --prepaid_delta]
```
Requires a path to the list of urls in a .txt file as an input. One full url (http://www.example.com) per line. Outputs result on health checks. 

## Options

`-i --input_file` - path to the .txt file with a list of urls

`-d --prepaid_delta` - minimal number of days to be prepaid in advance for domain. Default is 30 days.

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
