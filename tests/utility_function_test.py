import pytest
from utility_functions import create_char_line, create_table_cell, create_title, create_table_row, create_multi_line_table_row

# ============create_char_line tests============
def test_create_char_line_returns_string():
    """Ensures that create_line returns a string."""
    assert isinstance(create_char_line(), str)

def test_create_char_line_returns_default_value():
    """Test create_char_line returns a default value when not passed arguments."""
    default_value = f"{"-"*79}"
    assert create_char_line() == default_value

@pytest.mark.parametrize(
        ("char", "count", "expected"),
        (
            ("-", 5, "-----"),
            ("", 0, ""),
            ("hi", 2, "hihi"),
            ("test", 1, "test")
        )
)
def test_create_char_line_returns_expected_value(char, count, expected):
    """Test create_char_line returns expected value when passed arguments."""
    assert create_char_line(char, count) == expected


# ============create_title tests============
def test_create_title_returns_string():
    """Ensures that create_line returns a string."""
    assert isinstance(create_title("test"), str)

def test_create_title_returns_expected():
    """Ensures create_title returns the expected value."""
    assert create_title("hello") == "                            ------------------------\n                            |        hello         |\n                            ------------------------"
    assert create_title("this is a title") == "                            ------------------------\n                            |   this is a title    |\n                            ------------------------"


# ============create_table_cell tests============
def test_create_table_cell_returns_string():
    """Ensures that create_table_cell returns a string."""
    assert isinstance(create_table_cell("test", 10), str)

@pytest.mark.parametrize(
        ("item", "cell_width", "expected"),
        (
            ("test", 0, "test"),
            ("test", 10, "   test   "),
            ("test", 5, "test "),
            ("email", 10, "  email   ")
        )
)
def test_create_table_cell_returns_expected_value(item, cell_width, expected):
    """Ensures that create_table_cell returns expected value."""
    assert create_table_cell(item, cell_width) == expected


# ============create_table_row tests============
def test_create_line_returns_string():
    """Ensures that create_table_row returns a string."""
    assert isinstance(create_table_row(), str)

def test_create_table_row_returns_default_string():
    """Ensures create_table_row returns the correct default string when no args."""
    default = "|     Number     |                          Subject                           |"
    assert create_table_row() == default

@pytest.mark.parametrize(
        ("num", "subject", "expected"),
        (
            ("0", "British or American english variable names?", "|       0        |        British or American english variable names?         |"),
            ("1", "5 roasts for the the coffee-powered coder in your life", "|       1        |   5 roasts for the the coffee-powered coder in your life   |"),
            ("test", "test", "|      test      |                            test                            |")
        )
)
def test_create_table_row_returns_expected_value(num, subject, expected):
    """Ensures that create_table_cell returns expected value."""
    assert create_table_row(num, subject) == expected


# ============create_multi_line_table_row tests============
def test_create_multi_line_table_row_returns_string():
    """Ensures that create_multi_line_table_row returns a string."""
    assert isinstance(create_multi_line_table_row("test", "test", 60), str)

def test_create_multi_line_table_row_returns_expected_value():
    """Ensures that create_table_cell returns expected value."""
    expected = "|      test      |This string is to test that my function returns the correct |\n|                |     value. This is sorted as the variable 'expected'.      |"
    assert create_multi_line_table_row("test", "This string is to test that my function returns the correct value. This is sorted as the variable 'expected'.", 60) == expected