import json 
import google.generativeai as palm
import google.generativeai as palm
api_key = 'YOUR_API_KEYS' # put your API key here
palm.configure(api_key=api_key)

skills_and_technology={} #empty dictionary
field_wise_job={"Augmented and virtual reality":["XR UI/UX designer","XR developer","3D Modeling and Animation Specialist","Hardware Engineer","Computer Vision Engineer"],
                "Quantum computing":["Quantum Algorithm Researcher","Theoretical Quantum Physicist","Quantum Applications Specialist","Quantum Cloud Engineer"],
                }

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)


def palm_api(job):
# generate text
  prompt = 'Give me the skills, tools & techonologies , famous books to get started with & additional certificication course or youtube channels required for'+job+'in bullet points, in the form of python dictionary'
  text = palm.generate_text(
      prompt=prompt,
      model=model,
      temperature=0.8,
      max_output_tokens=1024,
    # top_p=0.9,
    # top_k=40,
    # stop_sequences=['\n']
  )
  return text.result


for i in field_wise_job.values():
  for job in i:
    skills_and_technology[job]=palm_api(job)


# for i in field_wise_job.values():
#   for job in i:
#     print("\n"+job+ ": "+skills_and_technology[job])
# Define student_details dictionary



json_l=[]
empty_dict={}
for i in skills_and_technology.keys():
  # print(i)
  empty_dict["role"]=i
  empty_dict["content"]=skills_and_technology[i]
  # print(empty_dict)
  json_l.append(empty_dict)

print(json_l)

    
# Convert and write JSON object to file
with open("./sample.json", "w") as outfile: 
    json.dump(json_l, outfile)
    


