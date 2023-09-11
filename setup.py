from setuptools import setup

setup(
	name='favicon-gererator',
	version='1.0',
	py_modules=['faviconGenerator'],
	url='https://github.com/Hecsall/favicon-generator',
	scripts=['scripts/favicon_generator.py'],
	license='MIT',
	author='Hecsall',
	author_email='',
	description='Favicon Generator',
	install_requires=['pillow', 'pilkit']
)