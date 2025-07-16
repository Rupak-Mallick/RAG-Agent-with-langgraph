
def test_agent_response():
    query = "How can I change my password?"
    # Simulated response from agent (replace with actual agent if available)
    response = "To change your password, go to settings > account > change password."
    assert isinstance(response, str)
    assert "password" in response.lower()
