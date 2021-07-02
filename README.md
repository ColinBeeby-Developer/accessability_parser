# accessability_parser
To perform the parsing activities described here, you will need to have nhsuk-cms running on your local environment.

You will also have downloaded and restored a copy of the production database to your local environment.

## Acquiring site urls
Before you can parse any of the sites pages you will need to have collected the urls that you wish to examine into a file.

The file should be in the format of a single url on each line, EG

    http://yousite.com/path/path1/
    http://yoursite.com/path/page0/
    http://yoursite.com/path/page2/

To build a urls file you can use the following command:

    wget -m http://www.example.com 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.\(css\|js\|png\|gif\|jpg\|JPG\)$' > urls.txt

This may take a significant amount of time to run, depending on how many pages you site contains.

Once you have created your *urls.txt* file, you can 'tidy' the file prior to processing with the *parse_found_urls.py* utility, which is provided as part of this repository. NB you will probably need to modify the parse_found_urls file to match your particular requirements.

    python parse_found_urls.py urls.txt cleaned_urls.txt

## Creating The Rules

The 'rules' to check are supplied to the Accessibility Checking tool as a JSON file. The JSON file can contain several rules and each rule can contain one or more clauses.
Each rule will be applied to each url which is supplied in the input file. Once a rule match is found in a particular url, any further rule checking aborted and the url will be written to the output file, along with the rule which is matched with.

Each rule must contain one or more clauses. These clauses determine which tags are to be found in the file and in which order the tags must appear. 

Here is an example rules file:

    {
	   "accessability_rules": [
	    {
		    "rule_name": "important_callouts",
		    "rule_clauses": [
			    {
				    "order": "1",
				    "descriptor": "h3 {}"
			    },
			    {
				    "order": "2",
				    "descriptor": "h3 {'class': \\['nhsuk-warning-callout__label'\\]}",
				    "clause_exit": "h3 {}"
			    }
		    ]
	    },
	    {
		    "rule_name": "division_as_header",
		    "rule_clauses": [
			    {
				    "order": "1",
				    "descriptor": "div {'class': \\['.*-header(?!__).*'\\]}"
				}
		    ]
		}
      ]
    }
The above example contains two rules. The first rule "important_callouts" has two clauses. When this rule is applied the first clause will be checked by scanning down the html of the current url, looking for the descriptor. The descriptor gives the tag which is being searched for and the attributes which that tag must possess. The clause_exit specifies a tag at which, if found, searching should stop and a negative result returned. Then a search for the second clause will be searched for, starting at the point in the file where the first clause found a match.

## Running The Parser
Now that you have generated the file containing the urls to parse and a file containing the rules to use, you can now run the parser.

    python check_accessability.py urls_file output_file rules_file

EG

    python check_accessibility.py cleaned_urls.dat results.dat accessability_rules.json

> Written with [StackEdit](https://stackedit.io/).