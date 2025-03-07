import subprocess 

from .post_processing import PostProcessing 

try:
    import tkinter
except ImportError:
    pass
else:
    from .video_tkinter import VideoTkinter

try:
    import PyQt6
except ImportError:
    pass 
else:
    from .video_pyqt import VideoPyQT

try:
    import pygame
except ImportError:
    pass 
else:
    pygame.init()

    from .video_pygame import VideoPygame as Video
    from .subtitles import Subtitles
    from .video_player import VideoPlayer
    from .webcam import Webcam

try:
    import pyglet
except ImportError:
    pass 
else:
    from .video_pyglet import VideoPyglet


_VERSION = "0.9.11"


def get_version_info() -> dict:
    try:
        pygame_ver = pygame.version.ver
    except NameError:
        pygame_ver = "not installed"

    try:
        ffmpeg_ver = subprocess.run(["ffmpeg", "-version"], capture_output=True, universal_newlines=True).stdout.split(" ")[2]
    except FileNotFoundError:
        ffmpeg_ver = "not installed"

    return {"pyvidplayer2": _VERSION,
            "ffmpeg": ffmpeg_ver,
            "pygame": pygame_ver}