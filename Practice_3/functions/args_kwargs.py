def sum_everything(*args):
    return sum(args) # Можно передать 2, 10 или 100 чисел


def show_list(*items):
    for item in items:
        print(f"- {item}")


def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Вызов: user_profile(name="Bob", age=25)


def log_data(message, *tags, **metadata):
    print(f"MSG: {message} | Tags: {tags} | Info: {metadata}")


def join_with_dash(*words):
    return "-".join(words)