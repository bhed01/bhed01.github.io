def Footer(title, sub_title, github_link, linkedin_link, email):
    return f'''
    <footer id="contact" class="footer">
        <div class="content-section">
            <h3 class="heading footer__heading">{title}</h3>
            <p class="footer__text">{sub_title}</p>
            <div id="get-in-touch" style="height: 6rem;">
                <h4 class="heading footer__heading--sm">Get in touch</h4>
                <div class="social-actions">
                    <a href="{github_link}" class="social-links icon">
                        <svg stroke="currentColor" fill="currentColor" xmlns='http://www.w3.org/2000/svg'
                            width='1em' height='1em' viewBox='0 0 35.318 35.318'>
                            <path
                                d='M23.71,34.689c-0.172,0.062-0.345,0.137-0.522,0.168c-0.678,0.121-1.112-0.229-1.116-0.922 c-0.009-1.287-0.009-2.572,0.012-3.859c0.022-1.48-0.012-2.941-1.139-4.162c0.67-0.12,1.266-0.204,1.849-0.338 c3.862-0.887,5.868-3.323,6.124-7.366c0.131-2.058-0.236-3.946-1.604-5.567c-0.099-0.114-0.104-0.373-0.057-0.539 c0.364-1.34,0.258-2.649-0.166-3.959c-0.105-0.327-0.279-0.428-0.602-0.407c-1.134,0.063-2.173,0.461-3.089,1.073 c-0.883,0.593-1.705,0.722-2.754,0.482c-2.31-0.521-4.635-0.369-6.94,0.165c-0.261,0.062-0.612-0.021-0.851-0.161 c-1.082-0.634-2.164-1.25-3.412-1.496c-0.965-0.188-1.049-0.14-1.305,0.793C7.816,9.77,7.784,10.947,8.113,12.13 c0.047,0.172-0.002,0.448-0.117,0.575c-2.557,2.853-1.631,8.244,0.092,10.309c1.34,1.604,3.12,2.326,5.096,2.701 c0.345,0.064,0.688,0.113,1.033,0.173c-0.296,0.77-0.562,1.497-0.863,2.212c-0.059,0.138-0.246,0.254-0.399,0.312 c-1.938,0.752-3.604,0.199-4.713-1.56c-0.593-0.938-1.354-1.639-2.488-1.842c-0.036-0.007-0.073-0.026-0.106-0.021 c-0.305,0.08-0.607,0.164-0.911,0.246c0.171,0.238,0.292,0.558,0.521,0.701c0.961,0.608,1.586,1.475,1.999,2.498 c0.649,1.604,1.909,2.319,3.546,2.459c0.799,0.065,1.606,0.01,2.481,0.01c0,0.996,0.036,2.133-0.015,3.265 c-0.026,0.61-0.639,0.854-1.373,0.604c-1.947-0.666-3.752-1.621-5.311-2.963C0.956,26.96-1.214,20.83,0.657,13.655 C2.522,6.503,7.383,2.116,14.651,0.739C24.708-1.163,34.235,6.161,35.233,16.37C36.021,24.418,31.284,31.949,23.71,34.689z M14.229,25.85c-0.006,0.014-0.01,0.024-0.016,0.038c0.018,0.003,0.036,0.006,0.055,0.009 C14.282,25.898,14.294,25.923,14.229,25.85z M9.679,29.031c0.157,0.097,0.307,0.22,0.477,0.273c0.062,0.02,0.177-0.121,0.38-0.271 c-0.282-0.107-0.448-0.201-0.623-0.225C9.845,28.8,9.757,28.953,9.679,29.031z M11.112,29.277c0.023,0.105,0.232,0.236,0.355,0.234 c0.119-0.002,0.235-0.16,0.354-0.25c-0.108-0.099-0.216-0.195-0.548-0.494C11.201,28.975,11.082,29.143,11.112,29.277z M12.87,28.854c-0.148,0.035-0.273,0.172-0.408,0.266c0.079,0.1,0.158,0.193,0.285,0.35c0.175-0.16,0.294-0.271,0.414-0.379 C13.061,29.004,12.944,28.836,12.87,28.854z M8.512,28.261c0.082,0.155,0.209,0.289,0.381,0.508 c0.115-0.188,0.24-0.332,0.218-0.361c-0.109-0.143-0.257-0.26-0.403-0.367C8.698,28.033,8.495,28.227,8.512,28.261z' />
                        </svg>
                    </a>
                    <a href="{linkedin_link}" class="social-links icon">
                        <svg stroke="currentColor" fill="currentColor" xmlns='http://www.w3.org/2000/svg'
                            width='1em' height='1em' viewBox='0 0 510 510'>
                            <path
                                d='M459,0H51C22.95,0,0,22.95,0,51v408c0,28.05,22.95,51,51,51h408c28.05,0,51-22.95,51-51V51C510,22.95,487.05,0,459,0z M153,433.5H76.5V204H153V433.5z M114.75,160.65c-25.5,0-45.9-20.4-45.9-45.9s20.4-45.9,45.9-45.9s45.9,20.4,45.9,45.9 S140.25,160.65,114.75,160.65z M433.5,433.5H357V298.35c0-20.399-17.85-38.25-38.25-38.25s-38.25,17.851-38.25,38.25V433.5H204 V204h76.5v30.6c12.75-20.4,40.8-35.7,63.75-35.7c48.45,0,89.25,40.8,89.25,89.25V433.5z'>
                            </path>
                        </svg>
                    </a>
                </div>
            </div>
            <div>
                <h4 class="heading footer__heading--sm">Reach me</h4> <a href="mailto:{email}" class="link--underlined">{email}</a>
            </div>
        </div>
    </footer>'''
