

- Paper Analysis Task:
  Analyse the pdf document that has been provided by the user
  Agent: research_coordinator_agent

- Literatue Review Task:
  Look for similar research papers over the internet using the search internet tool and search arxiv tool. 
  Agent: literature_reviewer_agent

- New Idea Iderator Task: 
  Create a novel idea and solxwution based on the gaps identified by in the research paper, literure review done earlier. 
  Agent: new_idea_agent


Short Comings and Identified Issues

- In case the pdf is large the LLM might not be able to accomodate the token length. Possible solution to have a map function to reduce and summarise or distill the content length.
- Currently only looks at arxiv.org for similar papers and within that has only access to the summary. Will need to add more sorces of papers as mentioned.

