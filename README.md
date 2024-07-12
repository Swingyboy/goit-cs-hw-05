# Homework 5 for GoIT Computer Science course

The project contains the homework 5 for the GoIT Computer Science course that includes two tasks:
 - Task 1: Copy the files from one directory and sorts them by the extension in another directory.
 - Task 2: Get the URL of the page and count the frequency of words on the page.

## Requirements

- Python 3.6 or higher

## Dependencies
- `requests`
- `matplotlib`
- `aiofiles`

## Installation

1. Clone the repository:
    ```sh
    git https://github.com/Swingyboy/goit-cs-hw-05.git
    cd goit-cs-hw-05
    ```
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Task 1

```sh
python task1/main.py --source <source-path> --dest  <destination-path>
```

#### Arguments
- `--source` - the path to the source directory.
- `--dest` - the path to the destination directory.

### Task 2

```sh
python task2/main.py --url <url>
```

#### Arguments
- `--url` - the URL of the page. Default value is `https://www.gutenberg.org/files/1342/1342-0.txt`.

#### Output
The program will output the frequency of words on the page as plot.