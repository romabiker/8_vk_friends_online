import getpass
import json
import vk


APP_ID = 6140951


def prettify_json(json_data):
    return json.dumps(
                    json_data,
                    indent=4,
                    sort_keys=True,
                    ensure_ascii=False
                    )


def get_user_login():
    return input('Enter login:  ')


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    vk_api = vk.API(session)
    friends_online = vk_api.friends.getOnline()
    return friends_online


def output_friends_to_console(friends_online):
    print('\nOnline FRIENDS:\n')
    print(prettify_json(friends_online))
    print()


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
