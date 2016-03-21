import setuptools

setuptools.setup(
    name="pyscreen",
    version="0.1.0",
    url="https://github.com/rv816/pyscreen",

    author="Ryan Vass",
    author_email="rvsax16@gmail.com",

    description="Small utility that translates a screencloud url into a png url",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['pyperclip', 'mechanicalsoup'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
