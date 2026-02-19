from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="Emotion Detection using Watson NLP",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    python_requires=">=3.6",
)