import cv2
import  mediapipe as mp
import glob
import csv
import time
import exclepy as e
handlist=[]
h=[]
#column=["x0","y0","x1","y1","x2","y2","x3","y3","x4","y4","x5","y5","x6","y6","x7","y7","x8","y8","x9","y9","x10","y10","x11","y11","x12","y12","x13","y13","x14","y14","x15","y15","x16","y16","x17","y17","x18","y18","x19","y19","x20","y20"]
#cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils




path = glob.glob("E:\Python\HandTracking\Data\*.png")

for file in path:
    img = cv2.imread(file)
    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            hand=[]
            for id, lm in enumerate(handLms.landmark):
                #print(id)
                #print(lm)

                handlist.append(lm)
                #h=handlist.split()
                # i=handlist.index("\n")
                # temp,temp1=handlist[:i],handlist[i+1:]
                # i1=temp1.index("\n")
                # temp1,temp2=temp1[:i1],temp1[i1+1:]
                # print(temp,temp1,temp2)

                #print(handlist)
                #hand=handlist.splitlines(




            h.extend([handlist])
            #print(type(h[0]))
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    # name of csv file
    # name of csv file
    # filename = "demodata.csv"
    temp=open("demo.txt","w")
    for  i in h:
        temp.write(str(h))
    temp.close()


    # # writing to csv file
    # with open(filename, 'w') as csvfile:
    #     # creating a csv writer object
    #     csvwriter = csv.writer(csvfile)
    #
    #     # writing the fields
    #     csvwriter.writerow(column)
    #
    #     # writing the data rows
    #     csvwriter.writerows(h)
    print(h)
    print(type(h))
    cv2.imshow("Image",img)
    e.something()
    cv2.waitKey(0)
