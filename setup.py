from setuptools import find_packages, setup

setup(
    name="fetch_abi_csv_project",
    packages=find_packages(exclude=["fetch_abi_csv_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
