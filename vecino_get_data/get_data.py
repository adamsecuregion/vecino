from conf import POSSIBLE_USERNAMES, POSSIBLE_PASSWORDS, TEXTFILE_PATH
from webbrowser import open_new_tab


def get_info():
    in_file = open(TEXTFILE_PATH, "rt")
    contents = in_file.read()
    in_file.close()

    username_line = ''
    password_line = ''

    for line in contents.strip().split('\n'):
        if any(substring in line for substring in POSSIBLE_USERNAMES):
            username_line = line
        if any(substring in line for substring in POSSIBLE_PASSWORDS):
            password_line = line

    return(username_line, password_line)

def extract_info(username_line, password_line):
    username = ''
    password = ''
    if username_line:
        username = username_line.split('UserName : ')[1]
    if password_line:
        password = password_line.split('Password : ')[1]

    return username, password

def wrapStringInHTMLWindows(username, password):
    if not username:
        username = 'Sorry, no username found in file'
    if not password:
        password = 'Sorry, no password found in file'
    filename = 'vecino_output.html'
    f = open(filename,'w')
    wrapper = """<html>
    <body bgcolor="LemonChiffon">
    <head>
        <style>
            header, footer {
            padding: 1em;
            color: LemonChiffon;
            background-color: black;
            clear: left;
            text-align: center;
            }
            article {
            margin-left: 170px;
            border-left: 1px solid gray;
            padding: 1em;
            overflow: hidden;
            }
        </style>
    </head>
    <body>
        <header>
            <h2>Output from Vecino </h2>
        </header>
        <article>
            <h3>
                <font color="black">Username: %s</font>
            </h3>
            <h3>
                <font color="black">Password: %s</font>
            <h3>
        </article>
        <footer></footer>
    </body>
    </html>"""

    whole = wrapper % (username, password)
    f.write(whole)
    f.close()
    open_new_tab(filename)

def execute_vecino_process():
    username_line, password_line = get_info()
    username, password = extract_info(username_line, password_line)
    wrapStringInHTMLWindows(username, password)


if __name__ == '__main__':
    execute_vecino_process()

