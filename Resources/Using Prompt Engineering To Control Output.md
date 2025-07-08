# [The Practical Guide](chrome-extension://hajanaajapkhaabfcofdjgjnlgkdkknm/course/ai-agents-workflows-the-practical-guide/)

Your progress

29 of 58 complete.

Finish course to get your certificate

Share

Using Prompt Engineering To Control Output

You already learned that you can use "Structured Outputs" to "force" LLMs to generate JSON-formatted data adhering to a certain structure.

But, of course, you can request any kind of return data by the LLM - just be aware that you'll never have a 100% guarantee that you'll get exactly that kind of data. LLMs are not deterministic after all - they're just token generators that generate output based on probabilities.

Still, here are some example instructions you could add to your prompts to request output in certain formats:

-   _"Return the response as raw markdown so that I can directly use it in my markdown processing pipeline. Don't add any extra annotations or explanations."_
    
-   _"Return just the plain text, NOT formatted as markdown, without adding any extra annotations or explanations"_
    
-   _"Return just the code, NOT formatted as markdown, without adding any extra annotations or explanations"_
    
-   _"Return the data using CSV formatting. Use commas (not semicolons) as separators. Don't add any extra annotations or explanations."_
    

As mentioned, you don't have a guarantee that you get the data in the format you want. So you should build workflows / applications that are robust enough to deal with "incorrect" responses.

Either by you, manually, fixing them (e.g., if you stored the output in a file) or by handling possible edge cases & outcomes.

For example, LLMs will often wrap code or markdown responses in ` ```markdown ... ``` ` (or ` ```javascript ... ``` ` etc.) wrappers.

You can add code to check whether that's the case to remove those wrappers if they were added.

You'll see examples for that in later lectures.