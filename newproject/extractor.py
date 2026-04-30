import json
from browser_use import Agent, Browser, BrowserConfig, Controller
from models import FacultyData
from config import PROGRESS_FILE

results = []

controller = Controller()

@controller.action("Save faculty data")
def save_faculty(data: FacultyData):
    results.append(data.model_dump())
    return f"Saved {data.name}"


def load_progress():
    try:
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    except:
        return {"completed": [], "results": []}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


async def scrape_university(url, name, llm):

    browser = Browser(config=BrowserConfig(
    headless=False
    ))

    task = f"""
1. Go to {url}
2. Wait until page loads completely
3. Find faculty directory or people section
4. Click on first professor profile
5. Extract:
   - Name
   - Email
   - Title
   - Research areas
6. Save using controller
7. Go back and repeat for 3 professors
"""

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        controller=controller
    )
    import logging
    logging.basicConfig(level=logging.INFO)

    await agent.run()
    await browser.close()

    progress = load_progress()
    progress["completed"].append(name)
    progress["results"].extend(results)
    save_progress(progress)

    return results