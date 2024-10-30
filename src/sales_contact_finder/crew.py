from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class KinaseResearchInstitutionFinderCrew:
    """Kinase Research Institution Finder Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def institution_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["institution_finder"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config["data_collector"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def data_validator(self) -> Agent:
        return Agent(
            config=self.agents_config["data_validator"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def prioritizer(self) -> Agent:
        return Agent(
            config=self.agents_config["prioritizer"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def compiler(self) -> Agent:
        return Agent(
            config=self.agents_config["compiler"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def identify_institutions_task(self) -> Task:
        return Task(
            config=self.tasks_config["identify_institutions_task"],
            agent=self.institution_finder(),
        )

    @task
    def collect_institution_data_task(self) -> Task:
        return Task(
            config=self.tasks_config["collect_institution_data_task"],
            agent=self.data_collector(),
        )

    @task
    def validate_and_filter_task(self) -> Task:
        return Task(
            config=self.tasks_config["validate_and_filter_task"],
            agent=self.data_validator(),
        )

    @task
    def prioritize_institutions_task(self) -> Task:
        return Task(
            config=self.tasks_config["prioritize_institutions_task"],
            agent=self.prioritizer(),
        )

    @task
    def compile_results_task(self) -> Task:
        return Task(
            config=self.tasks_config["compile_results_task"],
            agent=self.compiler(),
            output_file="kinase_institutions_report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the KinaseResearchInstitutionFinder crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
