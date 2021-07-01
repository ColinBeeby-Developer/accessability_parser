import json

import requests
from bs4 import BeautifulSoup


class RulesEngine(object):

    FOUND = 1
    NOT_FOUND = 2
    EXIT = 3

    def __init__(self, rules_file):
        self.accessability_rules = []
        self.rules = self.parse_rules_file(rules_file)

    def parse_rules_file(self, rules_file):
        with open(rules_file, "r") as rules:
            self.accessability_rules = json.load(rules)["accessability_rules"]

    def check_url(self, url):
        result = False
        matching_rule = None
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml").body
        page_elements = [e for e in soup.descendants if e.name is not None]
        for rule in self.accessability_rules:
            page_element_index = 0
            rule_clause_index = 0
            all_clauses_found = self.check_rule_clauses(
                page_elements,
                page_element_index,
                rule["rule_clauses"],
                rule_clause_index,
            )
            if all_clauses_found == self.FOUND:
                result = True
                matching_rule = rule["rule_name"]
                break

        return result, matching_rule

    def check_rule_clauses(
        self, page_elements, page_element_index, rule_clauses, rule_clause_index
    ):
        elements_checked = 0
        clause_descriptor = rule_clauses[rule_clause_index]["descriptor"]
        clause_exit = rule_clauses[rule_clause_index].get("exit_clause")
        for page_element in page_elements[page_element_index:]:
            page_element_descriptor = "{} {}".format(
                page_element.name, page_element.attrs
            )
            if page_element_descriptor == clause_exit:
                return self.EXIT
            if page_element_descriptor == clause_descriptor:
                if len(rule_clauses) - 1 == rule_clause_index:
                    return self.FOUND
                else:
                    clause_result = self.check_rule_clauses(
                        page_elements,
                        page_element_index + elements_checked + 1,
                        rule_clauses,
                        rule_clause_index + 1,
                    )
                    if clause_result == self.EXIT:
                        continue
                    else:
                        return clause_result
            elements_checked += 1

        return self.NOT_FOUND  # hit the end of the page and not found the clause
