import google.generativeai as genai

genai.configure(api_key="AIzaSyDPMKWkVsja7XrxUhFkLRo596GCaHj_0Xs")
models = genai.list_models()

for m in models:
    print(m.name)  # check available models
