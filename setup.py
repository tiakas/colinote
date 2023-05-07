from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="colinote",
    version="0.1.0",
    author="Giannis Tiakas",
    author_email="giannis@tiakas.com",
    description="A CLI note-taking application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiakas/colinote",
    packages=find_packages(),
    entry_points={"console_scripts": ["colinote=colinote.cli:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="cli, note-taking",
    install_requires=["click==8.0.1", "rich==10.9.0", "pyyaml==5.4.1"],
    python_requires=">=3.6",
)
