import pandas as pd
from statistics import mean
import json

# TODO get the number of mentees
# TODO get the set of languages mentees know
# TODO get the average length of mentees full names
# TODO find mentees with the longest full name
# TODO find the mentees with shortest full name
# TODO save report into .json file
# TODO add basic unit tests


sheet_url = "https://docs.google.com/spreadsheets/d/1HMZGrtc9bCdO7eaD6gMcxXXf2LJZ1JVWrU8noV6_MSs/edit#gid=0"


class Mentees:

    def __init__(self, url):
        self.url = url
        self.url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
        self.df = pd.read_csv(self.url)
        self.df['full_name'] = self.df['first_name'] + ' ' + self.df['last_name']

    def basic_info(self):
        return self.df.info()

    def number_mentees(self):
        number_of_mentees = self.df['index'].count()
        return number_of_mentees

    def set_languages(self):
        set_of_languages = self.df['language'].unique()
        return set_of_languages

    # average length of full name without dash between first and last name
    def average_full_name(self):
        name_without_dash = []
        for name in self.df['full_name']:
            name_len = len((name.replace(' ', '')))
            name_without_dash.append(name_len)

        return mean(name_without_dash)

    # average length of full name with dash between first and last name
    # used list comprehension
    def mean_full_name(self):
        mean_count = mean([len(name) for name in self.df['full_name']])
        return mean_count

    def longest_full_name(self):
        longest_name = ' '
        for name in self.df['full_name']:
            if len(longest_name) < len(name):
                longest_name = name

        return longest_name

    def shortest_full_name(self):
        shortest_name = ' '
        for name in self.df['full_name']:
            if shortest_name == ' ':
                shortest_name = name
            elif len(shortest_name) > len(name):
                shortest_name = name

        return shortest_name

    # function to convert data to dictionary and .json file
    def answers(self):
        # create dictionary
        my_details = {
            "number of mentees": int(self.number_mentees()),
            "set of languages": tuple(self.set_languages()),
            "average full name without dash": float(self.average_full_name()),
            "average full name with dash": float(self.mean_full_name()),
            "longest name": str(self.longest_full_name()),
            "shortest name": str(self.shortest_full_name())
        }

        # serializing json
        json_object = json.dumps(my_details, indent=len(my_details))

        # writing to answer.json
        with open("answer.json", "w") as outfile:
            outfile.write(json_object)


# object initialization
Mentees = Mentees(sheet_url)

# quick overview, basic info about the dataset
Mentees.basic_info()

# by this command you will get answers to all your questions
Mentees.answers()
