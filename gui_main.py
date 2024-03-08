from tkinter import filedialog
from tkinter.filedialog import askopenfile
import customtkinter
import os
from PIL import Image, ImageTk
import cv2
import cvzone
import requests
import numpy as np
import imutils
from cvzone.ColorModule import ColorFinder

# global variables
totalMoney = 0

myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 0, 'smin': 47, 'vmin': 49, 'hmax': 32, 'smax': 209, 'vmax': 255}

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CV Project")
        self.geometry("800x500")
        customtkinter.set_appearance_mode("Dark")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # Create fonts.
        project_font_bold = customtkinter.CTkFont(size=14, weight = "bold")
        project_font =  customtkinter.CTkFont(size = 14)
        project_font_bold_big = customtkinter.CTkFont(size = 15, weight = "bold")
        project_font_big = customtkinter.CTkFont(size = 15)
        project_font_heading = customtkinter.CTkFont(size = 18, weight = "bold")

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Coin Counter", compound="left", 
                font = project_font_heading)
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", 
                font = project_font, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                text="Project Description", font = project_font, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Credits", 
                font = project_font, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
                anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"], 
                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # create home frame.
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text = "\n\nUpload the coin image here.\n", font = project_font)
        self.home_frame_large_image_label.grid(row = 0, column = 0, padx = 20, pady = 0)
        self.home_frame_large_image_label2 = customtkinter.CTkLabel(self.home_frame, text = "(press ESC to exit the program)\n\n")
        self.home_frame_large_image_label2.grid(row = 1, column = 0, padx = 0, pady = 0)

        # create button on the home frame.
        # This will use the upload_file() method to accept images.
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Upload File", corner_radius = 32, hover_color = "#00cc00", 
                font = project_font_bold, command = lambda:self.upload_file())
        self.home_frame_button_1.grid(row = 2, column = 0, padx = 20, pady = 0)


        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        description_str = '''
        The Coin Counter project is a computer vision-powered system designed to 
        analyse live video input for the detection and identification of various coins, 
        along with their respective values. The project utilizes functions from openCV, 
        cvzone, and numpy libraries to preprocess the images for accurate analysis. 
        Notably, functions such as GaussianBlur, Canny, Dilate, morphologyEx, 
        and resize are employed to process the images effectively. It's important to 
        highlight that the system achieves these objectives without the use of any 
        machine learning or deep learning algorithms.\n'''

        self.description_label = customtkinter.CTkLabel(self.second_frame, text = description_str, width = 300,
                height = 300, font = project_font_big)
        # This keeps the label centered
        self.description_label.place(relx=0.5, rely=0.4, anchor='c')


        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        credit_str = '''Credits:\n\n Anirudha Upadhyay\n Aditya Kudikala\n Aayush Vishnoi\n Ankna Litoriya\n'''

        self.credit_label = customtkinter.CTkLabel(self.third_frame, text = credit_str, font = project_font_big)
        self.credit_label.place(relx=0.5, rely=0.3, anchor='c')


        # select default frame
        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()


    def upload_file(self):
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        self.countMoney(filename)


    def home_button_event(self):
        self.select_frame_by_name("home")


    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")


    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def preProcessing(self, img):
        imgPre = cv2.addWeighted(img, 1.2, np.zeros(img.shape, img.dtype), 0, 45)
        imgPre = cv2.GaussianBlur(imgPre, (5,5), 5)
        # threshold1 = cv2.getTrackbarPos("Threshold1", "Settings")
        # threshold2 = cv2.getTrackbarPos("Threshold2", "Settings")
        imgPre = cv2.Canny(imgPre, 60,130)
        kernel = np.ones((4,4), np.uint8)
        imgPre = cv2.dilate(imgPre, kernel, iterations=1)
        imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
        return imgPre


    def countMoney(self, filename):
        while True:
            photo = Image.open(filename)
            import io
            with io.BytesIO() as output:
                photo.save(output, format="JPEG")  # Preserve original format
                photo_bytes = output.getvalue()
            img_arr = np.array(bytearray(photo_bytes), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=800, height=600)
            imgPre = self.preProcessing(img)
            imgContours, conFound = cvzone.findContours(img, imgPre, minArea=20)
            totalMoney = 0
            if conFound:
                for contour in conFound:
                    peri = cv2.arcLength(contour['cnt'], True)
                    approx = cv2.approxPolyDP(contour['cnt'], 0.02*peri, True)

                    if len(approx) > 6:
                        area = contour['area']

                        # print(area)
                        x,y,w,h = contour['bbox']
                        imgCrop = img[y:y+h, x:x+w]
                        # cv2.imshow(str(count), imgCrop)
                        imgColor, mask = myColorFinder.update(imgCrop, hsvVals)
                        whitePixelCount = cv2.countNonZero(mask)
                        # print(whitePixelCount)

                        if 8000 < area < 12000 and whitePixelCount > 500:
                            totalMoney += 5
                        elif area < 10600:
                            totalMoney += 1
                        elif 10600 < area < 12000:
                            totalMoney += 2
                        elif area > 12000:
                            totalMoney += 10
                    # print(totalMoney)

            # stackedImage = cvzone.stackImages([img, imgPre, imgContours],2,0.5)
            cvzone.putTextRect(imgContours, f'Rs. {totalMoney}', (50,50))
            cv2.imshow("Image", imgContours)
            # cv2.imshow("ImageColor", imgColor)
            while True:
                k = cv2.waitKey(0) & 0xFF
                if k == 27:
                    print("Shutting Down Window...")
                    cv2.destroyAllWindows()
                    print("Window Shutdown.")
                    return
                else:
                    print(str(k) + ": Press ESC to exit.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
