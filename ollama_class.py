import requests
import json
from bg_context import examples_10, examples_chain_of_thoughts

class OllamaLLM:  
   def __init__(self, api_url="http://localhost:11434/api/generate"):
        """
        Initialize the Ollama interface with the API URL.
        """
        self.api_url = api_url
        self.examples_10 = examples_10
        self.examples_chain_of_thoughts = examples_chain_of_thoughts
        
   def minimally_enhance_text(self, model, text, context=None):
        """
        Enhance the text minimally by fixing grammar and spelling issues, using the given context.
        """
        prompt = f"""
        Background information: {context}

         Minimally enhance the following text by fixing grammar, spelling, and sentence structure issues. 
         Do not change the original meaning or tone. The enhancement must:
         - **Add no more than 10 additional words**.
         - **Preserve the original brevity and clarity**.
         - Avoid adding new content or rephrasing unnecessarily.
        
        examples for guidance:
         input text: pointer check
         enhanced text: I forgot to check pointer.
         input text: a and b point to the same value, until a chages
         enhanced text: I should take a note that A and B point to the same value until A changes.

        Original input Text: "{text}"

         Respond in JSON format:
         {{
            "enhanced_text": <result>,
         }}
        """
        return self._make_request(model, prompt)
     
   def analyze_planning(self, model, text, context=None):
      """
      Analyze the planning level of the input text using the Ollama model.

      Args:
         model (str): The name of the model to use (e.g., "llama3.2").
         text (str): The input text to analyze.
         context (str, optional): Custom background information to provide context for the analysis.

      Returns:
         dict: A JSON-like dictionary with the planning score and the analyzed text.
      """
      background = f"Background information: {context}\n\n" if context else ""
      prompt = f"""
      {background}Metacognition is the process of thinking about one's own thinking, including skills for self-regulation and reflection.

      You are tasked with evaluating **planning skills**, which involve the ability to think ahead, set objectives, and structure a task before starting it. This includes:
      - Identifying goals and steps required to achieve them.
      - Prioritizing tasks and organizing resources effectively.
      - Demonstrating foresight and preparation.

      Analyze the following text for **planning skills**:
      Text: "{text}"
      
      Provide a score (0-5) for:
      - **Planning**: How well does the text indicate foresight, goal setting, and organization of ideas?

      Use these reference examples for guidance:
      - **5 (Excellent Planning)**: "I will first gather all data from source A, then analyze it for trends using tool B, and finally summarize the findings in a presentation."
      - **4 (Good Planning)**: "I have a few steps planned, like analyzing trends and summarizing results, but I'm not sure how to start collecting the data."
      - **3 (Moderate Planning)**: "I think I'll analyze the trends and then summarize the results, but I haven't decided the exact steps."
      - **2 (Limited Planning)**: "I have some rough ideas but no concrete steps or priorities."
      - **1 (Minimal Planning)**: "I might try to collect data and then see what happens."
      - **0 (No Planning)**: "I just did the task without any preparation or planning."

      Important:
      - For empty text or gibberish input (e.g., random symbols, unreadable content), assign a score of **0**.
      - For reasonable content that lacks clear signs of planning (e.g., no structure, foresight, or organization), assign a score of **0**.

      Respond in JSON format:
      {{
         "text": "{text}",
         "planning_score": <score>
      }}
      """
      return self._make_request(model, prompt)

   def analyze_monitoring(self, model, text, context=None):
      """
      Analyze the monitoring level of the input text using the Ollama model.

      Args:
         model (str): The name of the model to use (e.g., "llama3.2").
         text (str): The input text to analyze.
         context (str, optional): Custom background information to provide context for the analysis.

      Returns:
         dict: A JSON-like dictionary with the monitoring score and the analyzed text.
      """
      background = f"Background information: {context}\n\n" if context else ""
      prompt = f"""
      {background}Metacognition involves thinking about one's thinking. Monitoring is a key component, referring to the ability to check progress, identify mistakes, and regulate actions while performing a task.

      You are tasked with evaluating **monitoring skills**, which include:
      - Assessing progress regularly.
      - Identifying and addressing errors or discrepancies.
      - Demonstrating self-awareness during the task.

      Analyze the following text for **monitoring skills**:
      Text: "{text}"
      
      Provide a score (0-5) for:
      - **Monitoring**: How well does the text show self-checking, progress evaluation, and adjustment?

      Use these examples for scoring:
      - **5 (Excellent Monitoring)**: "At each step, I reviewed my work to ensure it was correct, and I adjusted the strategy when errors were found."
      - **4 (Good Monitoring)**: "I checked most steps for accuracy and corrected some mistakes but might have missed minor issues."
      - **3 (Moderate Monitoring)**: "I noticed some mistakes while working but didn’t consistently check progress."
      - **2 (Limited Monitoring)**: "I checked my work at the end and found several errors."
      - **1 (Minimal Monitoring)**: "I only checked for errors after completing the entire task."
      - **0 (No Monitoring)**: "I completed the task without verifying any steps for correctness or progress."

      Important:
      - For empty text or gibberish input (e.g., random symbols, unreadable content), assign a score of **0**.
      - For reasonable content that lacks signs of monitoring (e.g., no self-checking or progress evaluation), assign a score of **0**.

      Respond in JSON format:
      {{
         "text": "{text}",
         "monitoring_score": <score>
      }}
      """
      return self._make_request(model, prompt)

   def analyze_evaluating(self, model, text, context=None):
      """
      Analyze the evaluating level of the input text using the Ollama model.

      Args:
         model (str): The name of the model to use (e.g., "llama3.2").
         text (str): The input text to analyze.
         context (str, optional): Custom background information to provide context for the analysis.

      Returns:
         dict: A JSON-like dictionary with the evaluating score and the analyzed text.
      """
      background = f"Background information: {context}\n\n" if context else ""
      prompt = f"""
      {background}Metacognition includes reflection and evaluation, crucial for judging outcomes, identifying strengths and weaknesses, and planning improvements.

      You are tasked with evaluating **evaluating skills**, which involve:
      - Reflecting on results and outcomes.
      - Identifying areas of success and failure.
      - Proposing improvements for future tasks.

      Analyze the following text for **evaluating skills**:
      Text: "{text}"
      
      Provide a score (0-5) for:
      - **Evaluating**: How well does the text demonstrate judgment, assessment, and reflection on outcomes?

      Reference examples:
      - **5 (Excellent Evaluating)**: "The outcome met expectations, and I identified key areas for improvement, including focusing more on accuracy in step 2."
      - **4 (Good Evaluating)**: "The results were mostly good, and I noted some areas to improve, but I didn’t analyze all the details."
      - **3 (Moderate Evaluating)**: "I reviewed the outcome briefly and noted a few weaknesses, but I didn’t fully assess why they occurred."
      - **2 (Limited Evaluating)**: "I looked at the results but didn’t reflect deeply or identify clear improvements."
      - **1 (Minimal Evaluating)**: "I acknowledged the outcome but didn’t analyze it or think about improvements."
      - **0 (No Evaluating)**: "I finished the task without considering the outcome or reflecting on it."

      Important:
      - For empty text or gibberish input (e.g., random symbols, unreadable content), assign a score of **0**.
      - For reasonable content that lacks evaluation (e.g., no reflection or judgment), assign a score of **0**.

      Respond in JSON format:
      {{
         "text": "{text}",
         "evaluating_score": <score>
      }}
      """
      return self._make_request(model, prompt)

   def _make_request(self, model, prompt, response_format="json"):
    """
    Helper method to make a request to the Ollama API.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    if response_format:
        payload["format"] = response_format

    try:
        response = requests.post(self.api_url, json=payload)
        response.raise_for_status()  # Raises HTTPError for bad HTTP responses
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")  # Log the error
        return None  # Explicitly return None on failure

    try:
        result = response.json()
        if "error" in result:
            print(f"API Error: {result['error']}")  # Log API-specific errors
            return None
        return result.get("response", None)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")  # Log JSON parsing errors
        return None
        
   def generate_batch_data(self, model, context, num_samples, tag):
        """
        Generate a dataset in batches to avoid exceeding the token window.

        Args:
            model (str): The name of the model (e.g., "llama3.2").
            context (str): Background context for data generation.
            num_samples (int): Total number of samples to generate.
            tag (str): Tag to associate with the generated data (e.g., "planning", "evaluating").

        Returns:
            list: A list of dictionaries containing generated texts and tags.
        """
        # List to store the final results
        all_examples = []
        batch_size = 10  # Number of samples per batch
        num_batches = (num_samples + batch_size - 1) // batch_size  # Calculate total batches

        for batch in range(num_batches):
            # Number of samples in the current batch
            current_batch_size = min(batch_size, num_samples - batch * batch_size)
            
            prompt = f"""
            Background information: {context}

            Generate {current_batch_size} unique examples of student reflections that demonstrate the following metacognitive skill: {tag}.
            Each example should:
            - Be concise and realistic, representing a student's perspective.
            - Demonstrate diverse phrasings while maintaining relevance to the {tag} skill.
            - Be no longer than 50 words per example.

            Respond in JSON format:
            {{
                "examples": [
                    {{"text": "<example 1>"}},
                    {{"text": "<example 2>"}},
                    ...
                ]
            }}
            """
            try:
                # Request batch generation
                result = self._make_request(model, prompt)
                if not result or "examples" not in result:
                    raise ValueError("Invalid response format or no examples returned")
                
                # Append the tag to each generated example
                batch_examples = [
                    {"text": example["text"], "tag": tag} for example in result["examples"]
                ]
                all_examples.extend(batch_examples)
            except Exception as e:
                print(f"Error generating batch {batch + 1}: {e}")
                continue  # Skip this batch and continue with the next

        return all_examples
   
   def generate_na_data(self, model, num_samples):
    """
    Generate a dataset of "na" (Not Applicable) examples that do not demonstrate any metacognitive content.

    Args:
        model (str): The name of the model (e.g., "llama3.2").
        context (str): Background context to guide the generation of unrelated examples.
        num_samples (int): Total number of "na" examples to generate.

    Returns:
        list: A list of dictionaries containing generated texts and the "na" tag.
    """
    all_examples = []
    batch_size = 10  # Number of examples per batch
    num_batches = (num_samples + batch_size - 1) // batch_size  # Calculate total batches

    for batch in range(num_batches):       
        prompt = f"""
        Generate 10 unique examples of general reflections or comments that do NOT demonstrate any metacognitive content.
        Examples should:
        - Be unrelated to planning, monitoring, or evaluating skills.
        - Avoid mentions of progress tracking, goal setting, self-reflection, or any metacognitive behavior.
        - Focus on neutral or descriptive statements that do not involve self-regulation or task performance.
        - Be concise and realistic, no longer than 50 words.

        Examples of valid "na" texts:
        - "The weather was nice today, and I enjoyed my walk in the park."
        - "I had coffee this morning and it tasted great."
        - "The movie I watched yesterday was really entertaining."

        Respond in JSON format:
        {{
            "examples": [
                {{"text": "<example 1>"}},
                {{"text": "<example 2>"}},
                ...
            ]
        }}
        """

        try:
            # Request batch generation
            result = self._make_request(model, prompt)
            print("result", result)

            # Ensure the response is parsed as JSON
            if isinstance(result, str):
                check = json.loads(result)
                result = check

            if not result or "examples" not in result:
                raise ValueError("Invalid response format or no examples returned")

            # Append the "na" tag to each generated example
            batch_examples = [
                {"text": example["text"], "tag": "na"} for example in result["examples"]
            ]
            print("batch_examples", batch_examples)
            all_examples.extend(batch_examples)
            print("all_examples", all_examples)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in batch {batch + 1}: {e}")
            continue  # Skip this batch and continue with the next
        except Exception as e:
            print(f"Error generating batch {batch + 1}: {e}")
            continue  # Skip this batch and continue with the next

    return all_examples

   def classify_metacognition(self, model, text, context=None, mode="basic"):
        """
        Classify a sentence into one of the metacognition categories or "NA" if it doesn't fit.

        Args:
            model (str): The name of the model (e.g., "llama3.2").
            text (str): The input text to classify.
            context (str, optional): Additional background context.
            mode (str): Mode for classification, one of "basic", "1_ex", "5_ex", "10_ex", "chain_of_thoughts".

        Returns:
            dict: A JSON-like dictionary with the classification result.
        """
        background = f"Background information: {context}\n\n" if context else ""
        intro = """
        Metacognition refers to one's ability to plan, monitor, and evaluate their own learning or task performance. 
        Based on Zimmerman's theory of self-regulated learning, metacognition can be categorized into three phases:

            - **Forethought Phase (planning)**:
                Involves setting goals, identifying strategies, and organizing resources to achieve objectives.
                Example: "I will divide the chapter into sections and finish reading it by Thursday."

            - **Performance Phase (monitor)**:
                Involves tracking progress, staying focused, and making adjustments during task execution.
                Example: "I noticed I was getting distracted, so I decided to take a short break to refocus."

            - **Self-Reflection Phase (evaluating)**:
                Involves reflecting on outcomes, assessing strengths/weaknesses, and proposing improvements for future tasks.
                Example: "I didn’t do well on the test because I didn’t review the notes. Next time, I’ll make a study plan."

            - **Not Applicable (na)**:
                The text does not explicitly demonstrate metacognitive behaviors or skills.
                Example: "The coffee I had this morning was delicious." (This is unrelated to metacognition.)
        """
        task = """
        Task:
            Analyze the following text and classify it into one of the categories:
            "planning", "monitor", "evaluating", or "na".
            If the text does not demonstrate metacognitive skills, classify it as "na" (Not Applicable).
            Be as specific as possible and avoid generalizations.\n
        """


        # Chain-of-thoughts specific handling
        if mode == "chain_of_thoughts":
            example_set = ""
            for example in self.examples_chain_of_thoughts:
                example_set += f"""
                Example:
                Text: "{example['text']}"
                Classification: "{example['classification']}"
                Chain-of-Thought: "{example['chain_of_thought']}"
                """

            prompt = f"""
            {background}{intro}

            For each example, include a chain-of-thought reasoning process that explains why the classification was chosen.

            {example_set}

            {task}

            Text: "{text}"

            Respond in JSON format:
            {{
                "text": "{text}",
                "classification": "<category>",
                "chain_of_thought": "<reasoning process>"
            }}
            """
        elif mode == "basic":
            prompt = f"""
            {background}{intro}

            {task}

            Text: "{text}"

            Respond in JSON format:
            {{
                "text": "{text}",
                "classification": "<category>"
            }}
            """
        else:
            example_set = ""
            examples = {
                "1_ex": self.examples_10[:4],
                "5_ex": self.examples_10[:20],
                "10_ex": self.examples_10
            }.get(mode, [])

            for example in examples:
                example_set += f"""
                Example:
                Text: "{example['text']}"
                Classification: "{example['classification']}"
                """

            prompt = f"""
            {background}{intro}

            {example_set}

            {task}

            Text: "{text}"

            Respond in JSON format:
            {{
                "text": "{text}",
                "classification": "<category>"
            }}
            """
        
        return self._make_request(model, prompt)
   
   def classify_monitor_or_na(self, model, text, context=None, mode="basic"):
    """
    Classify a sentence as "monitor" or "na" based on its content.

    Args:
        model (str): The name of the model (e.g., "llama3.2").
        text (str): The input text to classify.
        context (str, optional): Additional background context.
        mode (str): Mode for classification, one of "basic", "1_ex", "5_ex", "10_ex", "chain_of_thoughts".

    Returns:
        dict: A JSON-like dictionary with the classification result.
    """
    background = f"Background information: {context}\n\n" if context else ""
    intro = """
    Metacognition includes monitoring one's learning or task performance. Monitoring involves:
    - Tracking progress during a task.
    - Identifying errors or mistakes.
    - Adjusting actions to improve outcomes.

    Classify the input text based on:
    - **monitor**: If it reflects progress tracking, identifying mistakes, or making adjustments, even informally or fragmented.
      Such as "I forgot to check my pointer."
    - **na**: If it lacks signs of monitoring or is unrelated to the task.
      Such as "The test was really difficult."
    """
    task = """
    Task:
        Analyze the following text and classify it as "monitor" or "na".
    """

    if mode == "chain_of_thoughts":
        example_set = ""
        for example in self.examples_chain_of_thoughts:
            if example["classification"] in ["monitor", "na"]:
                example_set += f"""
                Example:
                text: "{example['text']}"
                classification: "{example['classification']}"
                chain-of-thought: "{example['chain_of_thought']}"
                """

        prompt = f"""
        {background}{intro}

        For each example, include a chain-of-thought reasoning process that explains why the classification was chosen.

        {example_set}

        {task}

        Text: "{text}"

        Respond in JSON format:
        {{
            "text": <inupt text>,
            "classification": "<monitor/na>"
        }}
        """
    elif mode == "basic":
        prompt = f"""
        {background}{intro}

        {task}

        Text: "{text}"

        Respond in JSON format:
        {{
            "text": <inupt text>,
            "classification": "<monitor/na>"
        }}
        """
    else:
        example_set = ""
        examples = {
            "1_ex": self.examples_10[:4],
            "5_ex": self.examples_10[:20],
            "10_ex": self.examples_10
        }.get(mode, [])

        for example in examples:
            if example["classification"] in ["monitor", "na"]:
                example_set += f"""
                Example:
                text: "{example['text']}"
                classification: "{example['classification']}"
                """

        prompt = f"""
        {background}{intro}

        {example_set}

        {task}

        Text: "{text}"

        Respond in JSON format:
        {{
            "text": "{text}",
            "classification": "<monitor/na>"
        }}
        """
    return self._make_request(model, prompt)
   