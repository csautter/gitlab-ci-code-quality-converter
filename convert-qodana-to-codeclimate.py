import json

with open('./result-allProblems.json', 'r', encoding="cp866") as json_file:
    data=json_file.read()

qodana_issue_list = json.loads(data)['listProblem']

def map_severity(severity):
    severity_map = {
        "Info": "info",
        "DEPRECATION": "minor",
        "Weak Warning": "major",
        "Moderate": "major",
        "Low": "major",
        "Warning": "critical",
        "High": "critical",
        "Error": "blocker",
        "Critical": "blocker",
    }
    return severity_map[severity]

def convert_to_code_climate_style(issue):
    return {
    "type": "issue",
    "check_name": issue['category'] + ': ' + issue['type'],
    "description": issue['comment'],
    "content": issue['detailsInfo'], # https://github.com/codeclimate/platform/blob/master/spec/analyzers/SPEC.md#contents
    "categories": [issue['category']], # https://github.com/codeclimate/platform/blob/master/spec/analyzers/SPEC.md#categories
    "location": { # https://github.com/codeclimate/platform/blob/master/spec/analyzers/SPEC.md#locations
      "path": issue['sources'][0]['path'],
      "lines": {
         "begin": issue['sources'][0]['line']
      },
    },
    "severity": map_severity(issue['severity']),
    }

cc_issue_list = []

for issue in qodana_issue_list:
    cc_issue_list.append(convert_to_code_climate_style(issue))

with open('./cc_issue_list.json', 'w') as outfile:
    json.dump(cc_issue_list, outfile, indent=3)
