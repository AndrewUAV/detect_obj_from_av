import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Не удалось открыть видеофайл: {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame_number in range(0, duration, fps):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if ret:
            frame_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(video_path))[0]}_{frame_number // fps + 1}.jpg")
            cv2.imwrite(frame_path, frame)
        else:
            print(f"Не удалось прочитать кадр {frame_number} из {video_path}")

    cap.release()

if __name__ == "__main__":
    videos_folder = "data_for_learn"
    output_folder = "data_for_learn/photo_from_video"

    video_files = [f for f in os.listdir(videos_folder) if f.endswith((".mp4", ".avi", ".mkv",'.MP4'))]

    for video_file in video_files:
        video_path = os.path.join(videos_folder, video_file)
        extract_frames(video_path, output_folder)

    print("end.")
