# Generative-AI
**Team Name:**

DataTech Pioneers

**List of Team Members:**

Mahesh Gudla

Srinivas Peeka

Sai Vamshi Krishna Gajji


**Title of the Project:**

PDF Image Extractor and Analyzer


**Project Idea:**

PDF Image Extractor and Analyzer aims to develop an advanced system that automates the extraction of images from PDF documents and provides detailed analysis of these images using AI. The project leverages Python libraries for image extraction and utilizes the LangChain library along with LLaVa via Ollama for image explanation and analysis.

**Key Features:**

Image Extraction from PDF: Utilize Python tools to efficiently extract images from PDF documents.
Image Information Retrieval: Gather metadata and other relevant information about the extracted images.
AI-Driven Image Analysis: Use LLaVa via Ollama to analyze and provide insights about the images.
User-Friendly Interface: Develop an intuitive interface for users to upload PDFs and view extracted image information.
Multi-Format Support: Ensure compatibility with various PDF formats and types of images.
Impact and Applications: This tool will be beneficial for researchers, educators, and professionals who need to analyze and interpret images embedded in PDF documents. It can be applied in academic research, legal document review, and digital archiving, enhancing productivity and accuracy in handling image-rich PDF files.

# Description

**Tools and Technologies**

For this project, we plan to use the following tools and technologies:

Python - The primary programming language for scripting and automation.
Unstructured - A Python library for extracting information from various document formats.
LangChain - A library for building applications with large language models.
Ollama - An AI platform for integrating and managing AI services.
Llava - A tool for visual understanding, specifically for explaining images.
Jupyter Notebook - For interactive development and testing of code.
Matplotlib - For creating visualizations and flowcharts.
Pandas - For data manipulation and analysis.

**Explanation of the Diagram**

Start:
The process begins.


PDF Input:
The PDF document is provided as input.


Pass PDF into partition_pdf:
The PDF is processed using the partition_pdf function from the Unstructured library to divide it into its components.


Extract Image Information:
Image information (such as metadata) is extracted from the PDF.


Extract Image and Image Information:
The actual images and additional information are extracted from the PDF.

Explain Image using Llava via Ollama and LangChain:
The extracted images are passed to the Llava tool via Ollama and LangChain to get a detailed explanation or analysis of the images.


End:
The process completes.

**Implementation Steps**

Setup Environment:
Install necessary libraries (unstructured, langchain, ollama, llava, matplotlib, pandas).
Set up a Jupyter Notebook for development.


Load PDF:
Write a script to load the PDF document using a library like PyPDF2 or pdfminer.


Partition PDF:
Use the partition_pdf function from the Unstructured library to break down the PDF into its components (text, images, etc.).


Extract Image Information:
Extract metadata and other relevant information about the images present in the PDF.


Extract Images:
Extract the actual images from the PDF and save them to a temporary directory.


Analyze Images with Llava:
Pass the extracted images to Llava via Ollama and LangChain.
Retrieve detailed explanations or analyses for each image.


Visualize Process:
Create visualizations to depict the flow of data and the operations performed at each step.
Use Matplotlib to generate the flowchart.


Review and Validate
Validate the extracted and analyzed data to ensure accuracy.
Review the process for any possible improvements or optimizations.


Document the Process:
Document each step of the implementation process.
Prepare a detailed report on the findings and results.


Deploy and Maintain:
Deploy the solution as a script or a service.
Maintain and update the solution as necessary based on feedback and new requirements.


**References**

https://unstructured.io/

https://unstructured-io.github.io/unstructured/index.html

https://docs.unstructured.io/api-reference/api-services/python-sdk
