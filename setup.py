from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'ANIK GHOSH'
SRC_REPO ='src'
LIST_OF_REQIREMENT =['streamlit']

set(
    name =SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'anikghosh.2854@gmail.com',
    description = 'it is a movie recomandation system',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requirements = LIST_OF_REQIREMENT,


)