# Deployment and Setup
## REQUIREMENTS
- [Python](https://www.python.org/downloads/)
- Python libraries:
    - fastapi
    - uvicorn
    - pymongo
    - jinja2
    - python-multipart  
To install python libraries type in the command `pip install <library_name>` in a terminal with Python.
## MongoDB Setup
1. Ensure that you have a MongoDB Project setup.
2. Go to Clusters in the Overview page of the Project and click Connect.
3. Copy the connection string and paste it into MONGO_URI in app.py.
4. Go to the MongoDB Project and go to Network Access under Security. Ensure that your IPv4 has access, otherwise the website won't work.
## Deploying the Web Application
1. Open a terminal in the directory of the repository.
2. Run in the command `python -m uvicorn app:app --reload`
3. To see the website, go to `127.0.0.1:8000` on your web browser.
