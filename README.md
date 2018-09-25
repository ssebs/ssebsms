# ssebsms - ssebsMS - ssebs CMS

## Requirements to run
- python3
    - markdown module from pip3



## Big picture idea / requested features
- Flat file CMS
- Use Markdown to generate pages/page sections
    - page section style support 
    - e.g. sub-theme: parallax:./img/plax1.jpg
    - e.g. sub-theme: billboard:./img/logolarge.png
    - Multiple Page Types (Home / Portfolio (Gallery) / Generic / Form / etc) 
- Enable CI to build website from source MD files (aka make a script to build files)
- ToC based on folder structure

## Help page below
```
ssebsMS.py <CMD> <site-name>

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files
    help        <- output this help page

```

## Sample file structure example below
```
.
├── bin
│   ├── _build.py
│   ├── _clean.py
│   ├── _init.py
│   └── ssebsMS.py
├── .gitignore
├── LICENSE
├── README.md
└── skel
    ├── pages
    │   ├── about
    │   │   ├── 1.md
    │   │   ├── img
    │   │   │   └── ssebsLogo.png
    │   │   ├── page.yml
    │   │   └── style
    │   │       └── __README__
    │   ├── gallery
    │   │   ├── 1.md
    │   │   ├── img
    │   │   │   └── ssebsLogo.png
    │   │   ├── page.yml
    │   │   └── style
    │   │       └── __README__
    │   └── home
    │       ├── 1.md
    │       ├── 2.md
    │       ├── img
    │       │   ├── plax.jpg
    │       │   └── ssebsLogo.png
    │       ├── page.yml
    │       └── style
    │           └── __README__
    ├── public
    │   └── .stub
    └── webparts
        ├── footer
        │   ├── footer.md
        │   ├── img
        │   │   └── ssebsLogo.png
        │   ├── part.yml
        │   └── style
        │       └── __README__
        └── header
            ├── header.md
            ├── img
            │   └── ssebsLogo.png
            ├── part.yml
            └── style
                └── __README__

```