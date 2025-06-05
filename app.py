# AI Research Assistant: Multi-Agent System for Automating Web Research and Summarization (Streamlit Version)

import os
import requests
import cohere
import streamlit as st
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from serpapi import GoogleSearch

# Set your API keys here
COHERE_API_KEY = "your_api_key_here"
SERPAPI_KEY = "your_api_key"

co = cohere.Client(COHERE_API_KEY)

# 1. Search Agent
def search_web(query, num_results=5):
    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results
    })
    results = search.get_dict()
    links = [item['link'] for item in results.get('organic_results', [])][:num_results]
    return links

# 2. Scraper Agent
def scrape_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join(p.get_text() for p in paragraphs if len(p.get_text()) > 50)
        return content[:5000]  # limit input to Cohere
    except Exception as e:
        return f"Failed to scrape {url}: {e}"

# 3. Summarizer Agent
def summarize_text(text):
    if not text.strip():
        return "No content to summarize."
    try:
        response = co.summarize(
            text=text,
            length='medium',
            format='paragraph',
            model='command'
        )
        return response.summary
    except Exception as e:
        return f"Summarization error: {e}"

# 4. Writer Agent
def compile_report(topic, summaries):
    report = f"### AI Research Summary Report on '{topic}'\n\n"
    for idx, (url, summary) in enumerate(summaries.items(), start=1):
        domain = urlparse(url).netloc
        report += f"#### Source {idx}: {domain}\n"
        report += f"{summary}\n\n"
    return report

# Streamlit App
st.set_page_config(page_title="AI Research Assistant", layout="wide")
st.title("🤖 AI Research Assistant")
st.markdown("Automate your research using Cohere + SerpAPI")

query = st.text_input("Enter your research topic:")
num_links = st.slider("Number of sources to search:", 1, 10, 3)

if st.button("Generate Research Summary") and query:
    with st.spinner("🔍 Researching..."):
        urls = search_web(query, num_links)
        summaries = {}
        for url in urls:
            content = scrape_website(url)
            summary = summarize_text(content)
            summaries[url] = summary

        final_report = compile_report(query, summaries)

    st.subheader("📄 Final Report")
    st.markdown(final_report)

    with st.expander("🔗 Sources"):
        for url in urls:
            st.markdown(f"- [{urlparse(url).netloc}]({url})")
