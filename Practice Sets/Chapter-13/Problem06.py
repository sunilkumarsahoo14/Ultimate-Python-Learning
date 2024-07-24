# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

"""
open terminal and run the command

> pip freeze > requirements.txt
> virtualenv sunilenv
> .\sunilenv\Scripts\activate.ps1
> pip install -r .\requirements.txt
"""