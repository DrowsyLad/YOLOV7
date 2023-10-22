import cv2
import torch
import time

#model YOLOv7
MODEL_PATH = '/home/musthafa/codes/YOLOV7/Sis/best.pt'
model = torch.hub.load('.', 'custom',
                       path_or_model=MODEL_PATH,
                       source='local',
                     )
print('data loaded')
print('oke')

#camera
cam = cv2.VideoCapture('webcam-plat-kuning.mp4')
print('oke')

start = time.process_time()

while True:
    ret, frame = cam.read()
    
    curr_time = time.process_time()
    
    if curr_time-start > 5:
        print("detect")
        results = model(frame)
        img = results.imgs
        img = results.render()[0]
        start = curr_time
        results_data = results.pandas().xyxy[0]
        #print(results_data[results_data["name"]=="Black"])
        black = results_data[results_data["name"]=="Black"]
        red = results_data[results_data["name"]=="Red"]
        white = results_data[results_data["name"]=="White"]
        yellow = results_data[results_data["name"]=="Yellow"]
        is_black = bool(len(black))
        is_white = bool(len(white))
        is_red = bool(len(red)) 
        is_yellow = bool(len(yellow))
        if is_black: 
            print("Ada kendaraan pribadi")
        elif is_white:
            print("Ada kendaraan pribadi")
        elif is_yellow:
            print("Ada kendaraan angkutan umum")
        elif is_red:
            print("Ada kendaraan instansi")
        else:
            print("Tidak ada kendaraan")
        
    cv2.imshow('frame', cv2.resize(frame, (1200, 800)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break
    #time.sleep(1)  
