import os

def find_env(env_path):
    return(os.path.isfile(env_path))

def read_env(env_path):
    env_var = {}
    with open(env_path) as fd:
        for line in fd:
            parse_line(line, env_var)
    return env_var

def parse_line(line, env_var):
    args = line.split("=")
    args[1] = treat_args(args[1])
    env_var[args[0]] = args[1]

def treat_args(arg):
    new_item = de_quote(arg)
    if type(new_item) is str:
        new_item = new_item.rstrip()
    return(new_item)

def de_quote(arg):
    sep_list = list(arg)
    if sep_list[0] == "'" or sep_list[0] == '"':
        new_string = ''.join([c for c in arg if c != '"' and c != "'"])
        return (new_string)
    return(arg)

def export_env(env_var):
    for key, value in env_var.items():
        os.environ[key] = value

def set_env(env_path):
    if find_env(env_path) == False:
        return
    env_var = read_env(env_path)
    export_env(env_var)

