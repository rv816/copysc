import setuptools



try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","") # Do not forget this line
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io
    # pandoc is not installed, fallback to using raw contents
    with io.open('README.rst', encoding="utf-8") as f:
        long_description = f.read()


setuptools.setup(
    name="copysc",
    version="0.2.5",
    url="https://github.com/rv816/copysc",

    author="Ryan Vass",
    author_email="rvsax16@gmail.com",

    description="Small utility that translates a shared screenshot url into a markdown-ready *.png url. Works with dropbox, screencloud, and others.",
    long_description = long_description,
    packages=setuptools.find_packages(),

    install_requires=['pyperclip', 'bs4', 'requests'],

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
