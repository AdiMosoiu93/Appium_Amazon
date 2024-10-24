import sys

from behave.__main__ import main as behave_main
from behave_html_formatter import HTMLFormatter

print("HTMLFormatter is available.")


def run_behave():
    args = [
        '--format', 'behave_html_formatter:HTMLFormatter',
        '--out', 'report.html',
        'features'
    ]
    sys.argv = ['behave'] + args
    behave_main()


if __name__ == "__main__":
    run_behave()
