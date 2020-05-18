import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="milky",
    version="0.1",
    author="matabares",
    author_email="matabares@gmail.com",
    description="Python client for Remember The Milk.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matabares/milky",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
