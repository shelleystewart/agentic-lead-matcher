import streamlit as st
from openai import OpenAI
import json

# 1. Point to your local Ollama server
# Ollama provides an OpenAI-compatible API out of the box at port 11434
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Ollama doesn't require a real key, but the SDK expects a string
)

# 2. Mock Real Estate Database (Palm Paradise Realty Group style)
PROPERTIES_DB = [
    {"id": 1, "city": "Fort Myers", "beds": 3, "baths": 2, "price": 420000, "features": "Pool, close to beach, quiet neighborhood"},
    {"id": 2, "city": "Cape Coral", "beds": 4, "baths": 3, "price": 550000, "features": "Waterfront canal access, modern kitchen"},
    {"id": 3, "city": "Fort Myers", "beds": 2, "baths": 2, "price": 310000, "features": "Gated community, low maintenance, garage"},
    {"id": 4, "city": "Fort Myers", "beds": 4, "baths": 2.5, "price": 495000, "features": "Large backyard, updated roof, family-friendly"},
]

# Streamlit UI Setup
st.title("🌴 Local Real Estate Agent (Powered by Ollama)")
st.write("Running a multi-agent workflow completely locally on your machine.")

# Input for the raw lead data
lead_input = st.text_area(
    "Enter Lead Note:", 
    value="Sarah Jenkins is looking for a 3 or 4 bedroom house in Fort Myers. Her budget maxes out at $500,000."
)

if st.button("Run AI Agent Workflow"):
    with st.spinner("Agent 1 is scanning local inventory..."):
        # --- AGENT 1: THE FILTERING AGENT ---
        agent_1_prompt = f"""
        You are a Real Estate Inventory Specialist Agent. Your job is to look at the client request and select the best matching properties from our database.
        
        Client Request: {lead_input}
        Available Database: {json.dumps(PROPERTIES_DB)}
        
        Return ONLY the raw JSON list of matching properties. Do not include conversational text, introduction, or markdown code blocks.
        """
        
        response_1 = client.chat.completions.create(
            model="llama3.2:1b",  # Updated to the lightweight version
            messages=[{"role": "user", "content": agent_1_prompt}],
            temperature=0.1
        )
        matched_properties = response_1.choices[0].message.content
        
        st.subheader("🤖 Agent 1 (Inventory Specialist) Output:")
        st.code(matched_properties, language="json")

    with st.spinner("Agent 2 is drafting the email..."):
        # --- AGENT 2: THE WRITER AGENT ---
        agent_2_prompt = f"""
        You are an Expert Real Estate Copywriter Agent working for Palm Paradise Realty Group. 
        Take the following matched properties and draft a warm, highly professional email to the client.
        Make sure to highlight why these specific properties fit their criteria.
        
        Original Lead Info: {lead_input}
        Matched Listings: {matched_properties}
        
        Draft the email now:
        """
        
        response_2 = client.chat.completions.create(
            model="llama3.2:1b", # Updated to the lightweight version
            messages=[{"role": "user", "content": agent_2_prompt}],
            temperature=0.7
        )
        final_email = response_2.choices[0].message.content
        
        st.subheader("📝 Agent 2 (Copywriter) Drafted Email:")
        st.markdown(final_email)