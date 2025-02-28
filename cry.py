import pandas as pd
import json
import re

# Read JSON file
with open("new.json", "r") as file:
    data = json.load(file)

# Convert JSON string to Python dictionary
# data = json.loads(json_data)    

# Normalize the 'value' field to flatten the structure
df = pd.json_normalize(data['value'])

# Rename columns for clarity
df.rename(columns={
    '_links.self.href': 'self_link',
    '_links.web.href': 'web_link'
}, inplace=True)

# Save to CSV
df.to_csv("output_cry.csv", index=False)

# Display DataFrame
print(df)


# Define the naming standard pattern
# <PipelinePrefix>-<serviceName>-<resourceCode>-<Descriptions>-<PipelineSuffix>
# Prefix: catos-*  Suffix: *-CICD / *-CI
pattern = re.compile(r"^catos-(pfm|modules)-[a-zA-Z0-9-]+-(CICD|CI)$")

# Check which names do not match the pattern
df['is_compliant'] = df['name'].apply(lambda x: bool(pattern.match(x)))

# Extract non-compliant pipelines
non_compliant_df = df[~df['is_compliant']]

# Save non-compliant pipelines to a new CSV file
non_compliant_df.to_csv("non_compliant.csv", index=False)

# Display the count of non-compliant pipelines
print(f"Total non-compliant pipelines: {len(non_compliant_df)}")
