from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Seo():
    """Seo crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def Keyword_Researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['Keyword_Researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def Content_Optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['Content_Optimizer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def Product_Page_Enhancer(self) -> Agent:
        return Agent(
            config=self.agents_config['Product_Page_Enhancer'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def Backlink_Strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['Backlink_Strategist'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def Keyword_Discovery(self) -> Task:
        return Task(
            config=self.tasks_config['Keyword_Discovery'], # type: ignore[index]
        )

    @task
    def Homepage_and_Category_Optimization(self) -> Task:
        return Task(
            config=self.tasks_config['Homepage_and_Category_Optimization'], # type: ignore[index]
            output_file='report.md'
        )

    @task
    def Product_Page_Copy_Enhancement(self) -> Task:
        return Task(
            config=self.tasks_config['Product_Page_Copy_Enhancement'], # type: ignore[index]
            output_file='report.md'
        )

    @task
    def Backlink_Outreach_Planning(self) -> Task:
        return Task(
            config=self.tasks_config['Backlink_Outreach_Planning'], # type: ignore[index]
            output_file='report.md'
        )
      
    @crew
    def crew(self) -> Crew:
        """Creates the Seo crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
