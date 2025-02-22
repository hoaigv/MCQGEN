from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',    
    author='hoai',
    author_email='hmhoai.20it11@vku.udn.vn',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)
