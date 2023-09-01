#截取固定起点和终点的视频

import os
import cv2


def extract_video_from_folder(input_folder, output_folder, start_time, end_time):
    # 获取输入文件夹下的视频文件列表
    video_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for video_file in video_files:
        video_path = os.path.join(input_folder, video_file)

        # 构建输出视频的文件路径
        output_path = os.path.join(output_folder, f"output_{os.path.splitext(video_file)[0]}.mp4")

        # 调用 extract_video 函数截取视频
        extract_video(video_path, output_path, start_time, end_time)


def extract_video(video_path, output_path, start_time, end_time):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    # 获取视频的帧率
    fps = video.get(cv2.CAP_PROP_FPS)

    # 计算开始帧和结束帧的位置
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    # 设置视频编解码器和输出格式
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output = cv2.VideoWriter(output_path, fourcc, fps,
                             (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    # 定位到开始帧
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    frame_count = start_frame

    # 截取指定帧范围内的视频
    while frame_count <= end_frame:
        success, frame = video.read()

        if success:
            output.write(frame)

        frame_count += 1

    # 释放资源
    video.release()
    output.release()


# 示例用法
input_folder = r"D:\data_set\videodata"  # 输入视频文件夹路径
output_folder = r"D:\data_set\video" # 输出视频文件夹路径
start_time = 0  # 起始时间（秒）
end_time = 1  # 结束时间（秒）

extract_video_from_folder(input_folder, output_folder, start_time, end_time)