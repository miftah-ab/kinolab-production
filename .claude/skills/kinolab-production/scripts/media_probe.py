#!/usr/bin/env python3
"""Read media metadata with ffprobe; optional heuristic black/freeze/silence scan."""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

def run(cmd):
    return subprocess.run(cmd, text=True, capture_output=True, check=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("media",type=Path); p.add_argument("--scan",action="store_true")
    p.add_argument("--black-duration",type=float,default=0.15)
    p.add_argument("--freeze-duration",type=float,default=1.5)
    p.add_argument("--silence-duration",type=float,default=0.5)
    a=p.parse_args()
    if not a.media.is_file(): p.error(f"File not found: {a.media}")
    if not shutil.which("ffprobe"):
        print("ffprobe not found; install FFmpeg or inspect manually",file=sys.stderr); return 2
    r=run(["ffprobe","-v","error","-show_format","-show_streams","-of","json",str(a.media)])
    if r.returncode:
        print(r.stderr.strip() or "ffprobe failed",file=sys.stderr); return r.returncode or 1
    d=json.loads(r.stdout); f=d.get("format",{})
    out={"file":str(a.media),"format":f.get("format_name"),
         "duration_seconds":float(f["duration"]) if f.get("duration") else None,
         "size_bytes":int(f["size"]) if f.get("size") else None,"streams":[]}
    for s in d.get("streams",[]):
        out["streams"].append({k:s.get(k) for k in
          ("index","codec_type","codec_name","profile","width","height","pix_fmt",
           "avg_frame_rate","sample_rate","channels","channel_layout","color_space",
           "color_transfer","color_primaries")})
    if a.scan:
        if not shutil.which("ffmpeg"): out["scan_warning"]="ffmpeg not found; metadata only"
        else:
            vf=(f"blackdetect=d={a.black_duration}:pix_th=0.10,"
                f"freezedetect=n=-50dB:d={a.freeze_duration},"
                f"silencedetect=noise=-50dB:d={a.silence_duration}")
            q=run(["ffmpeg","-hide_banner","-i",str(a.media),"-vf",vf,"-an","-f","null","-"])
            out["heuristic_scan"]={"return_code":q.returncode,"log":q.stderr[-12000:]}
    print(json.dumps(out,indent=2))
    print("\nHeuristics are not proof of quality. Play the full video and listen to the full audio.")
    return 0
if __name__=="__main__": raise SystemExit(main())
