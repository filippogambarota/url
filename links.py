import json
import os
import shutil

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

README="""
This repository contains a very simple implementation of a redirect service. Assuming you want to share a Google Form link or open a certain link with a complex url. Instead of sharing the actual url you can share a custom url in the format `filippogambarota.github.io/l/[custom url]`. Clearly, renaming the repository will change the `url` part to whatever you like.

To create the links you can simply modify the `links.json` file (also directly on Github without cloning) with the following format:

```json
[
  {
    "from": "custom url",
    "to": "real url"
  }
]
```

The `links.py` script will create a folder called as `"custom url"` with a `index.html` file inside contaning the `"real url"` as the target url. After commiting changes to the `links.json` file, a Github Action will create all new links/folders.

# Links

"""

with open("links.json") as json_file:
    links = json.load(json_file)

# remove unused folders

keep = ['.github', ".git"]

files_and_dirs = os.listdir()

# keep only folders with links
dirs = [f for f in files_and_dirs if os.path.isdir(f) and f not in keep]

if len(links) < 1:
    for d in dirs:
        shutil.rmtree(d)
    quit()

new_links_dirs = [l["from"] for l in links]
dirs_to_remove = [d for d in dirs if d not in new_links_dirs]

if len(dirs_to_remove) > 0:
    for d in dirs_to_remove:
        shutil.rmtree(d)

for i in range(len(links)):
    folder = links[i]["from"]
    link = links[i]["to"]
    
    # create folder
    if not os.path.isdir(folder):
        os.mkdir(folder)
    
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.writelines(html.format(link, link))

# format links as markdown

md_links = []

for i in range(len(links)):
    md_links.append("- from [{}]({}) to [{}]({})\n".format(links[i]["from"], links[i]["from"], links[i]["to"], links[i]["to"]))

# add links to readme

for i in range(len(md_links)):
    README += md_links[i]

with open("README.md", "w") as readme:
    readme.writelines(README)