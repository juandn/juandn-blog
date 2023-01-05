AUTHOR = 'Juan M. Díaz Nevado'
SITENAME = 'Juan M. Diaz Nevado'
SITEURL = 'http://juandn.github.io/juandn-blog/'
#SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

MAIN_MENU = 'true'
# theme pelican-antracite
THEME = 'pelican-antracite'
SIDEBAR_DIGEST = "Sysadmin"
DISPLAY_PAGES_ON_MENU = True
PAGES = True
AVATAR = 'images/juandn.jpeg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Uniovi', 'https://www.uniovi.es/'),
         ('Asturias', 'https://www.asturias.es/'),
)

# Social widget
SOCIAL = (("github", 'https://github.com/juandn'),
          ("linkedin", 'https://es.linkedin.com/in/juan-manuel-d%C3%ADaz-nevado-b12473131'),
)

MENUITEMS = (
    ("Archives", "archives.html"),
    ("Categories", "categories.html"),
    ("Tags", "tags.html"),
)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True