# AI Career Path Recommender :robot: :briefcase:

In our project, we focus on providing AI-driven features for everyday LinkedIn end-users, by creating an extension which recommends a career path to users. 
The suggested career path will be one of 10 pre-determined groups, and will be based on the user’s data (education, experience, personal, etc.).

In addition, as we know, one of the most important parameters when searching for a job is the salary. Thus, we will include the average salary of the recommended career path alongside the recommendation. 
This information will also allow the user to come to job interviews with an expected salary in mind.

## Contents
- [Running Instructions](#running-instructions)
  - [Project Notebook](#project-notebook)
  - [Data Scraping Code Appendix](#data-scraping-code-appendix)
  - [LLM Code Appendix](#llm-code-appendix)
- [Project Overview](#project-overview)
  - [Feature Extraction](#feature-extraction)
  - [Label Extraction](#label-extraction)
  - [Data Enrichment](#data-enrichment-using-web-scraping)
  - [Model Selection](#model-selection)
  - [User Interface](#user-interface-implementation)
- [Conclusion](#conclusion)

## Running Instructions
Our code for this project includes the following files:

- project_notebook.ipynb - the main code for the project, as well as a detailed walkthrough.

- data_scraping_code_appendix.ipynb - the code for the webscraping done in the project.

- LLM_code_appendix.py - the code for the LLM usage done in the project.

### Project Notebook
First, import the notebook to the Databricks platform.

Upload the file 'job_titles_dict.txt' to the platform as well.

Then, update the 'path' variable in cell 32 in the notebook to the current path of the 'job_titles_dict.txt' file on your machine.

![image](https://github.com/cohen-ariel/AI-Career-Path-Recommender/assets/127883151/c0ddbefa-7ed1-486d-82df-5244e0a507a0)

Now, simply run the notebook. Note that it is important to run the cells in their current order.

### Data Scraping Code Appendix
Upload the notebook to Google Colab.

To be able to run the data scraping section, please insert a Bright Data Scraping Browser key in the designated cell:

![image](https://github.com/cohen-ariel/AI-Career-Path-Recommender/assets/127883151/9fdf1fbb-36c4-4dd1-acd5-bdbce9e6aa4f)

Now, simply run the notebook in order to data scrape and recreate the corresponding CSV files:

- <job_title>.csv (where <job_title> represents a job title name that we webscraped)

- estimated_job_salaries.csv

- estimated_group_salaries.csv

### LLM Code Appendix
Unlike the previous code files which were submitted as notebooks, this is a .py file. Thus, it has to be run in a personal environment.

First, install the pandas and openai Python packages. In order to do that, run the following command lines in your Terminal:

```bash
pip install pandas
```

```bash
pip install --upgrade openai
```

Then, insert your OpenAI API key in the designated part within the code (at the top of the file):

![image](https://github.com/cohen-ariel/AI-Career-Path-Recommender/assets/127883151/4e934953-b539-427e-8b71-5781574c58ba)

*Note that you can create an OpenAI API key in the following [link](https://openai.com/blog/openai-api).

Now, simply run the code in order to recreate the following files:

- full_response.txt - the LLM's raw responses, concatenated

- job_titles_dict.txt - the processed responses, combined into a single dictionary


## Project Overview
In our project, we use the provided LinkedIn 'people' dataset in order to train an ML model, which recommends a career path for users, based on their information. We display the recommendation to the user, along with the estimated salary for the path, and several suggestions for popular jobs within that path.

### Feature Extraction
We extracted the following **initial feature set** from the LinkedIn dataset:
- Number of degrees
- Highest degree type
- Accumulated education years
- Education field cosine similarities
- Number of past job
- Accumulated experience years
- Number of recommendations
- Number of certifications
- Number of spoken languages
- Number of volunteer activities
- Number of courses
- ‘About’ section embeddings

### Label Extraction
Label extraction proved to be a bit more challenging. We made the following attempts:

**Attempt 1:** Use the job titles of all users as labels.

Problem: ~1mil unique job titles, too many labels.

**Attempt 2:** Reduce the number of job titles without removing too many records, using an Elbow graph.

Problem: ~35k job titles remaining, still too many labels.

**Attempt 3:** Assign all remaining job titles to 10 distinct career paths, using an LLM (via ChatGPT API). 

**This attempt was successful!** The distribution of job title assignments to the ten groups is as follows:

![image](https://github.com/cohen-ariel/AI-Career-Path-Recommender/assets/127883151/2be62e64-af0a-4c0d-9333-781bd3129173)

### Data Enrichment (Using Web Scraping)
We wanted to enrich our data with additional data regarding estimated salaries for the career paths we defined. To achieve that, we took the following steps:

1. We found the top 3 most common job titles for each career path (in our data).

2. We scraped the estimated salaries for each such job title (from "Glassdoor").

3. We, aggregated said salaries for each career path.

Below are the estimated salaries scraped for each career path:

![image](https://github.com/cohen-ariel/AI-Career-Path-Recommender/assets/127883151/587e53cf-c18c-4c57-92ab-aad10f45f053)

### Model Selection
In order to find the most suitable model for our task, we conducted numerous tests, comparing different models and architectures.

- For Multilayer Perceptron (MLP), we tested different number/size of hidden layers.
  
- For Random Forest (RF), we tested different number of trees.
  
- For Multiclass Logistic Regression (LR), we tested different regularization parameters.

The test results are as follows:

![image](https://github.com/cohen-ariel/AI-Career-Path-Recommender/assets/127883151/fdbc693a-9c33-4f1c-b1f6-2ed7fb8c89b3)

The best performing model, and the one we chose, is **MLP with a single hidden layer of size 100**.

Moreover, our final feature set is the **initial one** (chosen after performing a greedy feature selection procedure). 

### User Interface Implementation
To elevate our project, and to demonstrate our platform’s capabilities, we implemented a prototype for our system. We made it accessible through a simple user interface.

The interface asks the user for background information (education, experience, personal, etc.), and recommends a career path that best fits the user based on that information.
As mentioned, the recommendation is displayed alongside the following information:

- A salary estimation of the recommended career path.

- Multiple suggestions for popular jobs within that path.

- A salary estimation for said jobs.
  
*The user interface is available in the end of our project’s notebook. 

**A video walkthrough of the system is available in the following [link](https://technionmail-my.sharepoint.com/:v:/g/personal/dan_israeli_campus_technion_ac_il/ETUvwRYNH51Pt82pzbTlEtcBannfS6yr1pJIHUj1QgLCIA?e=6Y41xG).


## Conclusion
To summarize, we used real life data to create a machine learning system which utilizes users’ background information in order to give data-driven recommendations for a career path.

Upon model evaluation, it appears that there is room for improvement for our model’s performance. However, the performance for a couple of specific classes is quite impressive. 
Hence, our system could especially help users in these domains, and change their lives for the better.
