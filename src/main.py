from distutils.dir_util import copy_tree
from json import load
from re import sub
import os

from .Index import Index
from .utils import BUILD_DIR, ASSETS_DIR, SRC_DIR, JSON_DIR
from .project_template import template


def handle_dir(DIRS):
    """Makes shure that all directories inside DIRS exist.

    Parameters
    ----------
    DIRS: list
        list of string denoting directory names.
    """

    for DIR in DIRS:
        if not os.path.isdir(DIR):
            os.mkdir(DIR)


def minify(html):
    """Removes the extra white spaces from string.

    Parameters
    ----------
    html: string

    Returns
    -------
    string
        modified string.
    """

    return sub(r'> <', '><', sub(r"(\n|\r|\t| )+", " ", html))


def create_index(dir_name, html):
    """Creates a index.html file.

    Parameters
    ----------
    dir_name: string
        full path of the directory where file will be created.

    html: string
        content of the HTML file to be created.
    """

    with open(os.path.join(dir_name, 'index.html'), 'w') as f:
        f.write(minify(html))


def generate_files():
    """Copies and Creates all the required files in build directory."""

    handle_dir([BUILD_DIR, ASSETS_DIR])
    create_index(BUILD_DIR, Index())

    with open(os.path.join(JSON_DIR, 'projects_data.json')) as fData:
        projects = load(fData)['details']

    projectDir = os.path.join(BUILD_DIR, 'project')
    handle_dir([projectDir])

    for project in projects:
        dirName = os.path.join(
            projectDir, project['title'].lower().replace(' ', '-'))
        handle_dir([dirName])
        create_index(dirName, template(project))

    copy_tree(os.path.join(SRC_DIR, 'assets', 'images'),
              os.path.join(ASSETS_DIR, 'images'))
    copy_tree(os.path.join(SRC_DIR, 'assets', 'videos'),
              os.path.join(ASSETS_DIR, 'videos'))

    print("Generated new files.\n")
