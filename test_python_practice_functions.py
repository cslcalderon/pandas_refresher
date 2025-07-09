from unittest import main, TestCase
from python_practice_functions import (
    clean_rows,
    clean_rows_efficient,
    filter_high_scores,
    clean_sales_data,
)


class TestMyFunctions(TestCase):
    def test_clean_rows(self):
        data = [
            {"name": " Alice ", "score": " 90", "city": "Austin"},
            {"name": "Bob", "score": "", "city": "Dallas"},
            {"name": " Charlie", "score": "85 ", "city": "Austin"},
        ]

        result = clean_rows(data)
        expected = [
            {"name": "Alice", "score": 90, "city": "Austin"},
            {"name": "Charlie", "score": 85, "city": "Austin"},
        ]
        self.assertEqual(result, expected)

    def test_sales_data_clean(self):
        data = [
            {"customer": " Alice ", "amount": " 100.50 ", "date": "2025-01-01"},
            {"customer": "Bob", "amount": "", "date": "2025-01-02"},
            {"customer": "  Charlie", "amount": "200.75", "date": "2025-01-02"},
        ]

        result = clean_sales_data(data)
        expected = [
            {"customer": "Alice", "amount": 100.50, "date": "2025-01-01"},
            {"customer": "Charlie", "amount": 200.75, "date": "2025-01-02"},
        ]

        self.assertEquals(result, expected)


if __name__ == "__main__":  # pragma: no cover
    main()
