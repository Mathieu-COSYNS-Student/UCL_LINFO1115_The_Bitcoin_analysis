import sys
import pandas as pd

from inginious_question_1 import basic_properties
from inginious_question_2 import total_triadic_closures
from inginious_question_3 import end_balanced_degree


def main():
    sys.setrecursionlimit(1500)

    df = pd.read_csv('datasets/Project dataset.csv', index_col=0)

    print(basic_properties(df))
    print(total_triadic_closures(df))
    print(end_balanced_degree(df))


if __name__ == "__main__":
    main()
