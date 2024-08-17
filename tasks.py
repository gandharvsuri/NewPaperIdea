from crewai import Task
from textwrap import dedent

class NewPaperIdeaTasks:
	def paper_analysis(self, agent, paper_content, keywords):
		return Task(description=dedent(f"""\
			Analyze the given research paper content: {paper_content}.
			Extra keywords provided: {keywords}.

			Focus on identifying novelty, benefits, meathodology,
			data, results and short comings.

			Your final report should clearly articulate the
			ideas's key points, data used, methods used and next steps.

			Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.
			"""),
			agent=agent
		)

	def literature_review(self, agent, paper_content, keywords):
		return Task(description=dedent(f"""\
			Find similar research papers to: {paper_content}.
			Extra keywords provided: {keywords}.

			Identify the top 3 similar research papers and analyze their
			ideas, data, results, and short comings.

			Your final report MUST include BOTH all context about original paper
			and a detailed comparison to the other similar papers.
			"""),
			agent=agent
		)

	def new_idea_iderator(self, agent):
		return Task(description=dedent("""\
			Craft an novel research problem and solution for a 
			research domain.
			The solution should be concise, include all context, data, 
			and meathods to achieve the solution.

			Focus on giving reasoning based on existing papers that 
			this idea fills in a gap. It must give several existing 
			paper citations and a paragraph reasoning why this is novel and valuable.

			"""),
			agent=agent
		)

	

	def review_research_idea(self, agent):
		return Task(description=dedent(f"""\
			Review the research problem ideas you got from the Research Idea Ideator.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying question or delegate follow up work if
			necessary to make decisions. When delegating work send the full draft
			as part of the information.

			Reasoning based on existing papers that this idea fills in a gap. 
			Note that it must give several existing paper citations and a paragraph 
			reasoning why this is novel and valuable.
			"""),
			agent=agent
		)