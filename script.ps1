
# Create directories
New-Item -Path .vscode -ItemType Directory
New-Item -Path .github\workflows -ItemType Directory
New-Item -Path src -ItemType Directory
New-Item -Path notebooks -ItemType Directory
New-Item -Path tests -ItemType Directory
New-Item -Path scripts -ItemType Directory

# Create empty files
New-Item -Path .vscode\settings.json -ItemType File
New-Item -Path .github\workflows\unittests.yml -ItemType File
New-Item -Path .gitignore -ItemType File
New-Item -Path requirements.txt -ItemType File
New-Item -Path README.md -ItemType File
New-Item -Path notebooks\README.md -ItemType File
New-Item -Path notebooks\__init__.py -ItemType File
New-Item -Path src\__init__.py -ItemType File
New-Item -Path tests\__init__.py -ItemType File
New-Item -Path scripts\__init__.py -ItemType File
New-Item -Path scripts\README.md -ItemType File


# Open project in VS Code
code .