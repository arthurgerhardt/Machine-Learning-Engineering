# Data received from an API (JSON)
data = {
	"username": "alice",
	"email": "alice@example.com",
	"age": 30,  # age should be int
	"is_active": True  # boolean should be bool
}

# Manual validation without Pydantic
def validate_data(data):
	if not isinstance(data.get("username"), str):
		raise ValueError("username must be a string")
	if not isinstance(data.get("email"), str) or "@" not in data.get("email"):
		raise ValueError("invalid email")
	if not isinstance(data.get("age"), int):
		raise ValueError("age must be an integer")
	if not isinstance(data.get("is_active"), bool):
		raise ValueError("is_active must be a boolean")
	return True

try:
	validate_data(data)
except ValueError as e:
	print(f"Validation error: {e}")