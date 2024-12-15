import markdown
import os
import re

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
    return markdown.markdown(markdown_text)

def build_template(template_name:str):
    content = fetch_content(f"{template_name}/template.html")

    render_regex_list = re.findall("@Render\((.*)\)", content)

    for render_regex in render_regex_list:
        print(render_regex)
        content = content.replace(f"@Render({render_regex})", render_markdown(f"{template_name}/{render_regex}", render_regex.split(".")[0]))

    content = content.replace("@Timestamp", str(datetime.now().timestamp().__round__()))

    fout = open(f"webserver/templates/{template_name}.html", "w", encoding="utf-8")
    fout.write(content)

def main():
    build_template("court")
    build_template("court2")
    pass

if __name__ == "__main__":
    main()