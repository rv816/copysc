rm -rf build dist copysc.egg-info
python setup.py sdist bdist_wheel
twine upload dist/* 
python setup.py register
