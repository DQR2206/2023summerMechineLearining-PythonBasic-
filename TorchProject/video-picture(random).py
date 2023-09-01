#该版本为从视频中随机选取10帧进行保存 并未进行训练集与验证集的划分
import os
import cv2
import random
import shutil

def extract_frames(video_folder, output_folder):
    picture_folder = os.path.join(output_folder, "picture")
    os.makedirs(picture_folder, exist_ok=True)
    video_files = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f))]

    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        video_name = os.path.splitext(video_file)[0]

        # 打开视频文件
        video = cv2.VideoCapture(video_path)
        frame_count = 0
        success = True

        frames = []

        while success:
            success, image = video.read()

            if success:
                frames.append(image)

            frame_count += 1

        video.release()

        # 输出每个视频的帧数
        print(f"视频 '{video_name}' 的帧数为: {frame_count}")

        # 随机抽取连续的10帧
        num_frames = len(frames)

        if num_frames < 10:
            continue

        start_index = random.randint(0, num_frames - 10)

        # 提取连续的10帧并将其保存在picture的相应文件夹中
        extracted_frames_folder = os.path.join(picture_folder, f"{video_name}_extracted")
        os.makedirs(extracted_frames_folder, exist_ok=True)

        for i in range(start_index, start_index + 10):
            frame = frames[i]
            frame_path = os.path.join(extracted_frames_folder, f"{video_name}_frame_{i}.jpg")
            cv2.imwrite(frame_path, frame)


# 示例用法
video_folder_path = r"D:\data_set\videodata"  # 视频文件夹路径
output_folder_path = r"D:\data_set"  # 输出文件夹路径

extract_frames(video_folder_path, output_folder_path)