<h2>Update the Package</h2>
Update the package version using bumpver (in the root dir) <br/>
```bumpver update --minor```
<br/>

<h2>Build the new package</h2>
Before doing this make sure you've updated the readme with the new changes <br/>
```python -m build```

<h2>Check the new package</h2>
If the build was successful double check it by doing <br/>
```twine check dist/*```

<h2>Upload the package</h2>
No longer able to use username and password to authenticate so we need to use the api-key.
The username will always be __token__
and the password will be the API key (check docs or create one in pypi)
