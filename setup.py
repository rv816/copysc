import setuptools

setuptools.setup(
    name="copysc",
    version="0.1.5",
    url="https://github.com/rv816/pyscreen",

    author="Ryan Vass",
    author_email="rvsax16@gmail.com",

    description="Small utility that translates a shared screenshot url into a markdown-ready *.png url. Works with dropbox, screencloud, and others.",
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
