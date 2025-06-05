# AI-Research-Assistant
This AI Agent can answer your query with Research, summarization and generate your answer.
AI Research Assistant – Multi-Agent System for Web Research & Summarization
The AI Research Assistant is a smart Streamlit web app that uses multiple agents to automate web research, scrape content, summarize it, and compile a well-organized research report. It's powered by Cohere's LLMs and SerpAPI for real-time internet search.

Features
Web Search Agent: Finds top relevant links using SerpAPI (Google Search)

Scraper Agent: Extracts content from web pages using BeautifulSoup

Summarizer Agent: Summarizes long content using Cohere’s command model

Writer Agent: Compiles all summaries into a clean, readable report

Outputs a final research report with source-wise breakdown

Powered By
Cohere LLM (command model) – for advanced summarization

SerpAPI – for real-time search result scraping

BeautifulSoup – to parse and extract text content from web pages

Streamlit – for building an interactive user interface

Libraries & Tools Used
streamlit – UI framework

cohere – NLP summarization

serpapi – Search automation

bs4 – Web scraping

requests, urllib.parse, os – Web & API handling
