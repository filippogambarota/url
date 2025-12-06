# Redirect

This repository contains a very simple implementation of a redirect service. Assuming you want to share a Google Form link or open a certain link with a complex url. Instead of sharing the actual url you can share a custom url in the format `[your Github username].github.io/url/[custom url]`. Clearly, renaming the repository will change the `url` part to whatever you like.

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
