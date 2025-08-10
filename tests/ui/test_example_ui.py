def test_example_title(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
