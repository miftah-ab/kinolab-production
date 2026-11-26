#!/usr/bin/env python3
"""Create a video contact sheet with FFmpeg; this does not replace full playback."""
import argparse, shutil, subprocess, sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("video",type=Path)
    p.add_argument("--output",type=Path,default=Path("contact-sheet.jpg"))
    p.add_argument("--interval",type=float,default=2.0)
    p.add_argument("--columns",type=int,default=4)
    p.add_argument("--width",type=int,default=320)
    a=p.parse_args()
    if not a.video.is_file(): p.error(f"Video not found: {a.video}")
    if min(a.interval,a.columns,a.width)<=0: p.error("interval, columns and width must be positive")
    if not shutil.which("ffmpeg"):
        print("ffmpeg not found",file=sys.stderr); return 2
    vf=f"fps=1/{a.interval},scale={a.width}:-1,tile={a.columns}x999"
    r=subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-i",str(a.video),
        "-vf",vf,"-frames:v","1","-q:v","3",str(a.output)],text=True,capture_output=True)
    if r.returncode:
        print(r.stderr.strip() or "Contact sheet generation failed",file=sys.stderr)
        return r.returncode or 1
    print(f"Created: {a.output.resolve()}")
    print("Inspect this sheet, then play the complete video at normal speed.")
    return 0
if __name__=="__main__": raise SystemExit(main())
