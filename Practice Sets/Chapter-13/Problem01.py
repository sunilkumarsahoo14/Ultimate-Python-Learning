# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

"""
> virtualenv env1
> virtualenv env2

---> work on env1

> .\env1\Scripts\activate.ps1
> pip install pandas
> pip install pyjokes
> pip freeze > requirements.txt
> deactivate

---> work on env2

> .\env1\Scripts\activate.ps1
> pip install -r .\requirements.txt

"""