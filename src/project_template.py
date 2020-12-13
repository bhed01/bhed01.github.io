from .components.Head import Head
from .components.Footer import Footer
from .components.NavIcons import Back
from .components.Screens import HomeScreen, ProjectScreen
from .utils import JSON_DIR
from json import load
import os


def template(context):
    with open(os.path.join(JSON_DIR, 'footer_data.json')) as fFile:
        footer_data = load(fFile)

    return Head(
        title=f'Portfolio - {context["title"]}',
        children=f'''
        {Back()}
        {HomeScreen(context["title"], context["sub_title"], _type="project", bg_url=context['bg_url'])}
        {ProjectScreen(context)}
        {Footer(**footer_data)}'''
    )
