import cv2
import os

def video_to_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_path = os.path.join(output_folder, f"frame_{frame_number:04d}.png")
        cv2.imwrite(frame_path, frame)
        frame_number += 1

    cap.release()

video_path = 'your_video.mp4'
output_folder = 'frames'
video_to_frames(video_path, output_folder)
