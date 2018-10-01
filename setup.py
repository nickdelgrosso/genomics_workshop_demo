from setuptools import setup

setup(
    name='genomics_demo',
    version='v0.0.1',
    packages=['genomics_demo'],
    url='',
    license='MIT',
    author='Nicholas A. Del Grosso',
    author_email='delgrosso.nick@gmail.com',
    description='The best genomics package ever.  Just kidding--do NOT use this!',
    entry_points='''
        [console_scripts]
        complement=genomics_demo.scripts:get_reverse_complement
    ''',
)
