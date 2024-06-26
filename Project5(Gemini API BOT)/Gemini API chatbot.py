from google.generativeai import GenerativeModel, configure

# Configure the API with your key (replace with your actual key)
configure(api_key="AIzaSyAAgH7ODk1h_mpfYDBx4r0Q6yqgCCUNaFE")

# Create the GenerativeModel instance
model = GenerativeModel("gemini-1.5-pro")

# Start the conversation
print(model.generate_content("How are you?").text)

while True:
  # Get user input
  user_input = input("You: ")

  # Check for stop condition
  if user_input.lower() == "stop the chat":
    break

  # Generate response based on user input
  response = model.generate_content(user_input).text
  print(f"Bard: {response}")
