import asyncio
import csv
from extractor import scrape_university
from config import UNIVERSITIES, OUTPUT_CSV
from validator import is_valid_email, remove_duplicates
from langchain_openai import ChatOpenAI

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Test LLM (correct way)
def test_llm():
    response = llm.invoke("Hello")
    print(response.content)

print("Client initialized")
test_llm()


async def main():
    all_results = []

    for url, name in UNIVERSITIES:
        print(f"Scraping {name}...")
        data = await scrape_university(url, name, llm)
        all_results.extend(data)

    # Filter valid emails
    valid_data = [d for d in all_results if is_valid_email(d["email"])]

    # Remove duplicates
    final_data = remove_duplicates(valid_data)

    if not final_data:
        print("❌ No data extracted")
        return

    # Save CSV
    with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=final_data[0].keys())
        writer.writeheader()
        writer.writerows(final_data)

    print("✅ CSV saved successfully")


if __name__ == "__main__":
    asyncio.run(main())