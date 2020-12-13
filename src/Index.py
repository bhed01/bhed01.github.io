from .components.Head import Head
from .components.NavIcons import Hamburger
from .components.Screens import HomeScreen, AboutScreen, ProjectsScreen
from .components.Footer import Footer
from .utils import JSON_DIR
from json import load
import os


def Index():
    with open(os.path.join(JSON_DIR, 'home_data.json')) as hFile:
        home_data = load(hFile)
    with open(os.path.join(JSON_DIR, 'about_data.json')) as aFile:
        about_data = load(aFile)
    with open(os.path.join(JSON_DIR, 'projects_data.json')) as pFile:
        projects = load(pFile)['projects']
    with open(os.path.join(JSON_DIR, 'footer_data.json')) as fFile:
        footer_data = load(fFile)

    return Head(
        title='Portfolio - Bhed',
        children=f'''
        {Hamburger()}
        {HomeScreen(**home_data)}
        {AboutScreen(**about_data)}
        {ProjectsScreen(projects)}
        {Footer(**footer_data)}'''
    )
