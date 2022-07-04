from setuptools import setup, find_packages

setup(
    name="script-package",
    version="0.1.dev0",
    url="",
    author="James Derrick",
    author_email="jgd10.github@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    license_file="LICENSE",
    description="Package to be run as a cli",
    long_description=open("README.rst").read(),
    install_requires=["importlib-metadata >=4.0"],
    python_requires=">=3.7",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
