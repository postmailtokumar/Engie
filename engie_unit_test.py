import unittest
import pandas as pd
import json


def ascii_val(x):

    return ord(x)


def convert(input = ['A', 'a', 'H', 'X']):
    try:

        df = pd.DataFrame()
        input = pd.Series(input)
        df['input'] = input
        df['status'] = input.str.contains(r'[a-hA-H]', regex=True)
        df['ascii'] = df['input'].apply(ascii_val)
        df['output'] = df['ascii']
        df.loc[df['status'] == False, 'output'] = df['ascii'] * 10
        df['output'] = df['output'].astype(int)
        print(df)
        return df['output'].to_json(orient='split', index=False)
    except Exception as exc:
        print(str(exc))
        return 'something went wrong'


class Testconvert(unittest.TestCase):

    def test_convert_success(self):
        actual = convert(input = ['A', 'a', 'H', 'X'])
        actual_json = json.loads(actual)
        expected = {"name":"output","data":[65,97,72,880]}
        self.assertEqual(actual_json['data'], expected['data'])