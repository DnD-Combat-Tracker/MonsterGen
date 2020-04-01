from setuptools import setup


with open("README.md", "r") as file:
    long_description = file.read()

dev_status = {
    "Alpha": "Development Status :: 3 - Alpha",
    "Beta": "Development Status :: 4 - Beta",
    "Pro": "Development Status :: 5 - Production/Stable",
    "Mature": "Development Status :: 6 - Mature",
}

setup(
    name="MonsterGen",
    author="Robert Sharp",
    packages=['MonsterGen'],
    author_email="webmaster@sharpdesigndigital.com",
    version="0.0.1",
    description="Random Monster Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        dev_status["Alpha"],
        "Programming Language :: Python :: 3.8",
    ],
    keywords=[
        "Monster", "D&D",
    ],
    python_requires='>=3.6',
)
