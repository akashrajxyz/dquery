# Dquery
An API written in flask which takes GET request at /1/queries/count/<DATE_PREFIX> endpoint : returns a JSON object specifying the number of distinct query between that time interval.

## Requirements
- Python 3.7.x
- Flask 2.x 
- db-sqlite3

## Installation

```sh
git clone https://github.com/dasagreeva/query.git
cd dquery 


```

### Running with Gunicorn
```
pip install -r requirements.txt
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 api:app

```

```

## Usage
After running the server on some port (it use port =5000= by default).
Send a POST request using =curl=.
```sh
curl https://localhost:5000/1/queries/count/2015-08-03
{"count": 3}
```
