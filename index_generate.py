import os
import re 

def generate_index_html(womens_team_dir, mens_team_dir, output_file):
    # Initialize lists to hold the links for each team
    womens_links = []
    mens_links = []

    # Function to add links from a directory
    def add_links_from_directory(directory, team_name, links):
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                modified_filename = re.sub('[0-9]+\.html', '', filename)
                modified_filename = modified_filename.replace('_', ' ')
                
                link = f"<li><a href='{team_name}/{filename}'>{modified_filename}</a></li>"
                links.append(link)

    # Add links from both directories
    add_links_from_directory(womens_team_dir, 'womens_team', womens_links)
    add_links_from_directory(mens_team_dir, 'mens_team', mens_links)

     # Sort the links alphabetically
    womens_links.sort()
    mens_links.sort()

    # Create the index.html content
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/542a7b699c.js" crossorigin="anonymous"></script>
    <link rel = "stylesheet" href = "css/reset.css">
    <link rel = "stylesheet" href = "css/index.css">
    <title>Team HTML Files</title>
</head>
<body>
<a href = "#main" id = "skip">Skip to Main Content</a>

    <nav>
        <ul>
           <li><a href="index.html">Home Page</a></li>
           <li><a href="mens.html">Men's Team</a></li>
           <li><a href="womens.html">Women's Team</a></li>
        </ul>
    </nav>

    <header>
        <div id = "box">
            <h1>Cross Country Athletes Homepage</h1>
            <p>Find your favorite athletes below!</p> 
        </div>
    </header>

<main>

    <h2>Women's Team</h2>
    <ul>
        {}
    </ul>

    <h2>Men's Team</h2>
    <ul>
        {}
    </ul>
    </main>

    <footer>
        <p>
        Skyline High School<br>
        <address>
        2552 North Maple Road<br>
        Ann Arbor, MI 48103<br><br>

        <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
        <a href = "https://www.instagram.com/a2skylinexc/">Follow us on Instagram <i class="fa-brands fa-instagram" aria-label="Instagram"></i></a> 
    </footer>
</body>
</html>
""".format('\n'.join(womens_links), '\n'.join(mens_links))

    # Write the index.html file
    with open(output_file, 'w') as f:
        f.write(index_content)

if __name__ == "__main__":
    # Define the directories
    womens_team_dir = 'womens_team'
    mens_team_dir = 'mens_team'
    output_file = 'index.html'

    # Generate the index.html
    generate_index_html(womens_team_dir, mens_team_dir, output_file)
    print(f"Index file created at {output_file}")