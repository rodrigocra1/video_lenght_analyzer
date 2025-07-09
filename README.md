# Video Length Analyzer

A simple Python script to scan a directory and its subdirectories for video files, calculate their duration, and provide a summary based on their length.

---

### Author's Note

> This is an app to analyze video files length from a folder. It was created for my personal use, that's why the code is mostly AI made. I was in a hurry. New updates will be made anyway.

---

## Overview

This tool provides a straightforward way to quickly get an inventory of video files within a folder structure. It identifies common video formats, extracts the duration of each file, and prints a report to the console. At the end of the analysis, it displays a summary dialog box categorizing files as being longer or shorter than 90 seconds.

## Features

-   Scans a selected directory and all its subfolders recursively.
-   Identifies video files by common extensions (`.mp4`, `.mkv`, `.avi`, `.mov`, etc.).
-   Calculates and displays the duration of each video in `HH:MM:SS` format.
-   Handles potential errors with corrupted or unreadable files gracefully.
-   Provides a final summary of how many videos are longer than 1 minute and 30 seconds and how many are shorter.
-   Uses a graphical user interface (GUI) to select the target folder.

## Requirements

-   Python 3.x
-   `moviepy` library

## Installation

1.  **Clone or download the repository.**
    Save the `video_lenght_analizer.py` file to your local machine.

2.  **Install the required dependency.**
    Open your terminal or command prompt and run the following command to install `moviepy`:
    ```bash
    pip install moviepy
    ```
    If you are using an IDE like PyCharm, it is recommended to use its built-in terminal or package manager to install the library into the project's specific virtual environment.

## Usage

1.  **Run the script from your terminal:**
    ```bash
    python video_lenght_analizer.py
    ```

2.  **Select a folder.**
    A file dialog window will open. Navigate to and select the root folder you wish to analyze.

3.  **View the results.**
    The script will start processing and print the path and duration of each video file found directly into the terminal.

4.  **Check the summary.**
    Once the analysis is complete, a message box will pop up with a summary of the results.

