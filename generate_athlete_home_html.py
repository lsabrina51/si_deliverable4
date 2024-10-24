import os
from bs4 import BeautifulSoup
import re 

def extract_image_from_html(file_path):
    """Extract the first image source from the given HTML file."""
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        img_tag = soup.find('img')
        if img_tag and img_tag.has_attr('src'):
            return img_tag['src']
    return None  # Return None if no image is found

def is_valid_image(image_src, base_path):
    """Check if the given image source points to a valid file in the specified base path."""
    # Construct the full path to the image
    #full_image_path = os.path.join(os.path.dirname(base_path), image_src)
    full_image_path = image_src
    print(full_image_path)
    return os.path.isfile(full_image_path)

def generate_homepage(folder_path='mens_team', output_file='mens.html'):
    # Set to store unique links
    links = set()

    # Iterate through the files in the specified folder
    for filename in os.listdir(folder_path):
        # Check for HTML files
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            image_src = extract_image_from_html(file_path)
            # Create a link with image if an image is found
            modified_string = re.sub('[0-9]+\.html', '', filename)
            
            mod_img_src = image_src.replace('../', '')

            if image_src and is_valid_image(mod_img_src, base_path = os.path.join(os.path.dirname(folder_path), mod_img_src)):
                links.add(f'<li><a href="{filename}">{modified_string}<br><img src="{image_src}" alt="{modified_string}" style="width:100px;height:auto;"></a></li>')
            else: 
                default = os.path.join(os.path.dirname(folder_path), "/images/profiles/default_image.jpg")
                print(modified_string)
                links.add(f'<li><a href="{filename}">{modified_string}<br><img src="{".."+default}" alt="{modified_string}" style="width:100px;height:auto;"></a></li>')

    # Sort the links alphabetically
    sorted_links = sorted(links)

    # Create the HTML content for the homepage
    homepage_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Women's Team Homepage</title>
</head>
<body>
    <h1>Welcome to the Women's Team Homepage</h1>
    <ul>
        {}
    </ul>
</body>
</html>
    '''.format('\n'.join(sorted_links))

    # Write the homepage content to the output file
    with open(os.path.join(folder_path, output_file), 'w') as file:
        file.write(homepage_content)

    print(f'Homepage created at {os.path.join(folder_path, output_file)}')

# Run the function with the default folder
generate_homepage()