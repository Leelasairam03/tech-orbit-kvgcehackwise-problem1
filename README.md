# KVGCE Hackwise - Problem 1: Satellite Image Brightness Normalizer

## Team Information
- **Team Name**: TECH ORBIT
- **Team members**:
  1. PANCHAKARLA LEELA SAI RAM
  2. MANASWI KOCHI
  3. KUSHI K.T
  4. CHENDANA P


## Problem Statement
The task is to develop a Python program that normalizes the brightness of a set of grayscale satellite images. The program adjusts the brightness such that the global average intensity of all images becomes uniform.

## Instructions to Run the Code
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-team/kvgcehackwise-problem1.git
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the program using:
   ```bash
   python main.py
## Dependencies
Pillow (for image handling)

NumPy (for numerical operations)

Tkinter (for GUI)


### **Directory Structure**

Now, when users download/clone this repository, they will find the `sample_input` folder with the images inside. Your repository will look like this:

    tech-orbit-kvgcehackwise-problem1/
     ├── main.py                  # The main Python script containing the GUI and logic
     ├── requirements.txt         # List of dependencies
     ├── README.md                # Instructions and details about the project
     ├── docs/                    # Folder containing the project documentation
     │   └── documentation.pdf    # Documentation file with project details
     ├── expected_output/         # Folder containing the expected output images
     │   ├── normalized_image1.png
     │   ├── normalized_image2.png
     │   └── ...
     ├── sample_input/            # Folder containing the sample input images (image1.png to image10.png)
     │   ├── image1.png
     │   ├── image2.png
     │   └── ...
     
## sample Input
- sample_input/: A folder containing 10 grayscale PNG images named image1.png to image10.png. This folder will be included in the repository for you to use directly.

## Expected Output
The program will generate normalized images as normalized_image1.png to normalized_image10.png in the output directory. Each image will have its brightness adjusted such that its average intensity is within ±1 of the computed global average.

## The GUI interface supports the following workflow:

1. Users select the folder containing the input images (sample_input).

2. They choose or create a folder where the output should be stored (sample_output).

3. On clicking "Normalize Images", the process begins and displays the computed global average and scaling factors.
