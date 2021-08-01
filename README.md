<h1 align="center">Notiongram</h1>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
)](https://www.python.org/) [![profile](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/marcoscard)

Notiongram is a integration that allow your Saved Messages (like chat yourself) from Telegram become pages to Notion.

## **Easier, Simpler and Faster!**

---
The idea is that you send a message to *yourself* on Telegram and synchronize with Notion by storing it in a database as pages.

It's pretty simple, no?

> In the future, it's intended create tasks by the same messages, but with a simple notation.

## Objectives

---

- [x] Create and configuring enviroment. :computer:
- [x] Create a github repository and link it. :octocat:
- [x] Update README with info about how to contributing. :notebook:
- [x] Start code! :rocket:

## How to contributing

---

### Step 1 | Make a fork!

![fork icon location](https://user-images.githubusercontent.com/1951843/54656025-77fd0380-4a9a-11e9-82f6-35278ed9ccfc.png)

### Step 2 | Install Git and Python 3!

If you don't have Git and/or Python 3 installed yet, use this command.
 
![Linux badge](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white
)

```bash
sudo apt-get install -y git python3 python3-pip
```

![Windows badge](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white
)

Download [Python 3](https://www.python.org/downloads/windows/) and [Git](https://git-scm.com/download/win)

### Step 3 | Make a local copy!

In Windows you open a Command Prompt (or a Powershell). For Linux, open a Terminal pressing Ctrl+Alt+T.

Then run:
```bash
git clone https://github.com/your_github_username/docs
```

First time using git? Also run this:
```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Step 4 | Making things work!

In order to setup environment, follow this commands.

```
pip install virtualenv
virtualenv -p python3 venv
cd venv/
source bin/activate
pip install -r requirements.txt
```

If you did all correct, there should be some indication about the python virtual environment when `source bin/activate` was run, similarly to this:

![virtual environment](https://dkrn4sk0rn31v.cloudfront.net/2018/11/08121425/Captura-de-Tela-2018-11-08-a%CC%80s-11.11.58.png)

**Note:** The next time you just run `source bin/activate` in virtual environment's directory.

So now, you are free to editing and add features to the code!  

### Step 5 | It's time to share!

Again in the Terminal (or command prompt) and in the virtual environment's directory, type:
```bash
git commit -a -m "Some descriptions of your changes"
git push origin <branch>
```

You will be prompted for your GitHub credentials.

Go to Pull Requests and open a new pull request, fill in a description of your changes and it's done. I review your changes and if it's good enough you'll be approved!