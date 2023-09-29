
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='efficientad_nelson1425',
    version='1.0.0',
    packages=find_packages(
        where="./efficientad_nelson1425",
        include=[
              "common.py",
              "pretraining.py",
              "efficientad.py",
        ],
    ),    
    python_requires=">=3.10",
    install_requires=Path("requirements/base.txt").read_text().splitlines(),
)