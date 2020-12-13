import os

BUILD_DIR = os.path.join(os.getcwd(), 'build')
ASSETS_DIR = os.path.join(BUILD_DIR, 'assets')
SRC_DIR = os.path.join(os.getcwd(), 'src')
JSON_DIR = os.path.join(SRC_DIR, 'assets', 'json')


def dictToStr(ob, sep=" ", value_sep="=", value_wrapper='"'):
    return sep.join(list(map(lambda x: f'''{x}{value_sep}{value_wrapper}{ob[x]}{value_wrapper}''', ob)))


def source(data):
    return f'<source {dictToStr(data)}>'
