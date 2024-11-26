# Plagiarism
This project is a CLI tool to detect plagiarism in some set of files, being capable of detecting how similar files and text are

## Description
This project is a Python-based plagiarism detection tool that compares text files within a specified directory to identify similarities. The tool uses n-grams for text comparison and calculates similarity using the Jaccard coefficient. It includes user interaction functions to specify the directory, n-gram size, and report file name, and it outputs results highlighting suspicious similarities. 

Key components:
- `main.py`: Manages user interaction and program flow.
- `interaccion_usuario.py`: Handles user inputs and displays results.
- `procesamiento.py`: Processes files, calculates n-grams, and computes similarity.
- `.gitignore`: Specifies files and directories to be ignored by Git.
