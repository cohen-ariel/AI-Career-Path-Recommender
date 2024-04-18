from openai import OpenAI
import json
import pandas as pd


api_key = "Enter OpenAI API key"


def chatgpt(messages_history):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_history
    )

    return response.choices[0].message.content


def split_lst_into_chunks(lst, n):
    return [lst[i::n] for i in range(n)]


def assign_job_titles(input_file_path, output_file_name, num_chunks):
    jt_df = pd.read_csv(input_file_path)
    jt_lst = jt_df["job_title"].tolist()

    chunks = split_lst_into_chunks(jt_lst, num_chunks)

    with open(output_file_name, "w", encoding='utf-8') as f:

        system_prompt = """
        Your task is to assign job titles to the distinct group that they belong in. You should assign job titles ONLY to 
        one of the following groups:
        
        1. Management and Leadership
        
        2. Healthcare and Medical
        
        3. Education and Teaching
        
        4. Business and Administration
        
        5. Legal and Law
        
        6. Technology and Engineering
        
        7. Creative and Artistic
        
        8. Financial and Accounting
        
        9. Customer Service and Sales
        
        10. Nonprofit and Social Services
        
        11. Miscellaneous
        """

        for i, chunk in enumerate(chunks):
            if i % 10 == 0:
                print(i)

            user_prompt = f"""
            Hey, I have a list of job titles, and I want you to assign each one into a distinct group. You should
            assign it only to one of the following groups:
            
            1. Management and Leadership
            
            2. Healthcare and Medical
            
            3. Education and Teaching
            
            4. Business and Administration
            
            5. Legal and Law
            
            6. Technology and Engineering
            
            7. Creative and Artistic
            
            8. Financial and Accounting
            
            9. Customer Service and Sales
            
            10. Nonprofit and Social Services
            
            11. Miscellaneous
            
            I want your output to be in JSON format, where each key is a job title that I will provide, and the value is
            the group that you assign it. I remind you that you can assign job titles ONLY to one of the groups that I gave you.
            
            Here is the list of job titles:
            {chunk}
            """

            response = chatgpt([{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}])
            response += "\n"

            f.write(response)


def combine_dicts(input_file_path, output_file_name):
    with open(input_file_path, "r", encoding='utf-8') as f:
        dicts_str = f.read()

        dicts_str = dicts_str.replace("```json", "")
        dicts_str = dicts_str.replace("```", "")

        dicts_lst = dicts_str.split("}")

    job_titles_dict = {}
    for i, dict_str in enumerate(dicts_lst[:-1]):
        d = json.loads(dict_str + "}")
        job_titles_dict.update(d)

    with open(output_file_name, "w", encoding='utf-8') as f:
        job_titles_dict_str = json.dumps(job_titles_dict)
        f.write(job_titles_dict_str)


def main():
    assign_job_titles("job_titles.csv", "full_response.txt", num_chunks=1000)
    combine_dicts("full_response.txt", "job_titles_dict.txt")


if __name__ == "__main__":
    main()
