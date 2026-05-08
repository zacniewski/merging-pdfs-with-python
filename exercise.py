import os
from pypdf import PdfWriter

def basic_merger(input_dir, output_file):
    """
    EXERCISE: Complete this function to merge all PDFs in input_dir into output_file.
    
    Hints:
    1. Create a PdfWriter object.
    2. Use os.listdir() to get files.
    3. Filter for '.pdf' files and sort them.
    4. Loop through files and use writer.append(path_to_file).
    5. Write the result to output_file and close the writer.
    """
    # TODO: Implement the merging logic here
    pass

if __name__ == "__main__":
    # Example usage (uncomment after implementation):
    # basic_merger("pdfs/", "exercise_result.pdf")
    print("Open exercise.py and implement basic_merger function!")
