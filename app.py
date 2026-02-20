import streamlit as st
import re

st.set_page_config(page_title="Code Commenter for Beginners", layout="centered")

st.title("🧠 Code Commenter for Beginners")
st.write("Paste your confusing code below and get simple English explanations.")

code_input = st.text_area("Paste Your Code Here:", height=300)

def explain_line(line):
    stripped = line.strip()

    if stripped.startswith("import"):
        return "This line imports a library so we can use its features."

    elif stripped.startswith("from"):
        return "This line imports a specific part of a library."

    elif stripped.startswith("def"):
        return "This line defines a function (a reusable block of code)."

    elif stripped.startswith("class"):
        return "This line defines a class (a blueprint for creating objects)."

    elif "=" in stripped and "==" not in stripped:
        return "This line stores a value inside a variable."

    elif "==" in stripped:
        return "This line checks if two values are equal."

    elif stripped.startswith("if"):
        return "This line checks a condition. If it's true, the code below runs."

    elif stripped.startswith("elif"):
        return "This checks another condition if the previous one was false."

    elif stripped.startswith("else"):
        return "This runs if none of the above conditions were true."

    elif stripped.startswith("for"):
        return "This line starts a loop that repeats for each item."

    elif stripped.startswith("while"):
        return "This loop runs again and again until the condition becomes false."

    elif stripped.startswith("return"):
        return "This sends a result back from a function."

    elif stripped.startswith("print"):
        return "This shows output on the screen."

    elif stripped.startswith("#"):
        return "This is already a comment in the code."

    elif stripped == "":
        return ""

    else:
        return "This line performs an operation or instruction."

if st.button("Add Simple Comments"):
    if code_input.strip() == "":
        st.warning("Please paste some code first.")
    else:
        lines = code_input.split("\n")
        commented_code = ""

        for line in lines:
            explanation = explain_line(line)
            if explanation:
                commented_code += f"{line}  # {explanation}\n"
            else:
                commented_code += "\n"

        st.subheader("✨ Commented Code")
        st.code(commented_code, language="python")

        st.download_button(
            label="Download Commented Code",
            data=commented_code,
            file_name="commented_code.py"
        )