import io

from fgrep import fgrep


class TestStdInput:
    def test_empty_template(self, monkeypatch):
        input_mock = io.StringIO("string1\nstrtesting2\ntest\ntEsT\n\n\ntes\nstrites\nte st\n\n")
        input_mock.name = "mocked_stdin"
        monkeypatch.setattr("sys.stdin", input_mock)

        pattern = ""
        files = []
        ignore_case = False
        expected_result = "string1\nstrtesting2\ntest\ntEsT\n\n\ntes\nstrites\nte st\n"

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_simple(self, monkeypatch):
        input_mock = io.StringIO("string1\nstrtesting2\ntest\ntEsT\n\n\ntes\nstrites\nte st\n\n")
        input_mock.name = "mocked_stdin"
        monkeypatch.setattr("sys.stdin", input_mock)

        pattern = "test"
        files = []
        ignore_case = False
        expected_result = "strtesting2\ntest"

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_simple_ignore_case(self, monkeypatch):
        input_mock = io.StringIO("string1\nstrtesting2\ntest\ntEsT\n\n\ntes\nstrites\nte st\n\n")
        input_mock.name = "mocked_stdin"
        monkeypatch.setattr("sys.stdin", input_mock)

        pattern = "test"
        files = []
        ignore_case = True
        expected_result = "strtesting2\ntest\ntEsT"

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_not_found_template(self, monkeypatch):
        input_mock = io.StringIO("string1\nstrtesting2\ntest\ntEsT\n\n\ntes\nstrites\nte st\n\n")
        input_mock.name = "mocked_stdin"
        monkeypatch.setattr("sys.stdin", input_mock)

        pattern = "uuu"
        files = []
        ignore_case = True
        expected_result = ""

        assert fgrep(pattern, files, ignore_case) == expected_result


class TestSingleFile:
    def test_simple(self):
        pattern = "test"
        files = ["tests/fixtures/test_file.txt"]
        ignore_case = False
        expected_result = "strtesting2\ntest"

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_simple_ignore_case(self):
        pattern = "test"
        files = ["tests/fixtures/test_file.txt"]
        ignore_case = True
        expected_result = "strtesting2\ntest\ntEsT"

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_empty_template(self):
        pattern = ""
        files = ["tests/fixtures/test_file.txt"]
        ignore_case = False
        expected_result = "string1\nstrtesting2\ntest\ntEsT\n\n\ntes\nstrites\nte st\n"

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_not_found_template(self):
        pattern = "uuu"
        files = ["tests/fixtures/test_file.txt"]
        ignore_case = False
        expected_result = ""

        assert fgrep(pattern, files, ignore_case) == expected_result


class TestSomeFiles:
    def test_simple(self):
        pattern = "test"
        files = ["tests/fixtures/test_file.txt", "tests/fixtures/test_another_file.txt"]
        ignore_case = False
        expected_result = (
            "tests/fixtures/test_file.txt: strtesting2\ntests/fixtures/test_file.txt: test"
        )  # noqa

        assert fgrep(pattern, files, ignore_case) == expected_result

    def test_simple_ignore_case(self):
        pattern = "test"
        files = ["tests/fixtures/test_file.txt", "tests/fixtures/test_another_file.txt"]
        ignore_case = True

        expected_result_direct = "tests/fixtures/test_file.txt: strtesting2\ntests/fixtures/test_file.txt: test\ntests/fixtures/test_file.txt: tEsT\ntests/fixtures/test_another_file.txt: TeSt"  # noqa
        expected_result_reverse = "tests/fixtures/test_another_file.txt: TeSt\ntests/fixtures/test_file.txt: strtesting2\ntests/fixtures/test_file.txt: test\ntests/fixtures/test_file.txt: tEsT"  # noqa

        assert (
            fgrep(pattern, files, ignore_case) == expected_result_direct
            or fgrep(pattern, files, ignore_case) == expected_result_reverse
        )

    def test_empty_template(self):
        pattern = ""
        files = ["tests/fixtures/test_file.txt", "tests/fixtures/test_another_file.txt"]
        ignore_case = False

        expected_result_direct = "tests/fixtures/test_file.txt: string1\ntests/fixtures/test_file.txt: strtesting2\ntests/fixtures/test_file.txt: test\ntests/fixtures/test_file.txt: tEsT\ntests/fixtures/test_file.txt: \ntests/fixtures/test_file.txt: \ntests/fixtures/test_file.txt: tes\ntests/fixtures/test_file.txt: strites\ntests/fixtures/test_file.txt: te st\ntests/fixtures/test_file.txt: \ntests/fixtures/test_another_file.txt: TEsr\ntests/fixtures/test_another_file.txt: te st\ntests/fixtures/test_another_file.txt: TeSt\ntests/fixtures/test_another_file.txt: gfsefbesbfefe\ntests/fixtures/test_another_file.txt: fsesefesfs\ntests/fixtures/test_another_file.txt: \ntests/fixtures/test_another_file.txt: \ntests/fixtures/test_another_file.txt: sefsef\ntests/fixtures/test_another_file.txt: sefsef\ntests/fixtures/test_another_file.txt: te\ntests/fixtures/test_another_file.txt: s\ntests/fixtures/test_another_file.txt: t\ntests/fixtures/test_another_file.txt: file"  # noqa
        expected_result_reverse = "tests/fixtures/test_another_file.txt: TEsr\ntests/fixtures/test_another_file.txt: te st\ntests/fixtures/test_another_file.txt: TeSt\ntests/fixtures/test_another_file.txt: gfsefbesbfefe\ntests/fixtures/test_another_file.txt: fsesefesfs\ntests/fixtures/test_another_file.txt: \ntests/fixtures/test_another_file.txt: \ntests/fixtures/test_another_file.txt: sefsef\ntests/fixtures/test_another_file.txt: sefsef\ntests/fixtures/test_another_file.txt: te\ntests/fixtures/test_another_file.txt: s\ntests/fixtures/test_another_file.txt: t\ntests/fixtures/test_another_file.txt: file\ntests/fixtures/test_file.txt: string1\ntests/fixtures/test_file.txt: strtesting2\ntests/fixtures/test_file.txt: test\ntests/fixtures/test_file.txt: tEsT\ntests/fixtures/test_file.txt: \ntests/fixtures/test_file.txt: \ntests/fixtures/test_file.txt: tes\ntests/fixtures/test_file.txt: strites\ntests/fixtures/test_file.txt: te st\ntests/fixtures/test_file.txt: "  # noqa

        assert (
            fgrep(pattern, files, ignore_case) == expected_result_direct
            or fgrep(pattern, files, ignore_case) == expected_result_reverse
        )

    def test_not_found_template(self):
        pattern = "uuu"
        files = ["tests/fixtures/test_file.txt", "tests/fixtures/test_another_file.txt"]
        ignore_case = False
        expected_result = ""

        assert fgrep(pattern, files, ignore_case) == expected_result
