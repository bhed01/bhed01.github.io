from ..utils import source
from .Bio import Bio
from .Skills import Skills
from .Projects import Projects
from .Icons import IconWithLabel


def HomeScreen(title, sub_title, sub_sub_title="", _type=None, bg_url='#', video=[]):
    if _type == 'project':
        return f'''
        <div class="screen txt--dynamic">
            <img src="{bg_url}" class="screen__bg">
            <div class="screen__content screen__content--fxd move-up-scale">
                <h2 class="heading--lg txt--center">{title}</h2>
                <p class="txt--center">{sub_title}</p>
            </div>
            <a href="#about-project" class="note">Kindly scroll down</a>
        </div>'''
    else:
        return f'''
        <div id="home" class="screen txt--dynamic-lg">
            <video id="bg-video" class="screen__bg" muted loop playsinline autoplay>
                {"".join(list(map(source, video)))}
            </video>
            <div class="screen__content screen__content--fxd zoom-in">
                <h1 class="heading--lg">{title}</h1>
                <h2 class="heading--md">{sub_title}</h2>
                <p class="heading--sm">{sub_sub_title}</p>
            </div>
            <a href="#about" class="note">Kindly scroll down</a>
        </div>'''


def AboutScreen(bio, skills):
    return f'''
    <div id="about" class="screen screen--about">
        <div class="content-section">
            {Bio(**bio)}
            {Skills(skills)}
        </div>
        <a href="#projects" class="note">Kindly scroll down</a>
    </div>'''


def ProjectsScreen(projects):
    return f'''
    <div id="projects" class="screen">
        <div class="content-section">
            {Projects(projects)}
        </div>
    </div>'''


def AboutProject(text):
    return f'''<p class="animate" data-animation="slide-in">{text}</p>'''


def ProjectScreen(context):
    return f'''
    <div id="about-project" class="screen--proj-desc txt--dynamic">
        <div class="content-section">
            <div class="screen__block">
                <h1 class="heading screen__heading" data-heading="01">About Project</h1>
                <div class="screen__block">
                    {"".join(list(map(AboutProject, context['about_project'])))}
                    <video class="screen__block__video animate" data-animation="slide-in-right" src="{context["video"]}" muted loop playsinline controls></video>
                </div>
            </div>
            <div class="screen__block">
                <h1 class="heading screen__heading" data-heading="02">
                    Technologies Used
                </h1>
                <div class="flex">
                    {"".join(list(map(IconWithLabel, context["technologies"])))}
                </div>
            </div>
            <div class="screen__block">
                <h1 class="heading screen__heading" data-heading="03">
                    Resources
                </h1>
                <ul>
                    {"".join(list(map(lambda x: f'<li>{x}</li>', context["resources"])))}
                </ul>
            </div>
        </div>
    </div>'''
