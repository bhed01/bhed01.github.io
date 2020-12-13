def Head(children, title):
    return f'''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/assets/css/style.min.css" type="text/css">
            <title>{title}</title>
        </head>
        <body>
            {children}
            <script src="/assets/js/app.min.js" type="text/javascript"></script>
        </body>
    </html>'''
