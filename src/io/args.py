
import argparse
from typing import Any

def parse_args() -> Any:
    """ le os argumentos de linha de comando usando a biblioteca argparse """
    parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
    parser.add_argument('config_path', type=str, help='Path das configs')
    parser.add_argument('report_path', type=str, help='Path do report.txt')
    args = parser.parse_args()


    # Exemplo. Utilizar o argparse na versao final
    return args
