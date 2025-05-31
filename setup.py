from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read() # useful when we have to publish as our project as a PyPi package

## edit below variables as per your requirements -
REPO_NAME = "Book_Recommender_System"
AUTHOR_USER_NAME = "SreeDharsiniDevaraj"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

setup(
    name = SRC_REPO,
    version = "0.0.1",
    author = "Sree Dharsini Devaraj",
    description="A small local package for Machine Learning-based books recommendations",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url ="https://github.com/SreeDharsiniDevaraj/Book_Recommender_System",
    author_email="sreedharsinid@gmail.com",
    packages = find_packages(),
    license = "MIT",
    python_requires = ">=3.7",
    install_requires = LIST_OF_REQUIREMENTS
)