def Project(project):
    return f'''
    <div class="project">
        <a class="card card--project animate" data-animation="move-up-scale" href="{project['link']}">
            <img class="card__img" src="{project['bg_url']}">
            <h2 class="heading card__heading">{project['name']}</h2>
        </a>
    </div>'''


def Projects(projects):
    return f'''
    <div class="screen__content grid grid--projects">
        {"".join(list(map(Project, projects)))}
    </div>'''
