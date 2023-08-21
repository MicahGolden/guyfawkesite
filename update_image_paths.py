import os

# Specify the folder where your HTML files are located
html_folder = "GUYFAWKESITE"

# Specify the folder where your images are now located
image_folder = "Images"

# List all the HTML files in the specified folder
html_files = [file for file in os.listdir(html_folder) if file.endswith(".html")]

# Loop through each HTML file and update the image paths
for html_file in html_files:
    with open(os.path.join(html_folder, html_file), 'r') as f:
        content = f.read()

    # Update the image paths in the HTML content
    updated_content = content.replace('src="/', 'src="' + image_folder + '/')

    with open(os.path.join(html_folder, html_file), 'w') as f:
        f.write(updated_content)

print("Image paths updated successfully.")
