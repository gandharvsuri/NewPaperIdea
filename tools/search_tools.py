import json
import os

import requests
from langchain.tools import tool
import arxiv


class SearchTools():
  @tool("Search internet")
  def search_internet(query):
    """Useful to search the internet about a given topic and return relevant
    results."""
    return SearchTools.search(query)

  @tool("Search instagram")
  def search_instagram(query):
    """Useful to search for instagram post about a given topic and return relevant
    results."""
    query = f"site:instagram.com {query}"
    return SearchTools.search(query)

  def search(query, n_results=5):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    stirng = []
    for result in results[:n_results]:
      try:
        stirng.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    content = '\n'.join(stirng)
    return f"\nSearch result: {content}\n"

  @tool("Search ARXIV")
  def search_arxiv(query, n_results=5):
    """Useful to search arxiv for research papers of a given topic."""
    arxiv_client = arxiv.Client()
    search = arxiv.Search(
      query = query,
      max_results = n_results,
      sort_by = arxiv.SortCriterion.SubmittedDate
    )

    summary = ""
    for result in arxiv_client.results(search):
      summary = summary + result.summary + "\n"
      
    return f"Top {n_results} research papers summary \n {summary}"

