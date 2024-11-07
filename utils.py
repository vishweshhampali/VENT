from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load pre-trained DialoGPT model for conversation
def load_model(model_name="microsoft/DialoGPT-medium"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

# Generate response function
def generate_response(model, user_input):
    # Simple prompt with no additional instruction
    prompt = f"{user_input}"
    response = model(
        prompt,
        max_length=100,
        num_return_sequences=1,
        temperature=0.9,  # Slightly higher for more creative responses
        top_p=0.95,      # Top-p sampling for diverse output
        do_sample=True,  # Enable sampling
        pad_token_id=model.tokenizer.eos_token_id  # Suppress warning
    )
    # Return the entire generated response without modification
    generated_text = response[0]['generated_text'].strip()
    return generated_text
