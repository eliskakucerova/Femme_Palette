from main import Mentees
# you may run test in Pycharm console
# by calling >>> pytest -v basic_test.py


class TestClass:
    # test of dataset and non-null values
    def test_empty(self):
        for column in Mentees.df.columns:
            if not Mentees.df[column].empty:
                pass
            else:
                raise AssertionError('Test failed')

    # here I put the default value, could be change to check other columns if there is type of variable which I expect
    def test_type_data(self):
        for name in Mentees.df['full_name']:
            assert type(name) == str

        if type(name) != str:
            raise AssertionError("Invalid type")

    # test, the language is in set of unique languages and there is no other unpaired language
    def test_set_languages(self):
        for language in Mentees.set_languages():
            assert language in set(Mentees.df['language']) and len(Mentees.set_languages()) == len(
                set(Mentees.df['language']))

    def test_mean_full_name(self):
        assert Mentees.mean_full_name() == Mentees.df['full_name'].str.len().sum() / Mentees.df['full_name'].count()

    # test, the longest name is the only one
    def test_longest_full_name(self):
        assert len(Mentees.longest_full_name()) == max(Mentees.df['full_name'].str.len().unique())

    # test, the shortest name is the only one
    def test_shortest_full_name(self):
        assert len(Mentees.shortest_full_name()) == min(Mentees.df['full_name'].str.len().unique())


basic_test = TestClass()
