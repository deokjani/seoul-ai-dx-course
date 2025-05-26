import torch

# 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 샘플 이미지
img = "https://image.kmib.co.kr/online_image/2020/1122/611718110015239102_5.jpg"

# 예측 : Predict
results = model(img)

# 결과 확인
results.print()  # 콘솔에 출력
results.show()  # 화면에 표시
results.save()  # 저장

# cd /labeling   labelimg
# python detect.py --weights yolov5s.pt --source "https://image.kmib.co.kr/online_image/2020/1122/611718110015239102_5.jpg" classes 0
# python detect.py --weights yolov5s.pt --source aespa.mp4 classes 0

