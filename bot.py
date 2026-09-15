import random, re, datetime

THEMES = [
    ("#0aa5e2", "#fafafa", "#1a1a1a", "#777", "#e5e5e5"),   # light blue
    ("#e2703a", "#faf6f2", "#1a1a1a", "#777", "#e8ddd3"),   # warm orange
    ("#3a7d5c", "#f5faf7", "#1a1a1a", "#777", "#dde8e0"),   # forest green
    ("#8b5cf6", "#f8f7fc", "#1a1a1a", "#777", "#e5e2f0"),   # violet
    ("#c0392b", "#fdf7f6", "#1a1a1a", "#777", "#f0dedb"),   # red
    ("#1a1a1a", "#111111", "#eaeaea", "#999", "#2a2a2a"),   # dark mode
]

HEROES = [
    ("hey, i'm", "ice.", "front-end developer & designer — i build clean things for the web."),
    ("hello,", "ice.", "i make simple websites that work."),
    ("yo,", "ice.", "developer. designer. occasionally in the ocean."),
    ("hi there,", "ice.", "front-end dev who likes whitespace."),
]

PROJECTS = [
    ("e-commerce store", "online shop with cart & filters, pure html/css/js"),
    ("portfolio v2", "personal site with dark mode & scroll animations"),
    ("game dashboard", "stats tracker ui inspired by long gaming nights"),
    ("wave tracker", "surf forecast app for my local beach"),
    (" habit app", "minimal daily habit tracker, no login needed"),
    ("photo grid", "infinite scrolling gallery with lazy loading"),
    ("chat ui", "realtime chat interface concept"),
    ("music player", "tiny web audio player with visualizer"),
]

def replace_block(text, name, new_content):
    pattern = re.compile(rf"<!-- BOT:{name}:START -->.*?<!-- BOT:{name}:END -->", re.S)
    return pattern.sub(new_content, text)

# --- theme (style.css) ---
accent, bg, text_color, muted, line = random.choice(THEMES)
css = open("style.css").read()
new_theme = (f"/* BOT:THEME:START */\n:root {{\n  --accent: {accent};\n"
             f"  --bg: {bg};\n  --text: {text_color};\n  --muted: {muted};\n"
             f"  --line: {line};\n}}\n/* BOT:THEME:END */")
css = replace_block(css, "THEME", new_theme)

# --- hero (index.html) ---
hello, name, sub = random.choice(HEROES)
html = open("index.html").read()
html = replace_block(html, "HERO",
    f'<!-- BOT:HERO:START -->\n<header class="hero" id="top">\n'
    f'  <p class="hello">{hello}</p>\n'
    f'  <h1>{name}<span class="dot">.</span></h1>\n'
    f'  <p class="sub">{sub}</p>\n</header>\n<!-- BOT:HERO:END -->')

# --- projects (index.html) ---
projs = random.sample(PROJECTS, 3)
cards = ""
for i, (title, desc) in enumerate(projs, 1):
    cards += (f'    <a class="card" href="#">\n'
              f'      <span class="num">0{i}</span>\n'
              f'      <h3>{title.strip()}</h3>\n'
              f'      <p>{desc}</p>\n    </a>\n')
html = replace_block(html, "PROJECTS",
    '<!-- BOT:PROJECTS:START -->\n  <div class="grid">\n' +
    cards +
    '  </div>\n  <!-- BOT:PROJECTS:END -->')

open("style.css", "w").write(css)
open("index.html", "w").write(html)
print(f" rewrote site | theme={accent} | hero='{name}' | projects={[p[0].strip() for p in projs]}")