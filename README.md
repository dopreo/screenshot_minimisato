# screenshot_minimisato
a simple script that will:

---
- **1**. take your screenshots directory (as specified in the main.py)
- **2**. scour it for screenshots with names that don't end in `.webp`
- **3**. collect a list of screenshots that don't end in `.webp`
- **4**. convert a screenshot to the more efficient [webp image format](https://developers.google.com/speed/webp)
- **5**. move the old, less efficient copy into a directory called `old` within the same directory
- **6**. repeat steps **4** and **5** for each screenshot collected in the list
---
one may then discard of the `old` folder to enjoy the space savings as provided by the encoding of your screenshots in the more efficient [webp image format](https://developers.google.com/speed/webp).

### lossy mode
those who know what they are doing can optionally call the `convert_to_webp()` function with a **quality below 100** (but still above 0) to activate **lossy mode**.
this allows a user to enjoy further space savings on their disk at the sacrifice of quality, as this results in the loss of data in the new webp-encoded images.

**lossy mode is, importantly, disabled by default**. running this script unmodified will result in the creation of **perfect, lossless webps**, as not to lose information.

# installation

### 1. grab the project

#### **- a**. clone the repo
download its contents onto your local machine.

#### **- b**. open up a terminal inside it
open a terminal inside this `screenshot_minimisato` folder you just downloaded.

#### **- c**. ensure the presence of python where you are
- like this:
```
python3 --version
```
## 2. prepare a venv

#### **- a**. staying in this project's folder, make a new **venv** for this project
this **avoids conflicts** with other packages and applications on your system.

a python venv is kind of like a **separate place** where we install the packages for this project to work, all tucked away neatly, so we don't mess with anything else in doing so!
- to **make a new venv**, run:
```
python3 -m venv .venv
```

#### **- b**. '**activate**' your venv (this basically means just start using it)

this means your commands in this terminal session will take place **from this new venv** until you `deactivate` the venv.

- this is accomplished on **macOS** or **Linux** like so:
```
source .venv/bin/activate
```
- in **Windows Command Prompt** like this:
```
.venv\Scripts\activate.bat
```
- and in **Windows PowerShell** like this:
```
.venv\Scripts\Activate.ps1
```

## 3. grab dependencies

#### **- a**. **upgrade** your pip installation
this also lets us check it's present and working.
```
python -m pip install --upgrade pip
```

#### **- b**. show pip our **requirements.txt** file
this repo has a `requirements.txt` file inside. show it to pip, and it'll fetch everything you need for you.
- run this command to show pip our `requirements.txt`:
```
pip install -r requirements.txt
```

## 4. go for it, jimmy

#### **- a**. run the script
- to set sail, run, in the same directory:
```
python3 main.py
```

# contributing
this code probably sucks. if you have any better ideas on how to do anything, feel free to show me! i'm very much still learning.

you probably know the drill. in case you don't:
- fork the repo
- make your changes on your fork
- open up a pull request, asking us to pull your changes into our repo
- we'll review your request, thank you so much!!! :D

# licensing and terms of use
this is an oreohive project, and all of its materials, code and all else in this repo are oreohive works.

this means it is protected by the [oreohive terms & ethics of use](https://www.oreohive.org/onboarding). this, mainly, prohibits the use of anything inside this repo for the training, improvement, diagnostics, iterations or developments of ai models or machine learning models or applications, including generative ai and / or llm chatbots and similar applications that rely on mahcine learning techniques.

putting aside the restrictions of the oreohive terms & ethics of use, this repo's code is licensed and distributed by the oreohive organisation under the **GNU AGPL-3.0** license. all non-code elements or files (like this `README.md` and any `.txt` files) are instead licensed under **CC BY-NC-SA 4.0**.

we thank you in advance for respecting our wishes! :))
