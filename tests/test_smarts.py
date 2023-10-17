import os
from pathlib import Path
import unittest

import pandas as pd
from rdkit import Chem


class CheckedSmarts(unittest.TestCase):
    def test_validity(self):
        data_path = Path(__file__).parents[1] / "data"
        query_path = data_path / "queries"
        checked_smarts = 0
        for file in os.listdir(query_path):
            smarts_df = pd.read_csv(query_path / file, sep="\t")
            try:
                smarts_list = smarts_df["SMARTS"].tolist()
            except Exception as e:
                print(file)
                raise e
            for smarts_str in smarts_list:
                smarts_obj = Chem.MolFromSmarts(smarts_str)
                self.assertIsNotNone(smarts_obj, file)
            checked_smarts += 1
        print(checked_smarts)


if __name__ == '__main__':
    unittest.main()
