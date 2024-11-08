import os
import re


directory = "."

img_pattern = r"<img\b[^>]*>"

placeholder_img_tag = '<img src="https://media1.tenor.com/m/m08ZsYu5P8kAAAAd/pedro-raccoon-raccoon.gif">'


for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)


        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()


        modified_content = re.sub(img_pattern, placeholder_img_tag, content)


        with open(filepath, "w", encoding="utf-8") as file:
            file.write(modified_content)


        print(f"{filename} has been updated and <img> tags have been replaced")

