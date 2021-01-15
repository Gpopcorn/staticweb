import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="staticweb-Gpopcorn",
    version="1.0.1",
    author="Gpopcorn",
    description="An easy way to get started with static Python web backend.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gpopcorn/staticweb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
