import json
import os

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Redirecting...</title>
    <script type="text/javascript">
        window.location.href = "{}";
    </script>
</head>
<body>
    <p>If you are not redirected, <a href="{}">click here</a>.</p>
</body>
</html>
"""

with open("links.json") as json_file:
    links = json.load(json_file)


for i in range(len(links)):
    folder = links[i]["from"]
    link = links[i]["to"]
    
    # create folder
    if not os.path.isdir(folder):
        os.mkdir(folder)
    
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.writelines(html.format(link, link))