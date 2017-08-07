# Watcher of Friends Online

Checks friends online on vk.com and outputs results in pryttified json to the console

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```
pip install -r requirements.txt # alternatively try pip3

$ python3 vk_friends_online.py 
Enter login:  <login>
Password: 

Online FRIENDS:
[
    {
        "first_name": "Georges",
        "last_name": "Duroy",
        "uid": 310465879
    },
    {
        "first_name": "Иришка",
        "last_name": "Счастливая",
        "uid": 340718839
    },
    {
        "first_name": "Джек",
        "last_name": "Воробей",
        "uid": 412128272
    },
]

```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
