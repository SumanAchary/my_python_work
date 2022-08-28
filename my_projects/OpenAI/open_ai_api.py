import openai

openai.api_key = "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"
prompt_text1 = ("Classify the Text's label as positive, neutral, or negative.\n"
                + "Text: Kill Him!\n"
                + "Sentiment:")

try:
    for i in range(20):
        text = input("Ask Me Anything buddy?\n")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text
        )
        print(f'SUMAN AI : {response.get("choices")[0].get("text")}')

except Exception as e:
    print(f"Error: {e}")