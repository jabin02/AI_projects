import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the agent
car_comparison_agent = Agent(
    name="Car Feature Comparison Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Extract car features and compare them.",
        "Generate a simple table for the differences and commonalities.",
        "List cons or problems with each car.",
        "State which year model is recalled most",
        "Generate a simple table for interest rates and lease option"
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

def compare_car_features(brand1, model1, brand2, model2):
    query = f"Compare the features of {brand1} {model1} and {brand2} {model2}. Generate a table."
    try:
        # Get the response from the agent
        response = car_comparison_agent.run(query)
        # Convert the response to a dictionary and access its content
        response_content = response.to_dict()["content"]
        return response_content
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Car Feature Comparison Tool ")
st.write("Compare the features of two cars and get a detailed table of differences, commonalities, and cons.")

# Sidebar for inputs
with st.sidebar:
    st.header("Enter Car Details")
    brand1 = st.text_input("Enter the first car brand (e.g., Tesla):", "Tesla")
    model1 = st.text_input("Enter the first car model (e.g., Model S):", "Model S")
    brand2 = st.text_input("Enter the second car brand (e.g., BMW):", "BMW")
    model2 = st.text_input("Enter the second car model (e.g., X5):", "X5")
    submitted = st.button("Compare Cars")

# Main content area for results
if submitted:
    st.header("Comparison Results:")
    with st.spinner("Please wait..."):
        comparison_result = compare_car_features(brand1, model1, brand2, model2)
    if comparison_result.startswith("Error"):
        st.error(comparison_result)
    else:
        st.markdown(comparison_result)
