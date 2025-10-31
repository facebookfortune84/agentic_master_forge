import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FileReadTool
)






@CrewBase
class AgenticMastersGenesisForgeCrew:
    """AgenticMastersGenesisForge crew"""

    
    @agent
    def chief_language_architect(self) -> Agent:

        
        return Agent(
            config=self.agents_config["chief_language_architect"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def compiler_and_runtime_engineer(self) -> Agent:

        
        return Agent(
            config=self.agents_config["compiler_and_runtime_engineer"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def agent_forge_system_architect(self) -> Agent:

        
        return Agent(
            config=self.agents_config["agent_forge_system_architect"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def autonomous_agent_persona_engineer(self) -> Agent:

        
        return Agent(
            config=self.agents_config["autonomous_agent_persona_engineer"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def human_machine_interface_and_deployment_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["human_machine_interface_and_deployment_specialist"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def enterprise_security_and_compliance_analyst(self) -> Agent:

        
        return Agent(
            config=self.agents_config["enterprise_security_and_compliance_analyst"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def error_analyst_and_diagnostics_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["error_analyst_and_diagnostics_specialist"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def code_fixer_and_source_code_update_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["code_fixer_and_source_code_update_specialist"],
            
            
            tools=[
				FileReadTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="groq/llama-3.1-8b-instant",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def design_the_code_specification(self) -> Task:
        return Task(
            config=self.tasks_config["design_the_code_specification"],
            markdown=False,
            
            
        )
    
    @task
    def diagnose_system_error(self) -> Task:
        return Task(
            config=self.tasks_config["diagnose_system_error"],
            markdown=False,
            
            
        )
    
    @task
    def design_the_code_compiler_architecture(self) -> Task:
        return Task(
            config=self.tasks_config["design_the_code_compiler_architecture"],
            markdown=False,
            
            
        )
    
    @task
    def architect_agent_forge_core_system(self) -> Task:
        return Task(
            config=self.tasks_config["architect_agent_forge_core_system"],
            markdown=False,
            
            
        )
    
    @task
    def review_enterprise_security(self) -> Task:
        return Task(
            config=self.tasks_config["review_enterprise_security"],
            markdown=False,
            
            
        )
    
    @task
    def create_agent_identities(self) -> Task:
        return Task(
            config=self.tasks_config["create_agent_identities"],
            markdown=False,
            
            
        )
    
    @task
    def design_ar_vr_hil_environment(self) -> Task:
        return Task(
            config=self.tasks_config["design_ar_vr_hil_environment"],
            markdown=False,
            
            
        )
    
    @task
    def create_deployment_package(self) -> Task:
        return Task(
            config=self.tasks_config["create_deployment_package"],
            markdown=False,
            
            
        )
    
    @task
    def document_agent_forge_portability(self) -> Task:
        return Task(
            config=self.tasks_config["document_agent_forge_portability"],
            markdown=False,
            
            
        )
    
    @task
    def generate_code_fix(self) -> Task:
        return Task(
            config=self.tasks_config["generate_code_fix"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AgenticMastersGenesisForge crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
