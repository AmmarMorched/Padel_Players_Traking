import cv2
import torch
import numpy as np
from Yolo import Yolo
from Minimap import Minimapa

ruta = "C:/Users/Morched/Desktop/padel/Track-Padel-Match/Minimap/padell_match.mp4"

cap = cv2.VideoCapture(ruta)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 
od = Yolo(model, cap)

im_src = cv2.imread("C:/Users/Morched/Desktop/padel/Track-Padel-Match/Minimap/stadium.png")
im_dst = cv2.imread("C:/Users/Morched/Desktop/padel/Track-Padel-Match/Minimap/std_dimention.png")

pts_src = np.array([[105, 288], [105, 129], [389, 129], [389, 293]])
pts_dst = np.array([[4, 328], [2, 70], [259, 325], [259, 71]])
minimapa = Minimapa(im_src, im_dst, pts_src , pts_dst)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", od.get_coordinates)

od = Yolo(model, cap)

while True: 

    #frame = od.frame

    od.get_attributes("person")
    od.draw_pt_medio()
    od.draw_labels()
    od.draw_bbox("person")

    #od.draw_labels()    
    #od.init_labels()

    od.generate_next_frame()
    
    for i in od.labels: 
        minimapa.representa_punto(od.labels[i]["point"], od.labels[i]["color"])
    minimapa.im_dst = cv2.imread("C:/Users/Morched/Desktop/padel/Track-Padel-Match/Minimap/std_dimention.png")
    
    key = cv2.waitKey(1)
    if key == ord("q"): 
        break
        
    if len(od.coordinates_src) == 4:
        minimapa.pts_src = np.array(od.coordinates_src)
        od.coordinates_src=[]
    
        
    cv2.imshow("frame", od.frame)
        
    if not od.is_finished():
        od.generate_next_frame()
        
cv2.destroyAllWindows()