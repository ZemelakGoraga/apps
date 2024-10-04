import streamlit as st
import requests

# Function to call the OpenAI API
def get_chatgpt_response(prompt):
    api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return "Error: Unable to fetch response from ChatGPT."

def load_data():
    with open("top_tv_products.txt", "r") as f:
        data = f.readlines()
    return data

def main():
    st.title("Consumer Trends Pulse App")
    st.header("Top 5 Most Liked Market Products in the Television Category")
    
    data = load_data()
    
    for product in data:
        st.write(product)

    category = st.text_input("Enter a product category (e.g., Smartphones, Laptops):")
    
    if category:
        prompt = f"Identify the top 5 most liked market products within the {category} category in the United States over recent years."
        response = get_chatgpt_response(prompt)
        st.write("ChatGPT Response:")
        st.write(response)

if __name__ == "__main__":
    main()
