AUTHOR = 'Juan M. Díaz Nevado'
SITENAME = 'JuanDN Blog'
SITEURL = 'https://juandn.github.io'
PATH = 'content'

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT= '%Y-%m-%d'
TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'


PAGE_URL = 'juandn-blog/pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'


MAIN_MENU = 'true'
# theme pelican-antracite
THEME = 'pelican-antracite'
SIDEBAR_DIGEST = "Sysadmin"
DISPLAY_PAGES_ON_MENU = True
PAGES = True
AVATAR = 'juandn-blog/images/juandn.jpeg'

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
    ("Archivos", "juandn-blog/archives.html"),
    ("Categorias", "juandn-blog/categories.html"),
    ("Tags", "juandn-blog/tags.html"),
)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True