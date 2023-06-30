import moviepy.editor as mpy


def find_speaking_clips(audio, window_size=0.1, padding=0.25):
    num_windows = math.floor(audio.duration/window_size)
    print(num_windows)


def edit_video(input_video_name, output_name):

    video = mpy.VideoFileClip(input_video_name)
    audio = video.audio

    clips = find_speaking_clips(audio)
    # clips = [(30, 60), (90, 120)]

    video_clips = [video.subclip(clip[0], clip[1]) for clip in clips]

    final_clip = mpy.concatenate_videoclips(video_clips)

    final_clip.write_videofile(output_name,
                              fps=60,
                              codec="libx264",
                              audio_codec="aac",
                              audio_bitrate="128k",
                              temp_audiofile="temp-audio.m4a",
                              remove_temp=True,
                              ffmpeg_params=["-crf", "10"])
    video.close()

# edit_video("fetch-image.mov", "edited-video.mp4")