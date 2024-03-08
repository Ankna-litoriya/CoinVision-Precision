# Coin-Counter

Welcome to the Coin Counter project! This computer vision-based system is designed to analyze live video input for the detection and identification of various coins, along with their respective values. The project uses openCV, cvzone, and numpy libraries to preprocess the images for accurate analysis. Importantly, the system achieves these objectives without the use of any machine learning or deep learning algorithms.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Files:

### `main.py`

This file contains the main code for the project, focusing on live video processing. It fetches data from a specified URL (replace with your own) and applies various image processing techniques to identify and evaluate coins in the video feed. The script uses the cvzone library for contour detection and color analysis.

### `gui_main.py`

For a more interactive experience, `gui_main.py` offers a graphical user interface (GUI). Users can upload an image for analysis using the "Upload File" button. The GUI is built using the customtkinter library and incorporates the functionalities from `main.py`.


### `requirements.txt`

To ensure a smooth run of the project, make sure to install the necessary dependencies listed in this file. You can install them using the command:

```bash
pip install -r requirements.txt
```


--------------------------------------------------------------------------------------------------------------------------------------------------------------------


## How to Use:
- Ensure you have the required dependencies installed. 

- Replace the URL in main.py with IP address of the live video feed fetched from your phone camera to your system's browser on the same local network using IP Webcam (A thrid party app).

- You can also replace the url with a link to an image on the internet.

- Make sure to maintain a distance of 20 cms or around 8 inches between the camera and the coins.

- Run main.py to start the coin counting process.

- Optionally, you can use the GUI provided in gui_main.py for a more interactive experience. Run gui_main.py to launch the GUI, and use the "Upload File" button to analyze a specific image.


Credits:
This project was developed by the following contributors:

- Aayush Vishnoi
- Anirudha Upadhyay
- Aditya Kudikala
- Ankna Litoriya
