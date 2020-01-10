from setuptools import setup, find_packages

setup(
    name="TurboKid",
    version="1.0.4",
    description="TurboGears plugin to support use of Kid templates",
    author="Kevin Dangoor et al",
    author_email="dangoor+turbogears@gmail.com",
    url="http://www.turbogears.org",
    download_url="http://www.turbogears.org/download/",
    keywords=["python.templating.engines", "turbogears"],
    license="MIT",
    install_requires = ["kid >= 0.9.6"],
    zip_safe=False,
    packages=find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: TurboGears',
        'Environment :: Web Environment :: Buffet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points="""
    [python.templating.engines]
    kid = turbokid.kidsupport:KidSupport
    """,
    test_suite = 'nose.collector',
    )

