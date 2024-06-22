from PyPDF2 import PdfReader
import pyttsx3


# Function to convert text to speech

def speak(text):
    """
       This function takes text as input and uses pyttsx3 to speak it aloud.
       It initializes the speech engine, sets the speech rate (optional), and speaks the text.

       Args:
           text (str): The text to be spoken.
       """
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()


# Function to convert PDF text to speech
def pdfText2Speech(pdf_path):
    """
       This function takes a PDF file path as input, extracts text using PyPDF2,
       and calls the speak function to convert the text to speech.

       Args:
           pdf_path (str): The path to the PDF file.

       Raises:
           Exception: If there's an error during PDF processing or text extraction.
       """
    try:
        # Extract text from the PDF
        text = extractPdfDataToText(pdf_path)
        print(text)
        # Speak the extracted text
        speak(text)

    except Exception as e:
        print("Failed to convert PDF to Speech:", str(e))


# Function to extract text data from a PDF and save it to a file
def extractPdfDataToFile(pdf_path):
    """
    This function takes a PDF file path as input, extracts text using PyPDF2,
    and saves it to a text file named "pdf_2_textFile" in the "./text/" directory.

    Args:
        pdf_path (str): The path to the PDF file.

    Raises:
        Exception: If there's an error during PDF processing or text extraction.
    """
    try:
        text = extractPdfDataToText(pdf_path)
        with open("./text/pdf_2_textFile", "w") as textFile:
            textFile.write(text)
        # Save the extracted text to a file
        print("We've successfully created text file with pdf data")

    except Exception as e:
        print("Failed to extract PDF data to file:", str(e))


# Function to extract text data from a PDF
def extractPdfDataToText(pdf_path):
    """
        This function takes a PDF file path as input, extracts text using PyPDF2,
        and returns the extracted text as a string.

        Args:
            pdf_path (str): The path to the PDF file.

        Returns:
            str: The extracted text content from the PDF file.

        Raises:
            Exception: If there's an error during PDF processing or text extraction.
        """
    try:
        # Open the PDF file in binary read mode
        with open(pdf_path, 'rb') as file:
            content = ""
            pdf = PdfReader(file)
            # Loop through each page in the PDF
            for pageNum in range(len(pdf.pages)):
                myPage = pdf.pages[pageNum]
                content += myPage.extract_text()
            # Return the extracted text content
            return content

    except Exception as e:
        raise f"Failed to extract text: {str(e)}"


# Main program execution block
if __name__ == '__main__':

    print("Welcome to Yash PDF service")
    print("""
    Which Service you required: 
    1. Pdf-2-Speech Pdf
    2. Pdf-2-Image Data
    3. Pdf data extractor
    4. Exit\n
    """)

    # Get user input for service choice
    res = int(input("Enter Your Choice: "))

    if res == 4:
        exit(0)

    # Handle different service choices
    if res == 3:
        pdfName = input("Enter your Pdf Name: ")
        content = extractPdfDataToText(f"./pdf/{pdfName}")
        print(content)

    elif res == 2:
        pdfName = input("Enter your Pdf Name: ")
        extractPdfDataToFile(f"./pdf/{pdfName}")

    elif res == 1:
        pdfName = input("Enter your Pdf Name: ")
        pdfText2Speech(f"./pdf/{pdfName}")

    else:
        print("You have entered invalid input! \n")
        exit(1)
