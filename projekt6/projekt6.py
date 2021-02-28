#%%
from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

def detect_face(_):
  global face_cascade
  while True:
    _, frame = cap.read()
    #frame = cv2.flip(frame, 1)
    #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    face_img = frame.copy()
    face_rect = face_cascade.detectMultiScale(face_img, scaleFactor = 1.2,minNeighbors = 5) 
    for (x, y, w, h) in face_rect: 
      cv2.rectangle(face_img, (x, y),  (x + w, y + h), (0, 255, 0), 2) 
    img = Image.fromarray(face_img)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    cv2.waitKey(20)
    #lmain.after(10, detect_face)

#def run_detect_faces():
#  while True:
#    detect_face()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') 

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
root = Tk()

root.bind('<Escape>', lambda e: root.quit())

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

btn1 = Button(topFrame, text="Detect Faces",fg="red")
btn2 = Button(topFrame, text="Capture Faces",fg="red" )
btn3 = Button(topFrame, text="Detect Persons",fg="red" )
btn4 = Button(topFrame, text="Button number four",fg="red" )

btn1.pack(side=LEFT)
btn1.bind("<Button-1>",detect_face)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)

lmain = Label(bottomFrame)
lmain.pack()



#show_frame()
root.mainloop()
# %%
