import cv2
import os

# Variables
name = input('Enter Name: ').upper()
camera = cv2.VideoCapture(0)
count = 1

# Loop till 1000 images are captured for each class
while count <= 1200:
    # Capture current frame
    rval, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    width = int(camera.get(3)+0.5)
    height = int(camera.get(4)+0.5)
    x_ = width//4
    y_ = height//7
    w_ = width//3
    h_ = width//3
    cv2.rectangle(frame, (x_-1, y_-1), (x_ + w_+1, y_ + h_+1), (0, 255, 0), 1)
    
    # Display the image
    cv2.imshow("Video", frame)
    # cv2.imshow('gray_frame', gray)
    
    key = cv2.waitKey(1)
    # exit when ESC is pressed
    if key == 27:
        break
    # Take picture when Delete button is pressed.
    if key == 13:
        # crop ROI
        crop_y = y_ + w_
        crop_x = x_ + w_
        cropped_frame = frame[y_+2:crop_y-2, x_+2: crop_x-2, :]
        
        folder = 'dataset/train/' + name
        if count >= 1000:
            folder = 'dataset/test/'
        
        if not os.path.exists(folder):
            al_umask = os.umask(0)
            os.makedirs(folder)
        result = cv2.imwrite(folder + '/' + name + str(count) + '.jpg', cropped_frame)
        count += 1
        if not result:
            print("Error saving file")
        
            

# Release the video capture object
camera.release()

# Close all active windows
cv2.destroyWindow('Video')