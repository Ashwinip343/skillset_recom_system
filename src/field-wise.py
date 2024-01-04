import json
field_wise_job={"Augmented and virtual reality":["XR UI/UX designer","XR developer","3D Modeling and Animation Specialist","Hardware Engineer","Computer Vision Engineer"],
                "Quantum computing":["Quantum Algorithm Researcher","Theoretical Quantum Physicist","Quantum Applications Specialist","Quantum Cloud Engineer"],
                }

for i in field_wise_job:
    print(i)

with open("./field_wise.json", "w") as outfile: 
    json.dump(field_wise_job, outfile)