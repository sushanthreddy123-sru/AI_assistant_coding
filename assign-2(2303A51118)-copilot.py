#Task 3: Palindrome Check
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
# Test cases
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))  # False
Comparison: Gemini AI vs Copilot:
1)Coding Performance:
->Copilot is generally better integrated into IDEs for fast code suggestions and developer workflows.
->Gemini can generate code too, but tends to be slower and broader-focused rather than as tightly embedded into editor workflows.
Winner for pure coding speed → Copilot

2)Context & Reasoning:
->Gemini excels at deep reasoning, large context understanding (docs + code + research), and handling multimodal inputs like images/diagrams.
->Copilot is optimized for shorter, code-centric tasks within text editors.
Winner for complex tasks → Gemini

3)Integration & Workflow:
->Copilot works directly in popular editors with minimal setup.
->Gemini can integrate through CLI or APIs and into Google’s ecosystem, but isn’t as IDE-native by default (though integrations are growing).
Winner for seamless coding experience → Copilot

4)Multimodal & General Intelligence:
->Gemini supports multimodal input (text, visuals) and broader tasks like research, explanations, documentation, strategy, etc.
->Copilot focuses on code generation and in-editor support only.
Winner for versatility → Gemini

5)Pricing & Value

->Copilot is usually around $10/mo for individuals and integrated deeply with GitHub tools.
->Gemini varies by plan but often comes bundled with Google services (Cloud, Workspace), and free tiers like Gemini CLI offer generous daily usage.
Winner depends on budget & ecosystem needs

6)So Which One Is Better?
Use Case	Better Choice:
->Daily coding, fast suggestions inside your editor	GitHub Copilot
->Complex tasks — reasoning, docs, long projects, multimodal input	Google Gemini
->Working within GitHub & developer workflow	Copilot
->Handling diverse non-code tasks or big context workflows	Gemini

7)Many developers actually use both:
->Copilot for IDE coding speed,
->Gemini for deep questions, research, design docs, and multimodal tasks.

8)Quick Summary

->Copilot — Best code-focused assistant with strong editor integration and real-time code generation.
->Gemini — Best general AI partner for big-picture thinking, multimodal understanding, and broad tasks beyond code.