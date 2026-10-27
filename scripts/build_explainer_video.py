"""
Realistic SaaS Product Explainer Video Generator for YouTube Agent Kit.

Renders high-resolution 1920x1080 UI slides (terminal, IDE, validation dashboard, video engine),
synthesizes natural neural voiceover via Edge-TTS, and compiles a professional explainer video
using FFmpeg with smooth transitions and web-optimized compression.
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import imageio_ffmpeg
import edge_tts

REPO_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = REPO_ROOT / "docs" / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR = REPO_ROOT / "build_temp_video"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Fonts
FONT_REGULAR = "C:/Windows/Fonts/segoeui.ttf"
FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_CODE = "C:/Windows/Fonts/consola.ttf"
FONT_CODE_BOLD = "C:/Windows/Fonts/consolab.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def draw_window_frame(draw, x, y, w, h, title="bash — youtube-agent-kit"):
    # Window background
    draw.rounded_rectangle([x, y, x + w, y + h], radius=16, fill="#0F172A", outline="#334155", width=2)
    # Title bar
    draw.rounded_rectangle([x, y, x + w, y + 46], radius=16, fill="#1E293B")
    draw.rectangle([x, y + 36, x + w, y + 46], fill="#1E293B") # square bottom of title bar
    draw.line([x, y + 46, x + w, y + 46], fill="#334155", width=1)
    
    # macOS-style window controls
    draw.ellipse([x + 18, y + 16, x + 32, y + 30], fill="#EF4444")
    draw.ellipse([x + 38, y + 16, x + 52, y + 30], fill="#F59E0B")
    draw.ellipse([x + 58, y + 16, x + 72, y + 30], fill="#10B981")
    
    # Title text
    f_title = get_font(FONT_REGULAR, 15)
    draw.text((x + w // 2, y + 23), title, font=f_title, fill="#94A3B8", anchor="mm")

def draw_header(draw, step_num, step_title, step_desc):
    # Top banner
    f_brand = get_font(FONT_BOLD, 22)
    draw.text((80, 50), "YOUTUBE AGENT KIT", font=f_brand, fill="#60A5FA")
    
    f_tag = get_font(FONT_REGULAR, 16)
    draw.text((330, 56), "|   Autonomous Multi-Agent Creator Operating System", font=f_tag, fill="#64748B")
    
    # Step indicator pill
    f_pill = get_font(FONT_BOLD, 15)
    pill_text = f"STEP {step_num}"
    draw.rounded_rectangle([1650, 44, 1840, 78], radius=8, fill="#1E3A8A", outline="#3B82F6", width=1)
    draw.text((1745, 61), pill_text, font=f_pill, fill="#93C5FD", anchor="mm")
    
    # Section Title & Subtitle
    f_title = get_font(FONT_BOLD, 40)
    draw.text((80, 110), step_title, font=f_title, fill="#F8FAFC")
    
    f_desc = get_font(FONT_REGULAR, 20)
    draw.text((80, 165), step_desc, font=f_desc, fill="#94A3B8")

def create_slide_1(out_path):
    img = Image.new("RGB", (1920, 1080), color="#090D16")
    draw = ImageDraw.Draw(img)
    
    # Decorative subtle glow circles
    glow = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([1200, 200, 1900, 900], fill=(59, 130, 246, 25))
    glow_draw.ellipse([100, 600, 600, 1100], fill=(139, 92, 246, 25))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Header
    draw_header(draw, "01 / 05", "Universal AI Engine for Video Creators", 
                "Plug 14 production-grade AI skills into ChatGPT, Cursor, Claude, Antigravity, or Grok.")
    
    # Terminal Window (Left)
    draw_window_frame(draw, 80, 220, 920, 760, "zsh — terminal")
    f_code = get_font(FONT_CODE, 18)
    f_code_bold = get_font(FONT_CODE_BOLD, 18)
    
    lines = [
        ("$ git clone https://github.com/vbreddymora/youtube-agent-kit.git", "#F8FAFC", f_code_bold),
        ("Cloning into 'youtube-agent-kit'...", "#64748B", f_code),
        ("remote: Enumerating objects: 124, done.", "#64748B", f_code),
        ("remote: Total 124 (delta 62), reused 124", "#64748B", f_code),
        ("", "", f_code),
        ("$ python -m unittest discover tests", "#F8FAFC", f_code_bold),
        ("test_channel_archetypes (tests.test_benchmarks) ... ok", "#10B981", f_code),
        ("test_deterministic_validator (tests.test_validator) ... ok", "#10B981", f_code),
        ("test_hook_generator_compliance (tests.test_skills) ... ok", "#10B981", f_code),
        ("test_mcp_stdio_handshake (tests.test_mcp) ... ok", "#10B981", f_code),
        ("test_retention_scripting_rubric (tests.test_skills) ... ok", "#10B981", f_code),
        ("------------------------------------------------------------", "#334155", f_code),
        ("Ran 13 tests in 0.015s", "#F8FAFC", f_code_bold),
        ("OK — All 14 Agent Skills Verified & Ready", "#10B981", f_code_bold),
    ]
    
    curr_y = 280
    for text, color, font in lines:
        if text:
            draw.text((115, curr_y), text, font=font, fill=color)
        curr_y += 32
        
    # Feature Cards (Right Side)
    cards = [
        ("🧠 14 Open Agent Skills", "Standard Agent Skills spec. Works offline or in the cloud with zero lock-in.", "#3B82F6"),
        ("🛡️ Deterministic Validator", "Guarantees YouTube compliance: Title lengths, chapters, descriptions & tags.", "#10B981"),
        ("⚡ Headless Media Engine", "Neural Edge-TTS voiceovers and burned Hormozi subtitles rendered in 60s.", "#F59E0B"),
        ("🌐 100% Universal Compatibility", "Native configurations for ChatGPT, Cursor, Claude, Antigravity & Grok.", "#8B5CF6")
    ]
    
    card_y = 220
    for title, desc, border_col in cards:
        draw.rounded_rectangle([1040, card_y, 1840, card_y + 165], radius=14, fill="#0F172A", outline=border_col, width=2)
        f_card_t = get_font(FONT_BOLD, 22)
        draw.text((1075, card_y + 30), title, font=f_card_t, fill="#F8FAFC")
        f_card_d = get_font(FONT_REGULAR, 17)
        draw.text((1075, card_y + 75), desc, font=f_card_d, fill="#94A3B8")
        card_y += 195
        
    img.save(out_path, quality=95)

def create_slide_2(out_path):
    img = Image.new("RGB", (1920, 1080), color="#090D16")
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "02 / 05", "14 Modular Skills in Any IDE or Chat", 
                "Feed your channel topic directly into Cursor, Claude, or ChatGPT.")
    
    # IDE Window
    draw_window_frame(draw, 80, 220, 1760, 780, "Cursor / Claude Code — youtube-agent-kit")
    
    # Left Sidebar (Files)
    draw.rectangle([80, 267, 440, 998], fill="#0A0F1D")
    draw.line([440, 267, 440, 998], fill="#334155", width=1)
    
    f_side_h = get_font(FONT_BOLD, 14)
    draw.text((105, 290), "EXPLORER", font=f_side_h, fill="#64748B")
    
    files = [
        ("📁 skills/", "#93C5FD"),
        ("   📄 hook-generator", "#CBD5E1"),
        ("   📄 retention-scripting", "#38BDF8"), # active
        ("   📄 video-seo-metadata", "#CBD5E1"),
        ("   📄 thumbnail-concept", "#CBD5E1"),
        ("   📄 shorts-optimization", "#CBD5E1"),
        ("   📄 competitor-research", "#CBD5E1"),
        ("📁 references/", "#93C5FD"),
        ("   📄 retention-playbook.md", "#CBD5E1"),
        ("   📄 title-frameworks.md", "#CBD5E1"),
        ("📁 scripts/", "#93C5FD"),
        ("   🐍 validate_metadata.py", "#34D399"),
        ("   🐍 generate_short_video.py", "#34D399"),
    ]
    
    f_file = get_font(FONT_CODE, 16)
    sy = 330
    for fname, fcol in files:
        if "retention-scripting" in fname:
            draw.rectangle([80, sy - 4, 440, sy + 24], fill="#1E293B")
        draw.text((105, sy), fname, font=f_file, fill=fcol)
        sy += 36
        
    # Main Editor Prompt & Response
    f_chat_user = get_font(FONT_BOLD, 18)
    f_chat_body = get_font(FONT_REGULAR, 17)
    f_chat_code = get_font(FONT_CODE, 16)
    
    # User message card
    draw.rounded_rectangle([480, 300, 1800, 410], radius=10, fill="#1E293B", outline="#475569", width=1)
    draw.text((510, 320), "👤 USER PROMPT", font=f_chat_user, fill="#38BDF8")
    draw.text((510, 355), 
              "@youtube-agent-kit Create a 60-second retention script on 'Automating Busywork with AI'.\nInclude 3 stop-scroll hooks, scene-by-scene visual cues, and call to action.", 
              font=f_chat_body, fill="#F8FAFC")
    
    # Agent response card
    draw.rounded_rectangle([480, 440, 1800, 960], radius=10, fill="#0F172A", outline="#3B82F6", width=2)
    draw.text((510, 465), "🤖 AGENT EXECUTION (Skills: hook-generator + retention-scripting)", font=f_chat_user, fill="#60A5FA")
    
    agent_output = [
        ("HOOK 1 (Pattern Interrupt):", "#F59E0B", True),
        ('  "You\'re wasting 15 hours every single week on tasks a robot can do in 3 seconds."', "#F8FAFC", False),
        ("SCENE PACING & VISUAL DIRECTIVES:", "#10B981", True),
        ("  • Scene 1 (0-3s): Split screen. Left: Stressed person typing. Right: Smooth automated terminal.", "#94A3B8", False),
        ("  • Scene 2 (3-8s): Graphic zoom into n8n automated workflow + AI Agent trigger.", "#94A3B8", False),
        ("  • Scene 3 (8-25s): The 3 essential AI tools. Fast-cut typography every 2.4 seconds.", "#94A3B8", False),
        ("RETENTION RUBRIC VALIDATION:", "#A78BFA", True),
        ("  ✓ Passed: 0-3s Hook clarity score: 9.8/10", "#34D399", False),
        ("  ✓ Passed: Visual transitions budgeted every 3.2 seconds", "#34D399", False),
        ("  ✓ Passed: Frictionless payoff before 45s mark", "#34D399", False)
    ]
    
    ay = 510
    for line, lcol, is_bold in agent_output:
        draw.text((510, ay), line, font=get_font(FONT_CODE_BOLD if is_bold else FONT_CODE, 16), fill=lcol)
        ay += 38
        
    img.save(out_path, quality=95)

def create_slide_3(out_path):
    img = Image.new("RGB", (1920, 1080), color="#090D16")
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "03 / 05", "Deterministic YouTube Metadata Validation", 
                "Automated zero-error quality control before you publish to YouTube.")
    
    draw_window_frame(draw, 80, 220, 1760, 780, "Terminal — python scripts/validate_metadata.py")
    
    f_cmd = get_font(FONT_CODE_BOLD, 18)
    draw.text((115, 280), "$ python scripts/validate_metadata.py --title \"3 AI Tools That Save 15 Hours Weekly\" --chapters \"chapters.txt\"", font=f_cmd, fill="#F8FAFC")
    
    # Table Header
    draw.rectangle([115, 330, 1800, 380], fill="#1E293B")
    f_th = get_font(FONT_BOLD, 17)
    draw.text((140, 355), "METADATA FIELD", font=f_th, fill="#94A3B8", anchor="lm")
    draw.text((550, 355), "EXTRACTED VALUE / RULE", font=f_th, fill="#94A3B8", anchor="lm")
    draw.text((1200, 355), "BENCHMARK SPEC", font=f_th, fill="#94A3B8", anchor="lm")
    draw.text((1650, 355), "STATUS", font=f_th, fill="#94A3B8", anchor="lm")
    
    rows = [
        ("Video Title Length", "37 Characters ('3 AI Tools That Save...')", "Max 55 Chars (Mobile Cutoff Safe)", "✓ PASS", "#10B981"),
        ("Front-Loaded Keyword", "'AI Tools' in first 20 characters", "Must appear in first 4 words", "✓ PASS", "#10B981"),
        ("Description First 3 Lines", "Clear hook & problem statement present", "Visible above 'Show More' fold", "✓ PASS", "#10B981"),
        ("Timestamp Validation", "00:00 (Intro), 01:15 (Tool 1), 03:40 (Tool 2)", "Starts at 00:00, >= 3 chapters, min 10s gap", "✓ PASS", "#10B981"),
        ("HTTPS Links Verified", "github.com/vbreddymora/youtube-agent-kit", "Zero dead URLs, secure HTTPS only", "✓ PASS", "#10B981"),
        ("Target Tags Count", "14 Tags / 320 Characters", "Under 500 characters total", "✓ PASS", "#10B981"),
    ]
    
    ry = 405
    for field, val, spec, status, scol in rows:
        draw.rectangle([115, ry - 15, 1800, ry + 35], fill="#0F172A" if (ry // 50) % 2 == 0 else "#131C31")
        draw.text((140, ry + 10), field, font=get_font(FONT_BOLD, 16), fill="#F8FAFC", anchor="lm")
        draw.text((550, ry + 10), val, font=get_font(FONT_CODE, 16), fill="#CBD5E1", anchor="lm")
        draw.text((1200, ry + 10), spec, font=get_font(FONT_REGULAR, 16), fill="#94A3B8", anchor="lm")
        draw.text((1650, ry + 10), status, font=get_font(FONT_BOLD, 17), fill=scol, anchor="lm")
        ry += 52
        
    # Result Pill
    draw.rounded_rectangle([115, 760, 1800, 930], radius=12, fill="#064E3B", outline="#10B981", width=2)
    f_res_title = get_font(FONT_BOLD, 26)
    draw.text((160, 810), "🟢 AUDIT COMPLETE: 0 ISSUES, 0 WARNINGS — SUMMARY: PASS", font=f_res_title, fill="#34D399")
    f_res_desc = get_font(FONT_REGULAR, 18)
    draw.text((160, 860), "100% compliant with YouTube algorithm ranking factors, mobile app viewport, and CTR retention benchmarks.", font=f_res_desc, fill="#A7F3D0")
    
    img.save(out_path, quality=95)

def create_slide_4(out_path):
    img = Image.new("RGB", (1920, 1080), color="#090D16")
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "04 / 05", "Automated Headless Video Generation", 
                "Neural voiceover synthesis + Hormozi subtitles burned in one command.")
    
    # Left: Code & Pipeline Window
    draw_window_frame(draw, 80, 220, 1050, 780, "Terminal — python scripts/generate_short_video.py")
    
    f_code = get_font(FONT_CODE, 17)
    f_code_bold = get_font(FONT_CODE_BOLD, 17)
    
    pipeline_lines = [
        ("$ python scripts/generate_short_video.py", "#F8FAFC", f_code_bold),
        ("[1/4] Generating Neural Audio (en-US-ChristopherNeural)...", "#38BDF8", f_code),
        ("      -> Studio Voiceover: 128kbps 44.1kHz [44.8s audio]", "#94A3B8", f_code),
        ("[2/4] Formatting 5 High-Retention Visual Scenes...", "#38BDF8", f_code),
        ("      -> Cropping 1080x1920 portrait canvas...", "#94A3B8", f_code),
        ("      -> Adding smooth Ken Burns camera pan/zoom...", "#94A3B8", f_code),
        ("[3/4] Generating Synchronized Hormozi Captions (.srt)...", "#38BDF8", f_code),
        ("      -> Font: Impact / Yellow bold highlight on keywords...", "#94A3B8", f_code),
        ("[4/4] Hardware-Accelerated FFmpeg Video Rendering...", "#38BDF8", f_code),
        ("      frame= 1344 fps= 58 q=-1.0 Lsize= 25150kB time=00:00:44.80", "#10B981", f_code),
        ("------------------------------------------------------------", "#334155", f_code),
        ("SUCCESS: Rendered output_short.mp4 in 14.2s (1080x1920 @ 60fps)", "#34D399", f_code_bold),
    ]
    
    py = 280
    for text, color, font in pipeline_lines:
        draw.text((115, py), text, font=font, fill=color)
        py += 36
        
    # Render Progress Bar
    draw.rounded_rectangle([115, 840, 1090, 880], radius=8, fill="#1E293B")
    draw.rounded_rectangle([115, 840, 1090, 880], radius=8, fill="#10B981") # 100% full
    f_bar = get_font(FONT_BOLD, 15)
    draw.text((602, 860), "100% RENDER COMPLETE", font=f_bar, fill="#FFFFFF", anchor="mm")
    
    # Right: Realistic Vertical Phone Mockup
    draw.rounded_rectangle([1250, 220, 1750, 990], radius=32, fill="#000000", outline="#475569", width=4)
    # Notch/speaker
    draw.rounded_rectangle([1440, 235, 1560, 248], radius=6, fill="#1E293B")
    
    # Video screen area
    draw.rounded_rectangle([1260, 260, 1740, 975], radius=24, fill="#1E293B")
    
    # Mock video content inside phone
    draw.rectangle([1260, 260, 1740, 975], fill="#0F172A")
    # Grid lines / aesthetic graphic
    for gy in range(300, 950, 80):
        draw.line([1260, gy, 1740, gy], fill="#1E293B", width=1)
        
    # Hormozi Caption simulation
    f_sub1 = get_font(FONT_BOLD, 28)
    f_sub2 = get_font(FONT_BOLD, 36)
    draw.text((1500, 560), "STOP WASTING", font=f_sub1, fill="#FFFFFF", anchor="mm")
    draw.text((1500, 605), "15 HOURS", font=f_sub2, fill="#FACC15", anchor="mm") # bright yellow
    draw.text((1500, 650), "EVERY WEEK!", font=f_sub1, fill="#FFFFFF", anchor="mm")
    
    # UI Badges on phone
    draw.rounded_rectangle([1290, 900, 1710, 950], radius=10, fill=(0, 0, 0, 180), outline="#64748B", width=1)
    f_phone_tag = get_font(FONT_BOLD, 15)
    draw.text((1500, 925), "📱 1080x1920 Vertical Short Format", font=f_phone_tag, fill="#38BDF8", anchor="mm")
    
    img.save(out_path, quality=95)

def create_slide_5(out_path):
    img = Image.new("RGB", (1920, 1080), color="#090D16")
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, "05 / 05", "Universal Integration Across Every AI Tool", 
                "Zero proprietary lock-in. 100% open-source standard.")
    
    # 6 AI Tool Cards Grid
    tools = [
        ("ChatGPT", "Custom Instructions / Portable Prompts", "#10A37F", "Paste markdown prompts into any GPT-4o window."),
        ("Cursor IDE", ".cursorrules & Composer Ready", "#3B82F6", "Instant code completion and agent workflows in your editor."),
        ("Claude", "Agent Skills Specification", "#D97706", "Canonical folder structure native to Anthropic standards."),
        ("Google Antigravity", "Native Multi-Agent OS", "#4285F4", "Autonomous subagents with memory, tools, and background tasks."),
        ("Grok (X)", "Think Mode & Fast Research", "#FFFFFF", "Rapid competitor analytics and real-time outlier detection."),
        ("Windsurf & Cline", "MCP Stdio Server Integration", "#09B6A2", "Full tool-calling protocol support over standard stdio.")
    ]
    
    start_x, start_y = 100, 240
    cw, ch = 540, 210
    
    for i, (name, role, col, desc) in enumerate(tools):
        col_idx = i % 3
        row_idx = i // 3
        cx = start_x + col_idx * 590
        cy = start_y + row_idx * 240
        
        draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=14, fill="#0F172A", outline="#334155", width=2)
        # Accent indicator
        draw.rounded_rectangle([cx, cy, cx + 8, cy + ch], radius=4, fill=col)
        
        f_tname = get_font(FONT_BOLD, 24)
        draw.text((cx + 28, cy + 30), name, font=f_tname, fill="#F8FAFC")
        
        f_trole = get_font(FONT_BOLD, 15)
        draw.text((cx + 28, cy + 65), role, font=f_trole, fill=col)
        
        f_tdesc = get_font(FONT_REGULAR, 16)
        draw.text((cx + 28, cy + 110), desc, font=f_tdesc, fill="#94A3B8")
        
    # Bottom Call to Action Card
    draw.rounded_rectangle([100, 750, 1820, 960], radius=16, fill="#1E293B", outline="#3B82F6", width=2)
    f_cta_title = get_font(FONT_BOLD, 32)
    draw.text((960, 805), "Clone and Start Automating Your Channel Today", font=f_cta_title, fill="#F8FAFC", anchor="mm")
    
    f_cta_code = get_font(FONT_CODE_BOLD, 22)
    draw.rounded_rectangle([360, 855, 1560, 920], radius=10, fill="#090D16", outline="#60A5FA", width=1)
    draw.text((960, 887), "git clone https://github.com/vbreddymora/youtube-agent-kit.git", font=f_cta_code, fill="#38BDF8", anchor="mm")
    
    img.save(out_path, quality=95)

async def generate_narration():
    """Generate crystal-clear, realistic audio narration for each scene."""
    voice = "en-US-AndrewMultilingualNeural" # Natural, realistic software tech presenter voice
    
    scripts = [
        ("scene1.mp3", "Meet YouTube Agent Kit: an open-source multi-agent system that turns any AI model into a full-stack YouTube production team."),
        ("scene2.mp3", "Fourteen canonical agent skills plug straight into Cursor, Claude, or ChatGPT to generate viral retention hooks and production-ready video scripts."),
        ("scene3.mp3", "Our deterministic validator automatically inspects mobile title cutoffs, description chapters, and algorithm ranking factors before you ever publish."),
        ("scene4.mp3", "Need video? The headless media engine synthesizes studio neural voiceovers and burns high-retention subtitles into full HD videos in seconds."),
        ("scene5.mp3", "Zero proprietary lock-in. Full creator control. Clone YouTube Agent Kit on GitHub and start automating your channel today.")
    ]
    
    audio_paths = []
    durations = []
    
    for filename, text in scripts:
        out_file = TEMP_DIR / filename
        communicate = edge_tts.Communicate(text, voice, rate="+2%")
        await communicate.save(str(out_file))
        audio_paths.append(str(out_file))
        
        # probe audio duration with ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        cmd = [ffmpeg_exe, "-i", str(out_file)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        # Parse duration from ffmpeg stderr
        dur = 8.0 # fallback
        for line in res.stderr.splitlines():
            if "Duration:" in line:
                try:
                    time_str = line.split("Duration:")[1].split(",")[0].strip()
                    h, m, s = time_str.split(":")
                    dur = float(h) * 3600 + float(m) * 60 + float(s) + 0.6 # padding
                except Exception:
                    pass
        durations.append(dur)
        print(f"Generated {filename}: {dur:.2f}s")
        
    return audio_paths, durations

def assemble_video(scene_imgs, audio_paths, durations, output_mp4, output_gif):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # First: create individual video clips for each scene
    clip_files = []
    for i, (img, aud, dur) in enumerate(zip(scene_imgs, audio_paths, durations)):
        clip_path = TEMP_DIR / f"clip_{i}.mp4"
        cmd = [
            ffmpeg_exe, "-y",
            "-loop", "1", "-i", img,
            "-i", aud,
            "-c:v", "libx264", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", str(dur),
            str(clip_path)
        ]
        subprocess.run(cmd, check=True)
        clip_files.append(str(clip_path))
        
    # Concat clips using concat demuxer
    concat_list = TEMP_DIR / "concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for c in clip_files:
            clean_path = c.replace("\\", "/")
            f.write(f"file '{clean_path}'\n")
            
    # Render final MP4
    print("Rendering final MP4...")
    cmd_concat = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(output_mp4)
    ]
    subprocess.run(cmd_concat, check=True)
    print(f"Successfully generated MP4: {output_mp4}")
    
    # Generate animated GIF preview for README (720p width, 12fps, highly optimized palette)
    print("Generating optimized animated GIF preview for README...")
    palette = TEMP_DIR / "palette.png"
    subprocess.run([
        ffmpeg_exe, "-y",
        "-i", str(output_mp4),
        "-vf", "fps=10,scale=800:-1:flags=lanczos,palettegen",
        str(palette)
    ], check=True)
    
    subprocess.run([
        ffmpeg_exe, "-y",
        "-i", str(output_mp4),
        "-i", str(palette),
        "-lavfi", "fps=10,scale=800:-1:flags=lanczos [x]; [x][1:v] paletteuse=dither=bayer:bayer_scale=3",
        "-t", "18", # First 18s preview loop
        str(output_gif)
    ], check=True)
    print(f"Successfully generated GIF: {output_gif}")

async def main():
    print("Step 1: Rendering realistic UI slides...")
    slide1 = str(TEMP_DIR / "slide1.png")
    slide2 = str(TEMP_DIR / "slide2.png")
    slide3 = str(TEMP_DIR / "slide3.png")
    slide4 = str(TEMP_DIR / "slide4.png")
    slide5 = str(TEMP_DIR / "slide5.png")
    
    create_slide_1(slide1)
    create_slide_2(slide2)
    create_slide_3(slide3)
    create_slide_4(slide4)
    create_slide_5(slide5)
    
    print("Step 2: Generating neural voiceover...")
    audio_paths, durations = await generate_narration()
    
    print("Step 3: Assembling full explainer video and preview GIF...")
    final_mp4 = ASSETS_DIR / "explainer_demo.mp4"
    final_gif = ASSETS_DIR / "explainer_preview.gif"
    
    assemble_video([slide1, slide2, slide3, slide4, slide5], audio_paths, durations, final_mp4, final_gif)
    print("ALL DONE!")

if __name__ == "__main__":
    asyncio.run(main())
