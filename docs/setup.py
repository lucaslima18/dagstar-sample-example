import setuptools

setuptools.setup(
    name="docs",
    packages=setuptools.find_packages(exclude=["docs_tests"]),
    install_requires=[
        "dagster==0.15.5",
        "dagit==0.15.5",
        "pytest",
    ],
)
