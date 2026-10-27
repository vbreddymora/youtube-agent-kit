"""
Automated YouTube Short Video Generator (Option B).

Uses:
- `edge-tts` for natural, human-like neural voiceover synthesis (free, no API key).
- `imageio-ffmpeg` for native high-definition 1080x1920 MP4 video rendering.
- `PIL` for image dimension validation and formatting.
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path

# Force UTF-8 encoding on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import imageio_ffmpeg
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
VENV_DIR = REPO_ROOT / ".venv"


async def generate_voiceover(text: str, output_audio: str, voice: str = "en-US-ChristopherNeural") -> None:
    """Generate realistic neural voiceover using edge-tts."""
    import edge_tts
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_audio)


def render_short_video(
    image_path: str,
    audio_path: str,
    output_mp4: str,
    target_width: int = 1080,
    target_height: int = 1920,
) -> bool:
    """Render a 9:16 vertical MP4 video from an image and audio using FFmpeg."""
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    # Ensure image is resized/cropped to 1080x1920
    img = Image.open(image_path).convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = target_width / target_height

    # Crop to vertical 9:16
    if img_ratio > target_ratio:
        new_width = int(img.height * target_ratio)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))

    resized_img_path = str(REPO_ROOT / ".tmp_render_img.jpg")
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    img.save(resized_img_path, quality=95)

    # Run FFmpeg command: loop image, add audio, encode H.264 MP4 with subtle Ken Burns zoom
    cmd = [
        ffmpeg_exe,
        "-y",
        "-loop", "1",
        "-i", resized_img_path,
        "-i", audio_path,
        "-vf", "scale=1080:1920,zoompan=z='min(zoom+0.0006,1.1)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        output_mp4
    ]

    print(f"🎬 Rendering MP4 video with FFmpeg to {output_mp4}...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if os.path.exists(resized_img_path):
        os.remove(resized_img_path)

    if res.returncode != 0:
        print(f"❌ FFmpeg error: {res.stderr[-300:]}")
        return False

    print(f"✅ Video rendered successfully: {output_mp4}")
    return True


def main():
    script_text = (
        "If you are still doing data entry by hand in 2026, you are wasting 15 hours every single week. "
        "Here are 3 AI tools that will do it for you. "
        "First is n8n. Instead of Zapier, this connects your Gmail, Sheets, and WhatsApp into autonomous workflows that run 100% free on your computer. "
        "Second is Agentic Browser AI. You don't click buttons anymore. Just type 'book this flight' or 'research 20 leads'—it opens the browser and clicks everything for you. "
        "Third: Intelligent Document Parsers. Dump 500 messy PDF invoices into it—it reads messy scans, extracts every number, and files your taxes in 10 seconds. "
        "The future of work is not about working harder, it is about letting autonomous AI handle repetitive busywork so you can focus on what actually matters. "
        "Drop a comment if you want the setup guide!"
    )

    audio_file = str(REPO_ROOT / "voiceover_neural.mp3")
    cover_image = str(REPO_ROOT / "cover.jpg")
    output_video = str(REPO_ROOT / "output_short.mp4")

    print("🎙️ Step 1: Generating natural neural voiceover...")
    asyncio.run(generate_voiceover(script_text, audio_file, voice="en-US-ChristopherNeural"))
    print(f"✅ Audio generated: {audio_file}")

    print("🎞️ Step 2: Rendering 1080x1920 vertical MP4 video...")
    success = render_short_video(cover_image, audio_file, output_video)

    if success:
        size_mb = os.path.getsize(output_video) / (1024 * 1024)
        print(f"\n🎉 DONE! Generated production-ready YouTube Short:")
        print(f"📁 Path: {output_video}")
        print(f"📊 Size: {size_mb:.2f} MB")
        print(f"📐 Resolution: 1080x1920 (Vertical 9:16)")


if __name__ == "__main__":
    main()
