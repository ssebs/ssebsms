# ssebsms - ssebsMS - ssebs CMS

> TODO: Start on this project

## Big picture idea / requested features
- Flat file CMS
- Use Markdown to generate pages/page sections
    - page section style support 
    - e.g. sub-theme: parallax:./img/plax1.jpg
    - e.g. sub-theme: billboard:./img/logolarge.png
- Multiple Page Types (Home / Portfolio (Gallery) / Generic / Form / etc)
- Enable CI to build website from source MD files (aka make a script to build files)
- ToC based on folder structure

## Sample file structure example below
- ./
    - ./pages/
        - ./pages/0_home.md
        - ./pages/1_about.md
        - ./pages/1.1_about-me.md
        - ./pages/1.2_about-ssebs.md
        - ./pages/3_gallery,md
    - ./img/
        - ./img/plax1.jpg
        - ./img/logolarge.png
    - ./style/
        - ./style/src/
            - ./style/src/site.css
        - ./style/bin/
            - ./style/bin/site.scss
    - ./bin/
        - ./bin/ssebsMS.py
        - ./bin/build-style.sh
        - ./bin/build-site-all.sh
        - ./bin/build-md.sh
