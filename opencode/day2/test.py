from opencode_ai import Opencode


# Create a client (adjust base_url and API key as needed)
client = Opencode(base_url="http://127.0.0.1:65347")

#The base url can be created doing  opencode serve [--port <number>] [--hostname <string>]. This can be useful for automation.

# Example: list sessions (prints the result or error)
try:
	sessions = client.session.list()
	print(sessions)
except Exception as e:
	print(f"Error: {e}")