from ..utils import dictToStr
from .Icons import icons


def Skill(data):
    return f'''
    <div class="card card--skill animate" data-animation="slide-in" style="{dictToStr(data['style'], ";", ":", "")}">
        <div class="card--skill__icon">
            {icons[data['icon']]}
        </div>
        <h3 class="card--skill__heading">
            {data['name']}
        </h3>
        <div class="card--skill__bar"></div>
    </div>
    '''


def Skills(data):
    return f'''
    <div class="grid grid--skills">
        <h2 class="heading grid__heading screen__heading" data-heading="02">Skill Set</h2>
        {"".join(list(map(Skill, data)))}
    </div>'''
