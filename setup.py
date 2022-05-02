import os

import setuptools

setuptools.setup(
    name="wolfpackutil",
    version="0.1.3",
    author="Kalka",
    author_email="kalka2088@gmail.com",
    description="Python util library for WolfpackMC packages. https://github.com/WolfpackMC",
    url="https://github.com/WolfpackMC/wolfpackutil",
    project_urls={
        "Bug Tracker": "https://github.com/WolfpackMC/wolfpackutil/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "owoify-py",
        "pyfiglet",
        "python-dateutil",
        "rich"
    ]
)
