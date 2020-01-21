# coding:utf-8
import boto3
import cv2
import pygame
import json
from mutagen.mp3 import MP3 as mp3

# カメラの設定
CAMERA_ID = 0  # 端末のカメラのID(デオフォルトは0)
cap = cv2.VideoCapture(CAMERA_ID)

# AWS情報の読込
aws_info = json.load(open('credentials.json', 'r'))

# APIクライアント作成
rekognition = boto3.client('rekognition',
                           aws_access_key_id=aws_info['aws_access_key_id'],
                           aws_secret_access_key=aws_info['aws_secret_access_key'],
                           region_name=aws_info['region_name'],
                           )

# 表示設定
scale_factor: float = .15  # スケールの設定
green = (0, 255, 0)  # 枠線の色
red = (0, 0, 255)  # 枠線の色
frame_thickness = 2  # 枠線の幅
fontscale = 1.0  # フォントサイズ
color = (0, 120, 238)  # フォント色 (B, G, R)
fontface = cv2.FONT_HERSHEY_DUPLEX  # フォント

count = 0
# qが推されるまで実行を続ける
while(True):
# デバッグ用にカウンタを作成
# while (count < 1):
    
    # フレームをキャプチャ取得
    ret, frame = cap.read()
    # リクエスト前に画像ファイル圧縮
    height, width, channels = frame.shape
    small = cv2.resize(frame, (int(width * scale_factor), int(height * scale_factor)))
    ret, buf = cv2.imencode('.jpg', small)

    # RekognitionAPI実行
    faces = rekognition.detect_faces(Image={'Bytes': buf.tobytes()}, Attributes=['ALL'])

    # カウンタ
    count = count+1

    # カウンタをインクリメントするので実行を一度のみ行い、レスポンスを  整形されたJSONとして吐き出す
    print(json.dumps(faces, indent=4, sort_keys=True))

    # 描画
    if len(faces['FaceDetails']) == 0:
        continue
    face = faces['FaceDetails'][0]
    smile = face['Smile']['Value']
    # 顔の周りの枠線の描画例：img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
    # 引数は（画像、左上の座標、右下の座標、色、線の幅）
    cv2.rectangle(frame,
                  (int(face['BoundingBox']['Left'] * width),
                   int(face['BoundingBox']['Top'] * height)),
                  (int((face['BoundingBox']['Left'] + face['BoundingBox']['Width']) * width),
                   int((face['BoundingBox']['Top'] + face['BoundingBox']['Height']) * height)),
                  green if smile else red, frame_thickness)
    #テキストの描写
    cv2.putText(frame,#画像ファイル
                str("Smile") + ": " + str(face['Smile']['Confidence']),    # テキストデータ
                (25, 40), # 座標(テキストを書き始める位置の左下)
                fontface, # フォント
                fontscale, #フォントサイズ
                color)  #テキストカラー

    # 結果をディスプレイに表示
    cv2.imshow('frame', frame)

    #音声ファイル出力
    if not smile:
        filename = 'TOMINAGA_OUT.mp3'  # 再生したいmp3ファイル
        pygame.mixer.init()
        pygame.mixer.music.load(filename)  # 音源を読み込み
        mp3_length = mp3(filename).info.length  # 音源の長さ取得
        pygame.mixer.music.play(1)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
