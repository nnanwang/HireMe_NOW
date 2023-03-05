# Hire me now!

Our platform is designed to help job seekers stand out in a competitive job market. With our comprehensive tools and resources, you can easily build a winning resume, create a customized cover letter, improve your writing skills, and even translate your resume into different languages. Plus, the more you use our platform, the more personalized and effective your results become. Say goodbye to the frustration of job hunting and hello to a brighter future with our innovative tools. We're excited to share our code with you and help make your job search easier and more successful.
  
## Key Features

1. Resume Builder: A tool that helps users create a professional and competitive resume that showcases their skills, experiences, and accomplishments.

2. Cover Letter Generator: A feature that offers a wide range of cover letter templates and guides to help users create a customized and compelling cover letter that highlights their qualifications and aligns with the job requirements.

3. Writing Expression Improvement Tools: A writing modify tools that effectively helps users enhance their documents' expression in a professional and competitive manner.

4. Resume Translation: A feature that allows users to translate their resume into different languages, which is useful for job seekers who are applying for jobs in international or multilingual environments.

5. Personalization: A feature that customizes the website's tools and resources based on the user's input and behavior. The more users interact with the website, the more personalized and effective their results become.

## About this rep

This rep is the backend for the website "hire me now". It contains skills: Conda, Django, OpenAI, Restful.

## Setup Envrionment

To totally run this code, you need: 

- Setup necessary system environment 
- Setup suitable Python version (including special packages)

---

### 1. Setup necessary system environment
 To setup enrironment for this website app, you need to perpare the following tools: `shell`, [conda/miniconda](https://docs.conda.io/en/latest/miniconda.html).  
 
 - With `shell` (which is already in your computer!), we can use conda/miniconda, install pacages, and run our website. 
 
 - With `conda/miniconda`, we would be convinent to manage our python versions. Conda is a useful tool which integrate many platform such as: Jupyter notebook, Pycharm, ect. However, I would highly recommanded you just install **miniconda**. This is because if you don't need that much platforms (At least I don't need so much), then miniconda will **save you a lot of spaces**. At the same time, it's also **effectively enough for us to manage our python environments**, which is the main target for us to use in this project. Therefore, here I just put how to install miniconda for your computer.

PS: Here I provided one method of how to use shell and miniconda. Feel free to use another shell tools or conda, they should work well.

If you are a **Windows** user:
 
  1.  Open your shell. You need to tape **'win+R'** on your keyboard, and then type **'cmd'**, so that you will get your shell.

  2. Download [miniconda - for windows](https://docs.conda.io/en/latest/miniconda.html#windows-installers). Just download the installer and click 'next' would be fine. Please check your computer to make sure it's 32 bit or 64 bit.


If you are a **Mac** user:

  1. Open your shell. You need to tape **'Command+space'** on your keyboard, and then enter **'terminal'**, so that you will get your shell.

  2. Download [miniconda - for mac](https://docs.conda.io/en/latest/miniconda.html#macos-installers). Just download the .pkg file and click 'next' would be fine.


Check if your miniconda works well in your shell:
```
(base) PS YourUserLocation> conda --version  ## Type "conda --version" in your shell.
conda 22.11.1                                ## You should get result like (Depending on the version of your conda)
```


### 2. Setup suitable Python version

The python version we used in this project is python 3.11. And all the pacages we used is in [requirements.txt](##env.yml). The followings is the details about how to setup a suitable python environment for this project.

First, open your shell (See details in [previous](#1-setup-necessary-system-environment)). Then, git clone our project to your location by:
```
git clone https://github.com/nnanwang/HireMe_NOW.git
```
Then, change your shell location to your project:
```
cd project-location
```
After that, use conda to create an environment for this project:
```
conda create -n hire_me_now python=3.11
``` 
Then, we have an environment which calls 'hire_me_now', we need to activate this environment first, and install the pacages we need:
```
conda activate hire_me_now    # you should see the env name in the brackets changed from 'base' to 'hire_me_now'
pip install -r requirements.txt    # install packages we need
```

Now you are ready to develop this project (Yeah!)

## Develop Project

When you want to develop this project, and run this project, you need to go to hmn_project ([here](#folder-stucture) is the folders structure), and then 
```
cd <hmn_project>   # go to this folder
python manage.py runserver
```
This website should be run on your computer.

Several useful files you should know for developing this project:
| File | Location | Description |
|---|---|---|
| [views.py](##hmn_project/hire_me_now/views.py) | [HireMe_NOW/hmn_project/hire_me_now](##hmn_project/hire_me_now) | |
| [urls.py (hire_me_now)](##hmn_project/hire_me_now/urls.py) | [HireMe_NOW/hmn_project/hire_me_now](##hmn_project/hire_me_now) | |
| [urls.py (hmn_project)](##hmn_project/hmn_project/urls.py) | [HireMe_NOW/hmn_project](##hmn_project/hmn_project) | |
| [settings.py](##hmn_project/hmn_project/settings.py) | [HireMe_NOW/hmn_project](##hmn_project/hmn_project) | |
| [OpenaiAPIKey.py](##hmn_project/hire_me_now/secret/OpenaiAPIKey.py)| [HireMe_NOW/hmn_project/hire_me_now/secret](##hmn_project/hire_me_now/secret) | This is the file for you to put your OpenaiAPIKey, and make sure it wouldn't leak to website(See [details](#openaiapikey)). |
| **PS: Website screens are all in templates folder** |||

## Folder Stucture

Here is a folder stucture for what you should have when you download this project.

```
HireMe_NOW/
├── README.md
├── hmn_project
│   ├── db.sqlite3
│   ├── hire_me_now
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── hmn_project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
└── requirements.txt
```

## Appendix

### OpenaiAPIKey

Not finish yet.

## Useful Links
- Figma User Work Flow Link <br>
  https://www.figma.com/file/m0DCB8iKCoI0Y13mn6RxnK/Resume-Builder-Website-User-Flow-(Community)?node-id=0%3A1&t=Boe1amln4n1tCPkD-1

- Figma Prototype *(Version 1.0)* <br>
  https://www.figma.com/file/6QiRX08X6fzdC1kalFJcYL/Prototype?node-id=0%3A1&t=5gFNtOZTmGmyKXl7-1