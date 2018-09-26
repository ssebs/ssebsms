# ssebsms - ssebsMS - ssebs CMS

## Requirements to run
- `python3`
    - `markdown` module from pip3
    - `pyyaml` module from pip3


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
ssebsMS.sh <CMD> [site-name]

Possible CMD's:
    init        <- initialize a new ssebsMS website
    build       <- build current website
    clean       <- clean generated files (delete for now)
    help        <- output this help page

ENV file:
    ENV-ssebsMS    <- Modify this file so you don't have to
specify [site-name] in every command.

```

## Sample file structure example below
```
.
├── bin
│   ├── _build.py
│   ├── _clean.py
│   ├── _init.py
│   └── ssebsMS.py
├── LICENSE
├── README.md
├── skel
│   ├── conf.yml
│   ├── page-parts
│   │   ├── footer.md
│   │   └── header.md
│   ├── pages
│   │   ├── about
│   │   │   ├── about.md
│   │   │   ├── img
│   │   │   │   └── ssebsLogo.png
│   │   │   └── style
│   │   │       ├── __README__
│   │   │       └── style.css
│   │   └── home
│   │       ├── home.md
│   │       ├── img
│   │       │   └── ssebsLogo.png
│   │       └── style
│   │           ├── __README__
│   │           └── style.css
│   └── public
└── ssebsMS.sh

```