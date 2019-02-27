from utils import run_module


class TestMain:
    def test_simple(self, capsys):
        try:
            run_module("fgrep", ["test", "tests/fixtures/test_file.txt"], run_name="__main__")
        except SystemExit as exeption:
            exit_code = exeption.code
        else:
            exit_code = 0

        out, _ = capsys.readouterr()

        assert exit_code == 0
        assert out == "strtesting2\ntest\n"

    def test_file_not_found(self, capsys):
        try:
            run_module("fgrep", ["test", "random-file"], run_name="__main__")
        except SystemExit as exeption:
            exit_code = exeption.code
        else:
            exit_code = 0

        _, err = capsys.readouterr()

        assert exit_code == 2
        assert err == "random-file: No such file or directory\n"

    def test_not_found_template(self, capsys):
        try:
            run_module("fgrep", ["uuu", "tests/fixtures/test_file.txt"], run_name="__main__")
        except SystemExit as exeption:
            exit_code = exeption.code
        else:
            exit_code = 0

        out, _ = capsys.readouterr()

        assert exit_code == 1
        assert out == ""
