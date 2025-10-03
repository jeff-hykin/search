from browser_use_sdk import BrowserUse

client = BrowserUse(
    # api_key="bu_..."
)
task = client.tasks.create_task(
    task="Search for the top 10 Hacker News posts and return the title and url.",
    llm="gpt-4.1"
)
result = task.complete()
print(f'''result.output = {result.output}''')