# Car Feature Comparison Tool

This project is a **AI based Streamlit-based application** that helps customers compare the features of two cars. By leveraging an AI-powered agent, the tool provides detailed comparisons, including tables of differences, commonalities, cons, recall trends, and financial options like interest rates and lease terms. This user-friendly application is designed to assist customers of all ages in making informed car-buying decisions.

---

## Features

- **AI-Powered Comparisons**: Uses the Groq model and DuckDuckGo API for real-time feature extraction and comparison.
- **Comprehensive Information**: Generates tables showcasing differences, commonalities, and cons of selected cars.
- **Recall Trends**: Provides insights into the recall history of car models.
- **Financial Options**: Displays interest rates and lease options for better financial decision-making.
- **Streamlit Interface**: Interactive and easy-to-use interface for seamless user experience.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/car-comparison-tool.git
   cd car-comparison-tool
   ```

2. **Set Up Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate # For Linux/Mac
   env\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project directory and add your required environment variables.

---

## Usage

1. **Run the Application**:
   ```bash
   streamlit run Agent.py
   ```

2. **Enter Car Details**:
   - Input the brand and model of two cars in the sidebar.
   - Click "Compare Cars" to generate the comparison.

3. **View Results**:
   - The app displays a detailed comparison table and other insights in the main content area.

---

## Technology Stack

- **Python**: Core programming language.
- **Streamlit**: Framework for creating interactive web applications.
- **PHI Agent**: AI-powered tool for car feature comparison.
- **Groq Model**: Versatile language model for extracting and generating insights.
- **DuckDuckGo API**: For real-time web data retrieval.

---

## Folder Structure

```
car-comparison-tool/
|-- Agent.py                 # Main application script
|-- requirements.txt       # Python dependencies
|-- .env                   # Environment variables (not included in repo)
|-- README.md              # Project documentation
```

---

## Contributions

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes. Ensure your code follows best practices and is properly documented.

---


## Acknowledgments

- **Streamlit**: For making web app development simple and accessible.
- **Groq Model and DuckDuckGo**: For providing robust AI and data retrieval capabilities.
---

## Contact

For questions, suggestions, or support, please contact:
- **Name**: Jabinbalan Ravinbalan
- **Email**: jabinbalanravinbalan@gmail.com

Happy Car Comparing!


