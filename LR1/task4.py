import cv2

video = cv2.VideoCapture(r'..\resources\Dream_lake_1.mp4', cv2.CAP_ANY)

w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(r'..\resources\output.mp4', fourcc, 60, (w, h))

while True:
    ok, vid = video.read()

    if not ok:
        print('Конец видео')
        break

    cv2.imshow('Video', vid)
    video_writer.write(vid)

    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
video_writer.release()
cv2.destroyAllWindows()
