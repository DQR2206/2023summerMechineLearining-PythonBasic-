#该版本为保存视频的全部帧
import os
import cv2
import random
import shutil

def split_frames_to_train_val(folder_path, output_folder, train_ratio=0.8, shuffle=True):
    # 创建 train 和 val 文件夹
    train_folder = os.path.join(output_folder, "train")
    val_folder = os.path.join(output_folder, "val")
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    # 获取指定文件夹中的所有视频文件
    video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file)
        video_name = os.path.splitext(video_file)[0]

        # 建立与视频同名的文件夹，用于存储提取的帧
        output_video_folder = os.path.join(output_folder, video_name)
        os.makedirs(output_video_folder, exist_ok=True)

        # 打开视频文件
        video = cv2.VideoCapture(video_path)
        frame_count = 0
        success = True

        while success:
            # 读取一帧图像
            success, image = video.read()

            # 保存图像
            if success:
                output_path = os.path.join(output_video_folder, f"{video_name}_frame_{frame_count}.jpg")
                cv2.imwrite(output_path, image)

            frame_count += 1

        video.release()

        # 输出视频帧数
        print(f"视频 '{video_name}' 的帧数为: {frame_count}")

        frames = os.listdir(output_video_folder)
        if shuffle:
            random.shuffle(frames)

        train_frames = frames[:int(train_ratio * len(frames))]
        val_frames = frames[int(train_ratio * len(frames)):]

        # 将训练集和验证集的帧分别存入对应的文件夹
        for frame in train_frames:
            src_path = os.path.join(output_video_folder, frame)
            dst_path = os.path.join(train_folder, frame)
            shutil.move(src_path, dst_path)

        for frame in val_frames:
            src_path = os.path.join(output_video_folder, frame)
            dst_path = os.path.join(val_folder, frame)
            shutil.move(src_path, dst_path)

        # 删除原始文件夹
        os.rmdir(output_video_folder)


# 示例用法
video_folder_path = r"D:\data_set\videodata"  # 视频文件夹路径
output_folder = r"D:\data_set\picture"  # 存储提取帧的文件夹路径

split_frames_to_train_val(video_folder_path, output_folder)