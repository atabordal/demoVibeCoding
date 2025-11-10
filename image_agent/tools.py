import datetime
from google import genai
from google.genai.types import HttpOptions
from google.genai import types
import base64
import os
import mimetypes

def generate_image(prompt: str) -> str:
  """
  Generates an image based on a prompt and saves it to the 'images' directory.

  Args:
    prompt: The text prompt to generate the image from.
  """
  # Create the images directory if it doesn't exist
  if not os.path.exists('images'):
    os.makedirs('images')

  # The user had vertexai=True, which might not be standard for this library.
  # If issues arise, consider removing it or using the google-cloud-aiplatform library.
  client = genai.Client(http_options=HttpOptions(api_version="v1"), vertexai=True)

  model = "gemini-2.5-flash-image"
  contents = [
      types.Content(
          role="user",
          parts=[
              types.Part(text=prompt),
          ]
      )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 8192, # Adjusted for image generation
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="BLOCK_MEDIUM_AND_ABOVE"
    )],
  )

  try:
    response = client.models.generate_content(
      model = model,
      contents = contents,
      config = generate_content_config,
    )

    image_part = None
    if response.candidates:
        for part in response.candidates[0].content.parts:
            if part.inline_data and isinstance(part.inline_data, types.Blob) and part.inline_data.mime_type.startswith("image/"):
                image_part = part.inline_data
                break

    if image_part:
      image_data = image_part.data
      mime_type = image_part.mime_type
      extension = mimetypes.guess_extension(mime_type) or ".png"
      timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      file_path = os.path.join("images", f"generated_image_{timestamp}{extension}")

      with open(file_path, "wb") as f:
        f.write(image_data)
      print(f"Image saved to {file_path}")
      # Construct a simple hyperlink for the local file
      return f"Image generated and saved: [file://{os.path.abspath(file_path)}](file://{os.path.abspath(file_path)})"
    else:
      print("No image was generated. Full response:")
      print(response)
      return "No image was generated."

  except Exception as e:
    print(f"An error occurred: {e}")
    return f"An error occurred during image generation: {e}"


if __name__ == "__main__":
  # Example usage:
  generate_image("a beautiful landscape")
