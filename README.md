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

Each page's config / content is in the same file. ssebsMS looks for a specified `.mdx` file

#### mdx syntax below

```
!~title=<PAGE_TITLE>
!~url=<URL.html>
!~author=<YOUR NAME>

~start-section=<SECTION_NAME>  # COMMENT
~sec-theme=<THEME OF SECTION>  # COMMENT
~sec-option=<sec-theme OPTION> # COMMENT

<YOUR MARKDOWN HERE>

~end-section=<SECTION_NAME>

<OPTIONAL SECTION2 USING SAME SYNTAX ABOVE>
```

#### Themes and options listed below
- sec-theme's:
    - color       \<- color bg
    - billboard   \<- picture bg
    - parallax    \<- parallax'd image bg
    - blank       \<- blank bg
- sec-option's:
    - \<color\>     \<- color for (color) theme
    - \<img-name\>  \<- image for (billboard|parallax) themes 

## Sample file structure example below
```
.
├── bin
│   ├── _build.py
│   ├── _clean.py
│   ├── _init.py
│   ├── _page.py
│   └── ssebsMS.py
├── ENV-ssebsMS
├── LICENSE
├── README.md
├── skel
│   ├── conf.yml
│   ├── page-parts
│   │   ├── footer.md
│   │   ├── header.md
│   │   └── img
│   │       └── ssebsLogo.png
│   ├── pages
│   │   ├── about
│   │   │   ├── about.mdx
│   │   │   ├── img
│   │   │   │   ├── code.jpg
│   │   │   │   └── ssebsLogo.png
│   │   │   └── style
│   │   │       ├── __README__
│   │   │       └── style.css
│   │   └── home
│   │       ├── home.mdx
│   │       ├── img
│   │       │   ├── code.jpg
│   │       │   └── ssebsLogo.png
│   │       └── style
│   │           ├── __README__
│   │           └── style.css
│   ├── public
│   └── themes
│       ├── billboard.txt
│       ├── blank.txt
│       ├── color.txt
│       └── parallax.txt
└── ssebsMS.sh


```