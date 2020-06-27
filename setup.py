import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Google-News-Query-jso8910", # Replace with your own username
    version="0.0.1",
    author="Jason R",
    author_email="mail4jasonr@gmail.com",
    description="Query Google News and get 10 results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jso8910/Google-Chats-Query",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)