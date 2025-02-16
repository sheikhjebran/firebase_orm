from setuptools import setup, find_packages

setup(
    name="firebase_orm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "firebase-admin",
        "django"
    ],
    author="Sheikh Jebran",
    author_email="sheikhjebran@gmail.com",
    description="A Firebase ORM for Django",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/firebase_orm",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
