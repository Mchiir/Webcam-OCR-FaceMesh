import cv2, mediapipe as mp, os, time, sys

IMAGES_PER_PERSON = 10
SAVE_DELAY = 450
DATASET_DIR = "dataset"
CAM_INDEX = 1 # adjust accordingly

os.makedirs(DATASET_DIR, exist_ok=True)

mp_face = mp.solutions.face_detection
detector = mp_face.FaceDetection(min_detection_confidence=0.55)

cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    sys.exit("❌ Webcam not accessible.")

print("\n------ MULTI-FACE DATASET CAPTURE ------")
print("• Press Q anytime to stop\n")

faces = {}
last = time.time()*1000
fid = 0

while True:
    ok, frame = cap.read()
    if not ok: break

    frame = cv2.flip(frame,1)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = detector.process(rgb)

    detected = []
    if result.detections:
        h,w,_ = frame.shape
        for d in result.detections:
            b = d.location_data.relative_bounding_box
            x1=int(b.xmin*w); y1=int(b.ymin*h)
            x2=x1+int(b.width*w); y2=y1+int(b.height*h)
            detected.append((x1,y1,x2,y2))

    # register new faces
    for box in detected:
        exists = any(abs(faces[i]["bbox"][0]-box[0])<60 for i in faces)
        if not exists:
            name=input("\n🆕 New face → Enter name: ").strip()
            fid+=1
            faces[fid]={"name":name,"saved":0,"bbox":box}
            os.makedirs(f"{DATASET_DIR}/{name}",exist_ok=True)
            print(f"✔ Registered: {name}")

    # capture images
    if time.time()*1000-last>=SAVE_DELAY:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        for i,f in faces.items():
            if f["saved"]>=IMAGES_PER_PERSON: continue
            x1,y1,x2,y2=f["bbox"]
            crop=gray[max(0,y1):y2,max(0,x1):x2]
            if crop.size>0:
                f["saved"]+=1
                cv2.imwrite(f"{DATASET_DIR}/{f['name']}/{f['saved']}.jpg",crop)
                print(f"[{f['name']}] {f['saved']}/{IMAGES_PER_PERSON}")
        last=time.time()*1000

    # draw
    for f in faces.values():
        x1,y1,x2,y2=f["bbox"]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame,f"{f['name']} {f['saved']}",
            (x1,y1-5),0,0.6,(255,255,255),2)

    cv2.imshow("Dataset Capture",frame)
    if cv2.waitKey(1)&0xFF==ord('q'): break

cap.release()
cv2.destroyAllWindows()

print("\nDataset ready in /dataset")
print("➡ Next: run 02_train_lbph.py")
print("Exiting cleanly...")
time.sleep(2)

SystemExit(0)