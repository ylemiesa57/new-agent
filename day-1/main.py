"""
Personal Agent Twin - A simple CrewAI example for students
============================================================

This script creates an AI agent that acts as your "digital twin" - 
an agent that knows about you and can answer questions on your behalf.

Students: Edit the BACKSTORY section to create your own personal agent!
"""

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==============================================================================
# STEP 1: Configure your LLM (Language Model)
# ==============================================================================
# This is the "brain" of your agent. You can use OpenAI or Gemini.
# 
# Option 1: OpenAI (default)
# - Set OPENAI_API_KEY in .env file
# - Get key at: https://platform.openai.com/api-keys
#
# Option 2: Gemini
# - Set GEMINI_API_KEY in .env file  
# - Get key at: https://aistudio.google.com/apikey
# - Available models: gemini-2.5-pro, gemini-1.5-pro, gemini-1.5-flash

import os

# Option 1: Using OpenAI (default)
# llm = LLM(
#     model="openai/gpt-4o-mini",  # The AI model to use
#     temperature=0.7,              # Controls creativity (0.0 = focused, 1.0 = creative)
# )

# Option 2: Using Gemini (uncomment to use instead of OpenAI)
gemini_api_key = os.getenv("GEMINI_API_KEY")
llm = LLM(
    model="gemini/gemini-2.5-flash",  # Fast and efficient model (gemini-1.5-flash not available, using 2.5-flash)
    # model="gemini/gemini-flash-latest",  # Alternative: latest flash model alias
    # model="gemini/gemini-2.0-flash",     # Alternative: older flash version
    # model="gemini/gemini-2.5-pro",       # More capable but slower
    api_key=gemini_api_key,
    temperature=0.7,
)


# ==============================================================================
# STEP 2: Create your Personal Agent Twin
# ==============================================================================
# This is where you define WHO your agent is and WHAT it knows about you.
# 
# ✏️ STUDENTS: EDIT THIS SECTION TO MAKE IT YOUR OWN!
# Change the backstory to reflect YOUR interests, personality, and background!

my_agent_twin = Agent(
    role="Personal Digital Twin",
    
    goal="Answer questions about me accurately and helpfully",
    
    # 👇 EDIT THIS BACKSTORY - Make it about YOU!
    backstory="""
    To create a compelling backstory for you, I’ve woven together your roots in Ethiopia, your rigorous journey through MIT, and your drive toward a high-stakes future in tech and finance.

## The Architect of Systems: A Backstory

### Roots and Transitions

Born in the highlands of **Ethiopia**, your journey began with a massive leap across the globe at just three years old. Growing up in the U.S. (with roots trailing back to **Silver Spring, Maryland**), you carried a dual perspective: the cultural depth of your heritage—maintained through your dedication to learning **Tigrinya**—and the relentless "American Dream" drive to build something from nothing.

### The MIT Crucible

By 2024, you found yourself in the heart of Cambridge, navigating the halls of **MIT**. You didn't just study; you built. Your desk became a graveyard of silicon and code, ranging from **FPGA-controlled autonomous cars** to **RISC-V processors**. You bridged the gap between the physical and the digital, working on everything from robotic straps at the **d’Arbeloff Laboratory** to complex **AI RAG pipelines for NASA JPL**.

Your academic path was never just about a degree; it was a strategic roadmap. With an undergraduate finish line in 2027 and a Master’s in 2028, you positioned yourself at the intersection of **Machine Learning**, **Robotics**, and **Quantum Modeling**.

### The Quant and the Creator

While others focused solely on code, you looked at the "system" of life. You co-authored research on how **AI shapes cyber risk**, dived deep into the mechanics of **stock trading strategies**, and set a bold marker for your future: a **million-dollar net worth by age 26**. This wasn't about greed; it was about the freedom to innovate. Whether it was building **DeuceVision** for tennis analytics or **EmbraceAI** for mental health support, your projects always sought to solve a human problem using high-level technical precision.

### The Path Ahead

As 2026 unfolds, you stand at a crossroads of major milestones. With a summer internship at **Bloomberg** on the horizon and your **21st birthday** just days away, the "student" phase is rapidly evolving into the "architect" phase. Beyond the lab, you are a traveler—scouting the nightlife in **Porto**, surfing, and planning for a future that includes both global impact and a committed life with the person you love.

---

**Would you like me to refine this into a formal bio for a professional portfolio, or perhaps expand on the "innovator" persona for a personal website?**
    """,
    
    llm=llm,           # Connect our agent to the LLM we configured above
    verbose=True,      # Show detailed output (helpful for learning!)
)


# ==============================================================================
# STEP 3: Create a Task for your Agent
# ==============================================================================
# Tasks tell your agent WHAT to do. This task answers questions about you.

answer_question_task = Task(
    description="""
    Answer the following question about me: {question}
    
    Use the information from your backstory to provide an accurate,
    friendly, and helpful response. If you don't know something,
    say so honestly rather than making it up.
    """,
    
    expected_output="A clear, friendly answer to the question about me",
    
    agent=my_agent_twin,  # Assign this task to our agent
)


# ==============================================================================
# STEP 4: Create a Crew (Team of Agents)
# ==============================================================================
# A Crew manages your agents and tasks. Even with one agent, we need a Crew!

my_crew = Crew(
    agents=[my_agent_twin],           # List of agents (just one for now)
    tasks=[answer_question_task],     # List of tasks to complete
    verbose=True,                     # Show detailed execution logs
)


# ==============================================================================
# STEP 5: Run your Agent Twin!
# ==============================================================================
# This is where the magic happens - we "kickoff" the crew to complete the task.

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🤖 Personal Agent Twin - Ready to answer questions about you!")
    print("="*70 + "\n")
    
    # Example questions you can ask your agent twin
    # 👇 STUDENTS: Try different questions or make it interactive!
    
    question = "What are my interests and what am I learning?"
    
    print(f"❓ Question: {question}\n")
    
    # Run the crew with the question as input
    result = my_crew.kickoff(inputs={"question": question})
    
    print("\n" + "="*70)
    print("✅ Agent Response:")
    print("="*70)
    print(result)
    print("\n")
    
    
