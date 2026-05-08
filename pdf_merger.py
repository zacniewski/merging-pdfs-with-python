import os
from pypdf import PdfWriter


def merge_all_pdfs(path):
    """
    Merges all PDF files in the given directory into a single document.
    :param path: Path to directory with pdf documents
    :return: None
    """
    writer = PdfWriter()
    pdf_files = sorted([f for f in os.listdir(path) if f.lower().endswith('.pdf')])

    if not pdf_files:
        print(f"No PDF files found in {path}")
        return

    for filename in pdf_files:
        file_path = os.path.join(path, filename)
        writer.append(file_path)

    output_name = "Merged_pdfs_all.pdf"
    writer.write(output_name)
    writer.close()
    print(f"Successfully merged all PDFs into {output_name}")


def merge_groups_of_pdfs(path):
    """
    Generates single (larger) pdfs from groups of pdf files sharing the same prefix.
    Example: TypeA_01.pdf + TypeA_02.pdf -> TypeA.pdf
    :param path: path to directory with pdf documents
    :return: None
    """
    # Get and sort pdf files
    all_files = sorted([f for f in os.listdir(path) if f.lower().endswith('.pdf')])
    
    # Filter files that follow the naming convention Prefix_Number.pdf
    grouped_files = [f for f in all_files if check_if_number_after_underscore(f)]
    
    if not grouped_files:
        print("No grouped PDF files found (naming convention: Prefix_Number.pdf)")
        return

    current_prefix = None
    writer = None

    for i, filename in enumerate(grouped_files):
        prefix = get_prefix(filename)
        
        # If prefix changes, write current merger and start a new one
        if prefix != current_prefix:
            if writer:
                output_path = f"{current_prefix}.pdf"
                writer.write(output_path)
                writer.close()
                print(f"Created: {output_path}")
            
            writer = PdfWriter()
            current_prefix = prefix
        
        writer.append(os.path.join(path, filename))
        
        # Write the last group
        if i == len(grouped_files) - 1:
            output_path = f"{current_prefix}.pdf"
            writer.write(output_path)
            writer.close()
            print(f"Created: {output_path}")

    print("Finished merging pdf groups!")


def get_prefix(filename):
    """Extracts the prefix before the last underscore."""
    return filename.rsplit("_", 1)[0]


def check_if_number_after_underscore(file_name):
    """
    Checks if the filename follows 'Prefix_Number.pdf' pattern.
    """
    name_part = os.path.splitext(file_name)[0]
    if "_" not in name_part:
        return False
    
    suffix = name_part.rsplit("_", 1)[-1]
    return suffix.isdigit()


if __name__ == "__main__":
    folder_path = "pdfs/"
    if os.path.exists(folder_path):
        merge_groups_of_pdfs(folder_path)
    else:
        print(f"Directory '{folder_path}' not found.")
