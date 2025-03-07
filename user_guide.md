# User Guide
## Description
The web application gives users an interactive version of the OSU/Corvallis Map. It features key landmarks, such as campus buildings, cultural centers, restaurants, and notable natural locations. 
## Installation
* Requires Python, FastApi Libaries, and PyMongo
* A MongoDB Database
## Deployment
1. Install Python,  FastApi, and Pymongo
2. Pull from sjoerd's branch
3. Type `python -m uvicorn app:app --reload` in terminal while in the directory of the repository
4. Go to `127.0.0.1:8000` in browser
## How To Use
* Home Page should include links to the Map, About Us, Historical Entries, and Campus Tour (WIP)
* Campus Tour should give a walkthrough of the OSU Corvallis Campus (WIP)
* Map should have a search bar with filters (WIP)
* Historical Entries should have a search bar with filters (WIP)
## Known Bugs
* Hrefs don't work
* Images don't load in
* Embed map currently doesn't do anything
## Where to Report Bugs
1. Go to the repository and go to issues tab
2. Create an issue 
3. Write a concise title that clearly states and explains the bug
4. In the description, write the steps to reproduce the bug
5. Try to figure out what causes the bug, such as any browser settings, extensions, etc.
6. Provide any screenshots or videos if it will help explain how to reproduce the bug or what the problem is