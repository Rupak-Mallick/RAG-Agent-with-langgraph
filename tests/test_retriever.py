
def test_retriever():
    query = "What is the refund policy?"
    # Simulated document list (replace with actual retriever call)
    results = [{"page_content": "Our refund policy allows returns within 30 days."}]
    assert len(results) > 0
    assert "refund" in results[0]["page_content"].lower()
