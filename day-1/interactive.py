"""
Interactive Personal Agent Twin 

"""

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# ==============================================================================
# Configure the LLM
# ==============================================================================

gemini_api_key = os.getenv("GEMINI_API_KEY")
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=gemini_api_key,
    temperature=0.7,
)
# Create your Personal Agent Twin
# ==============================================================================

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

My favorite food is **Ethiopian Injera** and I love to play tennis and I love to workout too. I also love good food as well and I love my girlfriend. I'm Male 21.
---

**Would you like me to refine this into a formal bio for a professional portfolio, or perhaps expand on the "innovator" persona for a personal website?**
    """,
    
    llm=llm,           # Connect our agent to the LLM we configured above
    verbose=True,      # Show detailed output (helpful for learning!)
)
# ==============================================================================
# Interactive Chat Function
# ==============================================================================

def chat_with_twin():
    """Run an interactive chat session with your agent twin"""
    
    print("\n" + "="*70)
    print("🤖 Interactive Personal Agent Twin")
    print("="*70)
    print("\nAsk me anything about myself! Type 'quit', 'exit', or 'bye' to end.\n")
    
    while True:
        # Get user input
        question = input("❓ You: ").strip()
        
        # Check if user wants to quit
        if question.lower() in ['quit', 'exit', 'bye', 'q']:
            print("\n👋 Thanks for chatting! Goodbye!\n")
            break
        
        # Skip empty questions
        if not question:
            continue
        
        # Create a task for this specific question
        task = Task(
            description=f"Answer this question about me: {question}",
            expected_output="A clear, friendly answer",
            agent=my_agent_twin,
        )
        
        # Create a crew and run it
        crew = Crew(
            agents=[my_agent_twin],
            tasks=[task],
            verbose=False,  # Clean output
        )
        
        # Get the response
        print("\n🤖 Agent Twin: ", end="", flush=True)
        result = crew.kickoff()
        print(f"{result}\n")

# ==============================================================================
# Run the Interactive Chat
# ==============================================================================

if __name__ == "__main__":
    try:
        chat_with_twin()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        print("Make sure your .env file is set up with a valid OPENAI_API_KEY!\n")

