import streamlit as st

# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

# Streamlit app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for operation selection
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
<<<<<<< HEAD

import streamlit as st
=======
   import streamlit as st
>>>>>>> fe6d9576ba806d277fb248f5075d6bf3d617e30a

# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

# Streamlit app
st.title("Simple Calculator")

# Input fields for numbers with unique keys
num1 = st.number_input("Enter first number", value=0.0, key="num1")
num2 = st.number_input("Enter second number", value=0.0, key="num2")

# Dropdown for operation selection
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"], key="operation")

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.write(f"Result: {result}")

