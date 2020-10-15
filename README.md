# Unique Email Finder
This is a very simple Flask web application written in Python which removes irrelevant characters like '.' and '+' from the emails given to it and returns the number of unique email addresses.
### Sample cURL Request:
```json
curl --location --request POST 'http://127.0.0.1:5000/uniqueemails' \
--header 'Content-Type: application/json' \
--data-raw '{
    "emails": [
        "dheeraj.326@gmail.com",
        "dheeraj.326+abc@gmail.com",
        "chichumail1@gmail.com"
    ]
}'
```
## How do I run this locally?
1. This application was developed using Python 3.8 and hence the same version is recommended although any version of Python 3 should work fine.
2. Go to the root path of the project
3. Run `pip install -r requirements.txt`
4. `cd src`
5. `flask run`