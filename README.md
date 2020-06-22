# Gitpy
 A Python wrapper for git

This tool can be used for:
* Creating automatic commits in Python
* Speeding up your workflow
* Keeping everything up to date on all devices with the repo

## Setup
`pip install gitpy`

## Sample usage
```python
from gitpy import commitAdd, push

commitAdd("File updates")
push()
```