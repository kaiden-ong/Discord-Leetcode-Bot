import discord
import os
from dotenv import load_dotenv
load_dotenv()
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class MyClient(discord.Client):
    
    async def on_ready(self):
        # print(f'Logged on as {self.user}!')
        base_url_1 = 'https://leetcode.com/problemset/all/?page='
        base_url_2 = '&listId=wpwgkgt'
        # page_source = driver.page_source
        # soup = BeautifulSoup(page_source, 'html.parser')
    
        problem_urls = []
        # try:
        #     for i in range(1, 3):
        # url = f'{base_url_1}{1}{base_url_2}'
        # url = 'https://leetcode.com/problemset/all/?page=1&listId=wpwgkgt'

        # anchor_elements = driver.find_elements(By.TAG_NAME, 'a')
        # for anchor in anchor_elements:
        #     href = anchor.get_attribute("href")
        #     if href and '/problems/' in href and '/solution' not in href:
        #         problem_urls.append(href)
        # for url in problem_urls:
        #     print(url)
        # unique = set(problem_urls)
        # print(len(unique))
        # driver.quit()

        data = {"operationName":"questionData","variables":{"titleSlug":"two-sum"},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}

        r = requests.post('https://leetcode.com/graphql', json = data).json()
        soup = BeautifulSoup(r['data']['question']['content'], 'lxml')
        title = r['data']['question']['title']
        description =  soup.get_text().replace('\n',' ')
        problem = '\n'.join([title, description])
        formatted_problem = f'```python\n{problem}\n```'
        print(f'<@&1119381537750778027> Quick Solve This Problem!{formatted_problem}')
        
        # for div in div_elements:
            # Process the div element here
            # print(div.text)
                # anchor_elements = soup.find_all("a")
                # for anchor in anchor_elements:
                #     href = anchor.get("href")
                #     if href is not None and href.startswith("/problems/"):
                #         problem_links.append(href)
        # problem_cells = []
        # for rowgroup in soup.find_all("div", attrs={"role": "rowgroup"}):
        #     rows = rowgroup.find_all("div", attrs={"role": "row"})
        #     for row in rows:
        #         cells = row.find_all("div", attrs={"role": "cell"})
        #         if len(cells) > 1:
        #             nested_divs = cells[1].find_all("div")
        #             print(nested_divs)
        #             anchor = nested_divs[-1].find("a")
        #             if anchor is not None:
        #                 problem_links.append(anchor["href"])
        # print(len(problem_links))

    async def on_message(self, message):
        bot_rid = '<@1119380416521064558>'
        print("Message received:", message.content)

        if message.author != client.user:
            if client.user.mentioned_in(message) and '!check' in message.content:
                    async for previous in message.channel.history(limit=2):
                        if previous != message:
                            code = previous.content
                            code = code.strip('|`')
                            print(code)
                        # test_cases = {
                        #     "Example 1": ({"nums": [2, 7, 11, 15], "target": 9}),
                        #     "Example 2": ({"nums": [3, 2, 4], "target": 6}),
                        #     "Example 3": ({"nums": [3, 3], "target": 6})
                        # }

                        # expected_outputs = {
                        #     "Example 1": [0, 1],
                        #     "Example 2": [1, 2],
                        #     "Example 3": [0, 1]
                        # }
                            test_cases = {
                                "Example 1": 'hello',
                                "Example 2": 'hi',
                                "Example 3": 'hola'
                            }
                            expected_outputs = {
                                "Example 1": 'ello',
                                "Example 2": 'i',
                                "Example 3": 'ola'
                            }
                            try:
                                outputs = {}
                                exec(code, globals(), outputs)

                                for example, expected_output in expected_outputs.items():
                                    if outputs.get(example) == expected_output:
                                        print(f"Output is correct for {example}")
                                    else:
                                        print(expected_output, outputs.get(example))
                                        print(f"Output is incorrect for {example}")
                            except Exception as e:
                                await message.channel.send(f'Error occurred: {str(e)}')
                        #     # Iterate over the test cases and check the output
                        #     for case_name, case_input in test_cases.items():
                        #         variables = case_input
                        #         expected_output = expected_outputs[case_name]

                        #         # Extract the variable names and values from the test case
                        #         variable_names = list(variables.keys())
                        #         variable_values = list(variables.values())

                        #         # Pass the variable values as arguments to the user's code
                        #         user_output = twoSum(*variable_values)
                        #         if user_output == expected_output:
                        #             await message.channel.send(f'{case_name}: Output is correct!')
                        #         else:
                        #             await message.channel.send(f'{case_name}: Output is incorrect.')
                            # except Exception as e:
                            #     # If an error occurs, send an error message
                            #     await message.channel.send(f'Error occurred: {str(e)}')
                            

                            # if outputs == expected_outputs:
                            #     print(output)
                            #     await message.channel.send('Output is correct!')
                            # else:
                            #     print(output)
                            #     await message.channel.send('Output is incorrect.')
                # else:
                #     url = 'https://leetcode.com/problems/two-sum/'
                #     response = requests.get(url)
                #     soup = BeautifulSoup(response.content, 'html.parser')
                #     title = soup.find('span', class_='mr-2').text.strip()
                #     description = soup.find('div', class_='_1l1MA').text.strip()
                #     problem = '\n'.join([title, description])
                #     formatted_problem = f'```python\n{problem}\n```'
                #     print(formatted_problem)
                #     await message.channel.send(f'<@&1119381537750778027> Quick Solve This Problem!{formatted_problem}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))