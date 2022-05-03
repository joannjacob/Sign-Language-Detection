import cv2
import numpy as np
# from keras.models import load_model
# import sys
# from PIL import Image
import time


#Load the saved model
# model = load_model('model_resnet.h5')
# Start capturing Video through webcam
video = cv2.VideoCapture(0)

fps = 0
start = time.time()


while True:
    ret, frame = video.read()
    fps +=1
    
    width = int(video.get(3)+0.5)
    height = int(video.get(4)+0.5)
    x = width//4
    y = height//7
    w = width//3
    h = width//3
    cv2.rectangle(frame, (x-1, y-1), (x + w+1, y + h+1), (0, 255, 0), 1)

    # crop ROI
    crop_y = y + w
    crop_x = x + w
    cropped_frame = frame[y+2:crop_y-2, x+2: crop_x-2, :]
    
    
    img = cv2.resize(cropped_frame, (128, 128))
    # img_array = np.array(img)
    # print(img_array.shape)
    
    # img_array = np.stack((img_array,)*3, axis=-1)
    
    # img_array_ex = np.expand_dims(img_array, axis=0)
    # print(img_array_ex.shape)
    
    # prediction = model.predict(img)
    # print(prediction)
    
    cv2.putText(frame, text="HI",
                    # org=(width // 2 + 230, height // 2 + 75),
                    org=(x+5, y-7),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=3, color=(255, 255, 0),
                    thickness=5, lineType=cv2.LINE_AA)
    
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # key = cv2.waitKey(1)
    # if key == ord('q'):
    #     break
    # # if key == 27:
    #     break

# Calculate frames per second
end = time.time()
FPS = fps/(end-start)
print("[INFO] approx. FPS: {:.2f}".format(FPS))
    
video.release()
cv2.destroyAllWindows()