from setuptools import setup

setup(
    name='recipebuddy_frontend',
    version='0.1.0',    
    description='A webapp to suggest recipes based on a variety of input choices. Frontend using Streamlit and Backend using FastAPI ',
    url='https://github.com/SambhaviPD/RecipeBuddy',
    author='Sambhavi Dhanabalan',
    author_email='sambhavi@golittlebig.com',
    license='MIT',
    packages=['src.recipebuddy_frontend'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Work in Progress',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)