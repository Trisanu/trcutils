import markdownify
# html_file       = "markdown/Source_1.html"
html_file       = "markdown/ApacheSetup.html"
markdown_file   = "markdown/ApacheSetup.md"
# ----------------------------------------------------------------------

with open(html_file, "r") as f:
    convert = markdownify.markdownify(f.read(), heading_style="ATX")

with open(markdown_file, "w") as f:
    f.write(convert)
