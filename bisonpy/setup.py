from setuptools import setup, find_packages

setup(
    name="bisonpy",  # Your package name
    version="0.1.1",  # Your package version
    description="JSON superset for storing numpy arrays and other objects",
    author="Paul Shen",
    author_email="pxshen@alumni.stanford.edu",
    packages=find_packages(),  # Automatically find your package(s)
    install_requires=[
        "numpy",  # Add any other dependencies your package requires
    ],
)

# cd python
# python3 -m build
# python3 -m twine upload dist/*