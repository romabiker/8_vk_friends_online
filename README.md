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
        "response": {
            "online": [
                
                341635,
                377398,
                386785,
                  ...

                12605908,
                13555100,
                14321863,
                16360616,
                16628470,
                17237233,
                17631681,
                19498153,
              
            ],
            "online_mobile": [
                22,
                316,
                2943,
                3148,
                6010,
                6492,
                7176,
                10741,
                14099,
                ...        
                54986442,
                92093600,
                97023942,
                100593970
            ]
        }
    }
]


```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
