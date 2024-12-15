import markdown
import os
import re
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension

from datetime import datetime

def fetch_content(name:str):
    with open(name, "r", encoding="utf-8") as f:
        content = f.read()
        f.close()
        return content

def render_markdown(filename:str, playername:str):
    markdown_text = fetch_content(filename)
    
    prefix = f"""
    <button type="button" class="collapsible"><strong>{playername.split("/")[-1].capitalize().replace("_", " ")}</strong></button>
            <div class="collapsible-content">
    """
    suffix = "</div> "

    html = convert_markdown_to_html(markdown_text).replace("h2", "h3")

    return prefix + html + suffix
  

def convert_markdown_to_html(markdown_text):
    """
    Convert markdown text to HTML.
    
    Args:
        markdown_text (str): The markdown text to convert.
    
    Returns:
        str: The converted HTML.
    """
    return markdown.markdown(markdown_text, extensions=[ CodeHiliteExtension(linenums=False), FencedCodeExtension() ])

def render_template(template_name:str, path_raw:bool = False) -> str:
    if not path_raw:
        path = f"{template_name}/template.html"
    else:
        path = template_name
    content = fetch_content(path)

    include_regex_list = re.findall("@Include\((.*)\)", content)

    for include_regex in include_regex_list:
        print(include_regex)
        content = content.replace(f"@Include({include_regex})", render_template(include_regex, True))

    render_regex_list = re.findall("@Render\((.*)\)", content)

    for render_regex in render_regex_list:
        print(render_regex)
        content = content.replace(f"@Render({render_regex})", render_markdown(f"{template_name}/{render_regex}", render_regex.split(".")[0]))

    content = content.replace("@Timestamp", str(datetime.now().timestamp().__round__()))

    return content

def build_template(template_name:str) -> None:
    content = render_template(template_name)

    fout = open(f"webserver/templates/{template_name}.html", "w", encoding="utf-8")
    fout.write(content)

def main():
    build_template("court")
    build_template("court2")
    pass

if __name__ == "__main__":
    main()