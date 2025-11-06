import litellm 

BASE_URL="https://inference-3scale-apicast-production.apps.rits.fmaas.res.ibm.com/llama-3-3-70b-instruct/v1"
MODEL_NAME="openai/meta-llama/llama-3-3-70b-instruct"
API_KEY="c2c8951cd97777a26fa7bdb23f91b251"

completion_args = {
    "model": MODEL_NAME,
    "api_base": BASE_URL,
    "max_tokens": 50,
    "max_completion_tokens": 50,
    "extra_headers": {"RITS_API_KEY": API_KEY}
    }
litellm.api_key = API_KEY
response = litellm.completion(
    messages=[{"role": "user", "content": "Hello! Who are you?"}],
    **completion_args,
    )
print(response)