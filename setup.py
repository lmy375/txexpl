from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

requires = open("requirements.txt").read().splitlines()
requires = list(filter(lambda x: not x.startswith("#"), requires))

setup(
    name="txexpl",
    description="A customized transaction decoder.",
    url="https://github.com/lmy375/txexpl",
    author="Moon",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "scripts"]),
    python_requires=">=3.8",
    install_requires=requires,
    license="AGPL-3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["txexpl = txexpl.main:main"]},
    include_package_data=True,
)
