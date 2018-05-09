from conf import POSSIBLE_USERNAMES, POSSIBLE_PASSWORDS, TEXTFILE_PATH


def get_info():
    in_file = open(TEXTFILE_PATH, "rt")
    contents = in_file.read()
    in_file.close()

    username_line = ''
    username_substring = ''
    password_line = ''
    password_substring = ''

    for line in contents.strip().split('\n'):
        if any(substring in line for substring in POSSIBLE_USERNAMES):
            username_line = line
            username_substring = using_in(line, POSSIBLE_USERNAMES)
        if any(substring in line for substring in POSSIBLE_PASSWORDS):
            password_line = line
            password_substring = using_in(line, POSSIBLE_PASSWORDS)

    return(username_line, username_substring, password_line, password_substring)



def using_in(text, stopwords):
    for word in stopwords:
        if word in text:
            return word
    return ''


def extract_username(username_line, username_substring):
    username = ''
    if username_line:
        username = username_line.split(username_substring)[1]

    return username


def extract_password(password_line, password_substring):
    password = ''
    if password_line:
        password = password_line.split(password_substring)[1]

    return password

def get_username_and_password():
    username_line, username_substring, password_line, password_substring = get_info()
    username = extract_username(username_line, username_substring)
    password = extract_password(password_line, password_substring)
    return username, password


