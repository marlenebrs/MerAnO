from setuptools import setup
import merano

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="PROJET_CPRD",
    version=merano.__version__,
    description="Merge SBML file and analyze metabolic patways.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/marlenebrs/MerAnO",
    author=[
                "Ancelle Marie",
                "Barus Marlène",
                "Borg Mathilde",
                "Mathez Céline",
             "Paardekooper Marieke",
             ],

    author_email=["celinemathez@gmail.com"],
    license="GPLv3+",
    classifiers      =[
                            'Programming Language :: Python :: 3.7',
                            'Programming Language :: Python :: 3.8',
                            'Operating System :: MacOS :: MacOS X',
                            'Operating System :: Unix',
                        ],
    packages=["merano"],
    packages_dir = {'merano' : 'merano'}
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'merano = merano.__main__:main'
        ]
    },
)

