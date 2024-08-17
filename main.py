from agents import NewPaperIdeaAgents
from tasks import NewPaperIdeaTasks
from crewai import Crew
from dotenv import load_dotenv
from tools.pdf_reader import read_pdf
load_dotenv()


tasks = NewPaperIdeaTasks()
agents = NewPaperIdeaAgents()

research_paper_path = "3624732.pdf"
keywords = "Natural Language Processing, NLP, Attention, Self-Attention"

paper_content = read_pdf(research_paper_path)

# Create Agents
research_coordinator_agent = agents.research_coordinator_agent()
literature_reviewer_agent = agents.literature_reviewer_agent()
research_domain_agent = agents.research_domain_agent()
new_idea_agent = agents.new_idea_agent()

# Create Tasks
paper_analysis = tasks.paper_analysis(
    research_coordinator_agent, paper_content, keywords)
literature_review = tasks.literature_review(
    literature_reviewer_agent, paper_content, keywords)
new_idea_iderator = tasks.new_idea_iderator(
    new_idea_agent)
review_research_idea = tasks.review_research_idea(research_domain_agent)

# Create Crew responsible for Copy
copy_crew = Crew(
    agents=[
        research_coordinator_agent,
        literature_reviewer_agent,
        research_domain_agent,
        new_idea_agent
    ],
    tasks=[
        paper_analysis,
        literature_review,
        new_idea_iderator,
        review_research_idea
    ],
    verbose=True,
    # Remove this when running locally. This helps prevent rate limiting with groq.
    max_rpm=1
)

new_idea_copy = copy_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(new_idea_copy)
