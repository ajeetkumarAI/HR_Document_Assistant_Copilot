# HR Document ChatBot Assistant

## Create a virtual env and install dependency from requirements.txt

A Python virtual environment is an isolated folder structure that holds a specific Python interpreter and its own set of libraries/packages. It ensures project-specific dependencies do not interfere with other projects or the global system installation, allowing different projects to use different versions of the same library without conflicts.

Key Functions of a Virtual Environment:Isolation: 

Creates a "bubble" for each project, keeping dependencies contained and separate.Conflict Prevention: Prevents package version conflicts (e.g., Project A needing Django 3.0 while Project B needs Django 4.0).

Version Management: Allows different projects to use different versions of Python or libraries.

Cleaner System: Avoids cluttering the global Python installation with unnecessary packages.

Reproducibility: Makes it easy to share projects by creating a list of dependencies (requirements.txt) specifically for that environment.

## create a virtaul env
```bash
python -m venv venv
```

## activate virtual env
```bash
venv\Scripts\activate.bat
```

## PowerShell
```bash
\.venv\Scripts\Activate.ps1
```

## WindowsCommand Prompt.
```bash
\.venv\Scripts\activate.bat
```

## macOS/Linuxbash / zshsource 
```bash
.venv/bin/activate
```

# deactivate
```bash
venv\Scripts\deactivate.bat
```

# Install Dependency while virtual env activated
```bash
pip install -r requirements.txt
```

# Build the source code

# Build Application file

## Run application
```bash
streamlit run app.py
```

# Stop streamlit app
```bash
ctrl+c
```


# Updates gitignore file then push code to github

# track file
```bash
git add .
```

# to see tracked all files
```bash
git status
```
# commits the changes to stagging area
```bash
git commit -m "Add initial project structure and implement HR Document ChatBotCreated .gitignore to exclude environment files and cache directories. Added README.md with setup instructions and usage guidelines for the HR Document ChatBot.Implemented main application logic in app.py for document upload and question answering.Created document loaders and chunking functions to handle PDF files.
Integrated OpenAI embeddings and LLM for question answering.
Established vector store for document retrieval.
Added prompt template for structured responses.
Included sample HR policy document for testing.
Set up requirements.txt for project dependencies.
Created initial configuration files and directories."
```

# git push to remote repo

```bash
git push origin main
```