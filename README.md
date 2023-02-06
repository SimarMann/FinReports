# FinReports
Video Demo: [Youtube](https://youtu.be/mkvdpnTWgYY)

A finance dashboard app with a user authentication system.

## Table of Contents

- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---
# Key Features
**Dashboard**:
- *Macrodash:* US yield curve chart & 1MΔ for Index Futures, Crypto, Commodities and FX 
- *Stockscreen:* search by symbol to retrieve fundamental stock data 

**User Authentication**:
- Register/Login
- Change Password
- User Sessions

**Stack**:
- Built on Flask 
- OpenBB SDK: financial data
- Plotly-Dash: dashboard logic and views 
- WTForms + Flask-WTF: form validation and rendering
- Flask-SQLAlchemy + Sqlite: for data storage and database models
- Flask-Login: provides user session management
- Flask-Session + Redis: support for server-side sessions
---
# Getting Started

## Prerequisites: 

> **Miniconda**

Virtual Python environments are containers for Python applications, and allow the operating system to remain unchanged. Since we are using the OpenBB SDK, installing it in an isolated, dedicated, virtual environment is a must.

**1. Install Miniconda**

Download the x86_64 Miniconda for your respective system and follow along with it's installation instructions.

**2. Download the obb.yml file**

The [obb.yml](https://github.com/SSM0022/FinReports/blob/main/obb.yml) is available in the repo and you must create a copy of it to install all dependencies.

**3. Create the virtual environment**
```
conda env create -f obb.yml
```


## Installation:
**1. Clone the Repo**
```
git clone https://github.com/SSM0022/FinReports.git
cd FinReports
```

**2. Download Bootstrap** 
```
Download [Bootstrap v5.2.3](https://getbootstrap.com/docs/5.2/getting-started/download/) - compiled CSS & JSS

Delete the bootstrap.min.css included in the download (we will be replacing it with our own)

Copy the CSS **files** from Bootstrap into `FinReports/FinReports/static/css`

Copy the JS **folder** from Bootstrap into `FinReports/FinReports/static/`
```

**3. Activate the conda environment**
```
conda activate obb
```

## Configuration:
In Flask we store configuration variables such as database credentials, API keys, or settings for flask and its extensions.
Before the application will function you must create the files below.

> `.env`


```
# Replace 'string' with appropriate values
FLASK_APP='wsgi.py'
SECRET_KEY='string' 
FLASK_DEBUG='True'
SQLALCHEMY_DATABASE_URI='string'
REDIS_URI='string'
```

> `config.py`
```
from os import environ, path
from dotenv import load_dotenv
import redis

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    FLASK_APP = environ.get('FLASK_APP')
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    TESTING = True
    
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Session
    REDIS_URI = environ.get("REDIS_URI")
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(REDIS_URI)
```    

> API Keys

The only API Key required to use the app is available for free from [FinancialModelingPrep](https://site.financialmodelingprep.com/developer/docs/). 

Set Key:

- For API Keys related to financial data you can store them using [OpenBB Keys Menu](https://docs.openbb.co/sdk/guides/advanced/api-keys)

**OR**

- Set it in an environment variable on the OS (Linux example):
```
echo "export API_KEY_FINANCIALMODELINGPREP='yourkey'" >> ~/.zshrc
```
```
source ~/.zshrc
```
```
echo $API_KEY_FINANCIALMODELINGPREP
```
---
# Usage

**Start Redis-Server**: 
(**Linux example**)
1.  Open a second bash terminal
2.  `conda deactivate`
3.  `cd ~`
4. `sudo service redis-server start`
5. `sudo service redis-server stop` (good practice to turn off the redis-server when finished serving the app locally)

**Run the Flask App** 

In the first bash terminal which should be in /FinReports and have the conda environment active

`flask run`

**Register/Login** 

After you register an account using a username, email and password you will be able to login and access the stockscreen, macrodash views as well as a user profile page where you can change your password.

---
# Contributing

Currently not accepting contributions as this is a personal project, but feel free to clone and work on your own version. 

---
# License

FinReports is licensed under the **MIT License** for more information refer to [LICENSE.MD](https://github.com/SSM0022/FinReports/blob/main/LICENSE.MD)
