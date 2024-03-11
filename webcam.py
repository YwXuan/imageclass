import cv2

# 選擇第1隻攝影機
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('https://trafficvideo.tainan.gov.tw/beabed1d ')

while cap.isOpened():#鏡頭能開啟嗎？
  
  # 從攝影機擷取一張影像
  ret, frame = cap.read() #ret=retval(True:正常、False:不正常),frame=image    

  # 顯示圖片
  cv2.imshow('frame', frame)

  # 按a拍照存檔
  key=cv2.waitKey(1)#0=強制等待、1:等候1ms就跳過  更新影像
  if key == ord('a'): #使用者按了鍵盤'a'
    cv2.imwrite("test.jpg", frame)
  # 按q離開
  if key == ord('q'): #使用者按了鍵盤'q'
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()

