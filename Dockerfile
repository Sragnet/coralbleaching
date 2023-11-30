FROM deepnote/python:3.7

RUN apt update && apt install -y pandoc texlive-xetex
