from setuptools import setup

setup(
	name='favicon-generator',
	version='1.1',
	py_modules=['faviconGenerator'],
	url='https://github.com/Hecsall/favicon-generator',
	scripts=['scripts/favicon_generator.py'],
	license='MIT',
	author='Hecsall',
	author_email='',
	description='Favicon Generator',
	install_requires=['pillow', 'pilkit']
)
