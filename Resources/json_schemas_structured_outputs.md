More On JSON Schemas & Structured Outputs

Structured Outputs is an extremely useful feature that allows you to "force" LLMs to generate text that contains data in a certain shape / format.

As shown in this course, OpenAI has [official support](https://platform.openai.com/docs/guides/structured-outputs) - but, for example, Google also offers a [similar feature](https://ai.google.dev/gemini-api/docs/structured-output).

Those providers leverage a concept called "JSON Schema", which is a standardized way of describing the shape of JSON-formatted data.

You can learn more about JSON schema in general [here](https://json-schema.org/).

Though, you should always consult the documentation of the AI provider you're using, since they don't necessarily support all JSON schema features. For example, you find an overview of the features supported by OpenAI [here](https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses#supported-schemas).
