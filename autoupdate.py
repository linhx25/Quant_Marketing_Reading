import os
import glob

def generate_markdown_from_files(folder_path, markdown_path):
    # Get a list of all PDF files in the specified folder using glob
    pdf_files = glob.glob(os.path.join(folder_path, '**/*.pdf'), recursive=True)

    # Sort files by creation time
    sorted_files = sorted(pdf_files, key=os.path.getctime, reverse=True)

    # Initialize an empty dictionary to hold sub-folder titles and their paper titles
    subfolder_papers = {}

    # Extract sub-folder and titles from filenames
    for f in sorted_files:
        # Extract sub-folder and paper title from the file path
        subfolder = os.path.dirname(f).split('/')[-1]
        title = os.path.basename(f).split('.')[0]

        # Add to the dictionary
        if subfolder in subfolder_papers:
            subfolder_papers[subfolder].append(title)
        else:
            subfolder_papers[subfolder] = [title]

    # Write titles to markdown file
    with open(markdown_path, 'w') as md_file:
        for subfolder, titles in subfolder_papers.items():
            md_file.write(f"### {subfolder}\n")
            for title in titles:
                md_file.write(f"- {title}\n")
            md_file.write("\n")

if __name__ == '__main__':
    folder_path = '~reading'
    markdown_path = './most_recent.md'
    
    generate_markdown_from_files(folder_path, markdown_path)
