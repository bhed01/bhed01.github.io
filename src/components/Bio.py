def Bio(profile_pic, about):
    return f'''
    <div id="bio" class="bio">
        <div class="pic-frame animate" data-animation="slide-in">
            <img src="{profile_pic}">
        </div>
        <div class="bio__content txt--dynamic animate" data-animation="zoom-in">
            <h2 class="heading screen__heading" data-heading="01">About Me</h2>
            <p class="bio__text">
                {about}
            </p>
        </div>
    </div>'''
