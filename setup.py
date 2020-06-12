import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LCD-breakpoints-detection", # Replace with your own username
    packages=['lcdbp'],
    package_dir={'lcdbp':'lcdbp/src'},
    install_requires=['numpy'],
    version="0.1.4",
    author="Etienne Kronert",
    author_email="etienne.kronert@lilo.org",
    description="Breakpoint Detection with LASSO and Coordinate Descent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kronerte/LCD_breakpoints_detection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)