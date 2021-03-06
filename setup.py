import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitpy", # Replace with your own username
    version="0.0.5",
    author="Filip Troníček",
    author_email="filip@trnck.dev",
    description="A Python wrapper for git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/filiptronicek/gitpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)