### README

#### Prerequisites

1. **Python**: Ensure you have Python installed.
2. **Jupyter Notebook**: Ensure you have Jupyter Notebook installed. You can install it via pip if you don't have it already.

#### Installation Steps

1. **Clone the Repository** (or download the notebook file):
   Download the Jupyter Notebook file to your local machine.

2. **Install Required Libraries**:
   Open a terminal or command prompt and run the following commands to install the required Python libraries:

   ```sh
   pip install langchain openai PyPDF2 faiss-cpu tiktoken PyDrive
   ```

#### Setup Instructions

1. **Open Jupyter Notebook**:
   Open a terminal or command prompt and navigate to the directory where you saved the notebook file. Start Jupyter Notebook by running:

   ```sh
   jupyter notebook
   ```

   This will open the Jupyter Notebook interface in your web browser.

2. **Open the Notebook**:
   In the Jupyter Notebook interface, navigate to and open the downloaded notebook file.

3. **Add Your OpenAI API Key**:
   Replace `{ADD KEY HERE}` with your OpenAI API key in the following line:

   ```python
   os.environ["OPENAI_API_KEY"] = "{ADD KEY HERE}"
   ```

   You can obtain your API key from the [OpenAI API keys page](https://platform.openai.com/account/billing/overview).

4. **Specify the Path to Your PDF Files**:
   Replace `{Path/To/Directory}` with the path to the directory containing your PDF files:

   ```python
   directory_path = '{Path/To/Directory}'
   ```

#### Running the Notebook

1. **Run All Cells**:
   In the Jupyter Notebook interface, select `Cell` > `Run All` to execute all the cells in the notebook. This will load your PDFs, extract text, generate questions, perform similarity searches, and generate detailed reports.

2. **View Results**:
   The notebook will print the summaries and detailed reports generated from the PDF documents in the output cells.

#### Notes

- Ensure your PDF files are accessible and readable.
- If you encounter any issues, check the output for error messages and ensure all dependencies are installed correctly.
- This notebook requires internet access to communicate with the OpenAI API.
