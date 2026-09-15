import random, datetime

ACTIONS = ["edit", "rewrite", "delete", "add"]

html_templates = [
"""<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="style.css">
  <title>Auto Bot</title>
</head>
<body>
  <h1>Auto-generated page v{n}</h1>
  <p>Rewritten by the bot on {date}</p>
</body>
</html>
""",
"""<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Version {n}</h1>
  <ul><li>bot was here</li></ul>
</body>
</html>
"""]

css_snippets = [
    "h1 { color: #58a6ff; }",
    "body { margin: 40px; }",
    "p { font-size: 18px; }",
    ".box { border: 1px solid #3fb950; padding: 10px; }",
]
html_snippets = [
    "<!-- edited by bot -->",
    "<p>New line added automatically.</p>",
    "<div class='box'>bot box</div>",
]

def edit_file(path, snippets):
    with open(path) as f:
        lines = f.readlines()
    if not lines:
        return
    i = random.randrange(len(lines))
    lines[i] = random.choice(snippets) + "\n"      # overwrite a random line
    with open(path, "w") as f:
        f.writelines(lines)

def delete_line(path):
    with open(path) as f:
        lines = f.readlines()
    if len(lines) > 3:                               # keep file from breaking
        lines.pop(random.randrange(len(lines)))
        with open(path, "w") as f:
            f.writelines(lines)

def add_line(path, snippets):
    with open(path, "a") as f:
        f.write(random.choice(snippets) + "\n")

def rewrite():
    n = random.randint(1, 999)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("index.html", "w") as f:
        f.write(random.choice(html_templates).format(n=n, date=date))

action = random.choice(ACTIONS)
if action == "edit":
    edit_file("style.css", css_snippets)
elif action == "delete":
    delete_line(random.choice(["index.html", "style.css"]))
elif action == "add":
    add_line("style.css", css_snippets)
    add_line("index.html", html_snippets)
else:
    rewrite()
print("Bot action:", action)