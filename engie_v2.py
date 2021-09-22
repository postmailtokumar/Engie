from flask import Flask, jsonify, request
import re
import pandas as pd


app = Flask(__name__)


def ascii_val(x):

    return ord(x)


@app.route("/convert",  methods = ['GET','POST'])
def convert():
    try:
        input = ['A', 'a', 'H', 'X']
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


if __name__ == "__main__":
    app.run(debug=True)