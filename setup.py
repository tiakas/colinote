from setuptools import find_packages, setup

setup(
    name="colinote",
    version="0.1",
    packages=find_packages(),
    install_requires=["click", "rich", "pytest"],
    entry_points="""
        [console_scripts]
        colinote=colinote.cli:cli
    """,
)
