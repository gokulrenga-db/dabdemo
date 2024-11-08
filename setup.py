# Filename: setup.py
from setuptools import setup, find_packages
import sys
sys.path.append('./src')

import dabdemo

setup(
  name = "dabdemo",
  version = dabdemo.__version__,
  author_email = "gokul.renganathan@databricks.com",
  description = "cicd test",
  packages = find_packages(where='./src'),
  package_dir={'': 'src'},
  entry_points={
        "packages": [
            "main=dabdemo.main:main"
        ]
    },
  install_requires = ["setuptools"]
)
