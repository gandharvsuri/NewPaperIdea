import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools


class NewPaperIdeaAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-8b-8192"
        )
        # self.llm = ChatOpenAI(
        #     model="crewai-llama3-8b",
        #     base_url="http://localhost:11434/v1",
        #     api_key="NA"
        # )

    def research_coordinator_agent(self):
        return Agent(
            role="Lead Research Coordinator",
            backstory=dedent(
                f"""Expert in conducting research, planning and logistics. 
                I have decades of expereince in conducting acadamic research, coming up with novel
                meathodologies and strategies to help clients students and peers achieve their goals."""),
            goal=dedent(f"""
                        Facilitate academic research with detailed plans,
                        include novelty, innovative and value tips.
                        """),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_arxiv
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def literature_reviewer_agent(self):
        return Agent(
            role="Literature Reviewer",
            backstory=dedent(
                f"""Expert in finding the relevant and related literature."""),
            goal=dedent(f"""
                        Select the relevant and related literature based on the provided research topic and research question.
                        """),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_arxiv
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def research_domain_agent(self):
        return Agent(
            role="Research Domain Expert",
            backstory=dedent(
                f"""Expert for a research domain. I have years of experience in conducting research and planning for research."""),
            goal=dedent(f"""
                        Provide relevant ideas and reviews for a research topic and domain.
                        """),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_arxiv
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def new_idea_agent(self):
        return Agent(
            role="Research Idea Ideator",
            backstory=dedent(
                f"""Expert in coming up with new ideas and research problems and solutions."""),
            goal=dedent(f"""
                        Provide relevant ideas and research problems to work on and provide solutions for them.
                        Provides data and methods to achieve and reseasoning based on existing papers that this idea fills in a gap.
                        """),
            tools=[
                SearchTools.search_internet,
                SearchTools.search_arxiv
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
