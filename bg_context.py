generate_pl_bg = """
Metacognition refers to the process of thinking about one's own thinking, including self-regulation and planning. In this scenario, the student is tasked with planning their study strategy to effectively master computer science topics such as data structures and sorting algorithms. 

The student is using the CompassX learning platform, which provides quizzes, exercises, and resources. They can also refer to lecture slides, textbooks, or external materials. To support metacognitive skill development, the student is encouraged to reflect on how they allocate time and resources, set objectives, and structure their study schedule.

We asked the student: "How will you allocate your time and resources to ensure you effectively master these topics? Please describe your plan, priorities, and expected steps in detail."

The generated responses should illustrate the student’s planning metacognitive skills, including:
- Goal-setting and identifying required steps.
- Prioritizing tasks and organizing resources effectively.
- Demonstrating foresight and adaptability. 

The responses should be concise, realistic, and indicative of typical student reflections, emphasizing their ability to plan and regulate their learning process.
"""

generate_ev_bg = """
Metacognition involves the ability to evaluate one's own learning process, including reflection on outcomes, identifying areas of success and failure, and planning future improvements. In this scenario, the student has completed a week of studying computer science topics such as Binary Search Trees and Sorting Algorithms.

Using the CompassX learning platform, the student engaged in quizzes, exercises, and lectures to improve their understanding of these topics. At the end of their study period, they are asked to evaluate their progress by reflecting on the time and effort they spent.

We asked the student: "Reflect on the time and effort you spent studying your chosen topics. Why do you think you made significant progress, or why not? Please provide specific examples and reasoning."

The generated responses should highlight the student’s metacognitive evaluating skills, including:
- Reflection on results and learning outcomes.
- Identification of strengths and weaknesses in their approach.
- Proposals for specific improvements or adjustments for future tasks.

The responses should be concise, realistic, and representative of typical student evaluations, focusing on critical assessment and reflection as key metacognitive skills.
"""

generate_na_bg = """
Background information: The purpose of this dataset is to generate examples of reflections or sentences that do not demonstrate metacognitive skills, such as planning, monitoring, or evaluating. These examples should represent casual or unrelated statements, lacking self-regulation, progress tracking, or reflective insights.

Generated examples should:
- Be concise and realistic, resembling typical casual statements or unrelated reflections.
- Avoid indicating intentional actions, self-assessment, or forward-thinking strategies.
- Be diverse in phrasing and tone, ensuring the examples are unique.

Examples:
- "I guess I’ll just try something random."
- "Not sure what I’ll do next, maybe take a break."
- "I didn’t really think about it."
- "The result doesn’t matter to me."
"""


# 1. **Self-Monitoring**: The ability to track progress, identify areas for improvement, and make adjustments accordingly.
# 2. **Self-Assessment**: The process of evaluating one's own performance, identifying strengths and weaknesses, and making 
# informed decisions about future learning.
# 3. **Self-Reflection**: The process of reflecting on experiences, identifying patterns, and drawing conclusions about the 
# effectiveness of strategies used.
# 4. **Self-Regulation**: The ability to plan and execute intentional actions to regulate learning, such as setting goals, 
# creating schedules, or using memory aids.

# To encourage students' metacognition, particularly their planning skills, 
# the question should guide them to reflect and describe their study plan in detail, 
# without being overly explicit or rigid. Here's the proposed question:

# Question:
# How will you allocate your time and resources to ensure you effectively master these topics? 
# Please describe your plan, priorities, and expected steps in detail.

# Scoring Examples
# Below are scoring examples based on the student's answers to the above question. 
# These are categorized based on the level of planning metacognition, ranging from 0 to 5.

# Score: 5
'''
I will dedicate at least one hour each day to review the topics in the following order: 
Day 1 will focus on Java syntax (e.g., error handling and references), 
Day 2 will cover basic data structures (e.g., binary search trees and linked lists), 
and Day 3 will focus on sorting algorithms and their complexities. 
After completing each section, I will use CompassX to practice and verify my understanding using lecture notes. 
I will summarize my progress each evening and adjust my plan if needed to address any challenges.
'''

# Score: 4
'''
My plan is to focus on Java syntax first, followed by sorting algorithms and data structures. 
I will use CompassX exercises and lecture slides, dedicating one hour daily to studying. 
If I encounter difficulties, I will refer to additional resources. 
I will follow topic priorities but may not have a strict schedule.
'''

# Score: 3
'''
I plan to study different topics each day, such as binary search trees on Day 1 and sorting algorithms on Day 2. 
I will start with lecture slides and then use CompassX to practice. If I don’t have enough time, I might skip some topics.
'''

# Score: 2
'''
I will try to go through some lecture notes and exercises, likely starting with data structures. 
If I have time, I’ll work on sorting algorithms as well.
'''

# Score: 1
'''
I’ll use CompassX to study these topics, but I haven’t decided on the order or plan yet.
'''

# Score: 1
'''
I might check out what’s available to study, maybe starting with binary trees, but I’m not sure if I’ll complete it.
'''


# Background Text
# For a scenario where a student is planning their weekly study topics on a CS learning platform, here's a background context:
bg_planning = '''
The student is planning how to study computer science topics, such as data structures and sorting algorithms, 
over the next week. We provide an online CS learning platform (named CompassX) where they can complete exercises, 
or they may choose to use lecture notes, external resources, or a combination of methods. 
The student is expected to allocate time and resources effectively to master these concepts. 
We asked the student, "How will you allocate your time and resources to ensure you effectively master these topics? 
Please describe your plan, priorities, and expected steps in detail."
The input text is the student's response.
'''


# Proposed Question
# To encourage students to develop metacognitive monitoring skills, 
# the question should guide them to reflect on their performance and identify areas for improvement. 
# Here’s a question tailored to this scenario:
# After completing this test, reflect on your performance. 
# What did you do well, where did you struggle, and how will you address any mistakes or gaps in understanding? 
# Please provide a detailed analysis.

# Scoring Examples
# Below are scoring examples categorized by metacognitive monitoring levels (0–5), 
# based on how effectively the student reflects on their performance and identifies ways to improve.
# Score: 5
'''
I answered most of the questions on sorting algorithms correctly because I reviewed the lecture notes thoroughly. 
However, I struggled with binary search trees because I didn’t fully understand how to trace recursive calls. 
I plan to revisit the tree traversal examples in the lecture slides and practice similar problems on CompassX to strengthen my understanding.
'''

# Score: 4
'''
I did well on Java syntax questions, especially on references, but I missed a few questions on error handling. 
I also struggled with hashing-related problems because I didn’t remember the key properties of hash tables. 
I will review the relevant textbook sections and solve additional CompassX problems on these topics.
'''

# Score: 3
'''
I managed to answer many questions correctly, but I made several errors in sorting algorithms 
because I didn’t fully grasp the complexity analysis. 
I will try to review the topic again. I think I need more practice, but I’m not sure where to start.
'''

# Score: 2
'''
I got some questions wrong, but I’m not sure why. 
Maybe I need to spend more time studying sorting algorithms. 
I think I’ll look at a few examples later.
'''

# Score: 1
'''
I made mistakes, but I didn’t have time to analyze them. I might try again later.
'''

# Score: 1
'''
I don’t know where I went wrong. I don’t think I’ll change my approach.
'''

# Background Text
# This background text provides context for the monitoring scenario within the CompassX platform:
bg_monitoring = '''
The student has just completed a test on computer science topics using an online CS learning platform (named CompassX). 
After each test, they are required to reflect on their performance by answering an open-text question. 
This reflection helps the student identify areas where they performed well, where they struggled, 
and how they plan to address mistakes or gaps in understanding. 
We asked the student, "After completing this test, reflect on your performance. What did you do well, where did you struggle, 
and how will you address any mistakes or gaps in understanding? Please provide a detailed analysis." 
The input text is the student's response.
'''


# Proposed Question
# To foster metacognitive skills, particularly evaluating, 
# the question should encourage students to reflect on their effort and progress critically. 
# Here’s a proposed question based on the provided context:
# Reflect on the time and effort you spent studying your chosen topics. 
# Why do you think you made significant progress, or why not? 
# Please provide specific examples and reasoning.

# Scoring Examples
# Below are examples of student responses, scored from 0 to 5 based on the depth and quality of their reflection in terms of evaluating their progress:
# Score: 5
'''
I spent a total of 3 hours on Binary Search Trees and Sorting Algorithms, 
dividing my time equally between CompassX practice quizzes and reviewing lecture slides. 
I made significant progress because I identified my mistakes during the quizzes and corrected them using the lecture notes. 
However, I realized I still struggle with understanding time complexity analysis, 
so I plan to revisit that topic next week. Overall, 
I feel I’ve mastered tree traversal techniques but need more work on algorithmic efficiency.
'''

# Score: 4
'''
I dedicated about 2 hours to reviewing lecture slides on Binary Search Trees and practicing on CompassX. 
While I made progress in understanding traversal methods, 
I couldn’t complete all the planned quizzes due to time constraints. 
I noticed that I tend to spend too much time reviewing notes instead of practicing problems, 
which I plan to balance better in the future.
'''

# Score: 3
'''
I spent around 1.5 hours on CompassX quizzes, and I feel I made some progress in Binary Search Trees. 
However, I didn’t review the lecture slides as much as I should have, so I didn’t fully grasp the concepts. 
I think I made moderate progress but could have done more with better time management.
'''

# Score: 2
'''
I only spent an hour on Sorting Algorithms and didn’t review Binary Search Trees. 
I struggled with the quizzes because I hadn’t prepared enough, so I don’t think I made much progress. 
I plan to spend more time next week.
'''

# Score: 1
'''
I tried to do some quizzes but didn’t understand them. 
I didn’t spend much time on this week’s plan, so I don’t think I made any progress.
'''

# Score: 1
'''
I didn’t study much and don’t feel like I made progress. I’m not sure what went wrong.
'''

# Background Text
# For this scenario, the background provides the context of the evaluating task within CompassX:
bg_evaluating = '''
The student is using an online CS learning platform (named CompassX) to study computer science topics, 
such as Binary Search Trees and Sorting Algorithms. At the end of their study plan, 
the platform asks students to evaluate their progress by reflecting on the time and effort they spent studying. 
This reflection aims to help the student assess their learning outcomes, 
identify areas of strength and weakness, and plan improvements for the future. 
We asked the student, "Reflect on the time and effort you spent studying your chosen topics. 
Why do you think you made significant progress, or why not? Please provide specific examples and reasoning." 
The input text is the student’s response.
'''


class_bg = "We are analyzing students' metacognitive types based on their feedback from surveys conducted on an online CS learning platform."

examples_10 = [
    # Topic 1: Binary Search Trees
    {"text": "I will spend one hour studying tree traversal today and review insertion tomorrow.", "classification": "planning"},
    {"text": "While coding, I checked the structure of my binary search tree after each insertion.", "classification": "monitor"},
    {"text": "After solving problems, I realized I need to focus on understanding balancing operations.", "classification": "evaluating"},
    {"text": "Binary search trees are widely used in database systems.", "classification": "na"},
    
    # Topic 2: Sorting Algorithms
    {"text": "I will start with bubble sort today and cover quicksort and merge sort over the next two days.", "classification": "planning"},
    {"text": "While practicing quicksort, I debugged each partition function step by step.", "classification": "monitor"},
    {"text": "After implementing merge sort, I realized it's faster than bubble sort for large datasets.", "classification": "evaluating"},
    {"text": "Sorting algorithms are essential in competitive programming.", "classification": "na"},

    # Topic 3: Recursion
    {"text": "I will review recursive functions today and solve at least five related problems on LeetCode.", "classification": "planning"},
    {"text": "While solving recursion problems, I checked if my base case was correctly implemented.", "classification": "monitor"},
    {"text": "Reflecting on my recursion practice, I need to focus more on stack memory usage.", "classification": "evaluating"},
    {"text": "Recursion is a fundamental concept in computer science.", "classification": "na"},

    # Topic 4: Hash Tables
    {"text": "I plan to review hash table basics first and then practice collision resolution methods.", "classification": "planning"},
    {"text": "I checked if my hash function correctly distributed keys to buckets during practice.", "classification": "monitor"},
    {"text": "After implementing open addressing, I noticed its advantages over chaining for small datasets.", "classification": "evaluating"},
    {"text": "Hash tables are used in dictionaries and caching.", "classification": "na"},

    # Topic 5: Graph Algorithms
    {"text": "I will start with depth-first search today and review breadth-first search tomorrow.", "classification": "planning"},
    {"text": "While coding DFS, I checked if all nodes were visited as expected.", "classification": "monitor"},
    {"text": "After solving several problems, I realized I need to practice cycle detection more.", "classification": "evaluating"},
    {"text": "Graphs are used to represent social networks and maps.", "classification": "na"},

    # Topic 6: Dynamic Programming
    {"text": "I plan to study the knapsack problem today and review longest common subsequence tomorrow.", "classification": "planning"},
    {"text": "During practice, I checked if my memoization table had correct values.", "classification": "monitor"},
    {"text": "After solving knapsack problems, I found I need to focus on understanding state transitions.", "classification": "evaluating"},
    {"text": "Dynamic programming is an optimization technique.", "classification": "na"},

    # Topic 7: Time Complexity
    {"text": "I will review Big-O notation today and analyze algorithms for efficiency tomorrow.", "classification": "planning"},
    {"text": "While analyzing algorithms, I checked each loop to calculate time complexity.", "classification": "monitor"},
    {"text": "Reflecting on my practice, I need to focus more on nested loop analysis.", "classification": "evaluating"},
    {"text": "Time complexity measures algorithm efficiency.", "classification": "na"},

    # Topic 8: Software Design Patterns
    {"text": "I plan to review singleton and factory patterns today and observer pattern tomorrow.", "classification": "planning"},
    {"text": "During practice, I checked if my implementations followed design principles.", "classification": "monitor"},
    {"text": "After implementing patterns, I realized I need more practice with observer pattern.", "classification": "evaluating"},
    {"text": "Design patterns are reusable solutions for common problems.", "classification": "na"},

    # Topic 9: Object-Oriented Programming
    {"text": "I will review inheritance today and practice polymorphism tomorrow.", "classification": "planning"},
    {"text": "While coding, I checked if my class hierarchy was correctly implemented.", "classification": "monitor"},
    {"text": "After solving OOP problems, I realized I need more examples to understand abstraction.", "classification": "evaluating"},
    {"text": "OOP is a paradigm based on objects and classes.", "classification": "na"},

    # Topic 10: Debugging Techniques
    {"text": "I will learn about breakpoints today and log debugging tomorrow.", "classification": "planning"},
    {"text": "While debugging, I checked each step to isolate the root cause of errors.", "classification": "monitor"},
    {"text": "After fixing bugs, I realized I need to focus more on understanding stack traces.", "classification": "evaluating"},
    {"text": "Debugging is an essential skill for programmers.", "classification": "na"}
    ]

examples_chain_of_thoughts = [
    # Topic 1: Binary Search Trees
    {
        "text": "I will dedicate one hour today to studying tree traversal methods and another hour tomorrow for practicing insertion techniques.",
        "classification": "planning",
        "chain_of_thought": "The text outlines a clear time allocation and steps for learning tree traversal and insertion techniques, demonstrating planning."
    },
    {
        "text": "While inserting nodes into the tree, I checked after each operation to confirm the tree's structure was correct.",
        "classification": "monitor",
        "chain_of_thought": "The text shows progress tracking and verification during the insertion process, which is characteristic of monitoring."
    },
    {
        "text": "After practicing binary search trees, I realized I need more focus on understanding balancing operations to handle unbalanced trees better.",
        "classification": "evaluating",
        "chain_of_thought": "The text reflects on the outcome of the practice session and identifies areas for improvement, indicating evaluation."
    },
    {
        "text": "Binary search trees are an efficient way to store and retrieve data.",
        "classification": "na",
        "chain_of_thought": "The text provides general information about binary search trees without demonstrating metacognitive skills, so it is classified as 'na'."
    },
    # Topic 2: Sorting Algorithms
    {
        "text": "I plan to start with bubble sort, then move to quicksort, and finally practice merge sort over the next three days.",
        "classification": "planning",
        "chain_of_thought": "The text provides a detailed sequence of steps and topics to cover, demonstrating planning."
    },
    {
        "text": "While debugging my quicksort implementation, I traced the values in the partition function to identify errors.",
        "classification": "monitor",
        "chain_of_thought": "The text describes a self-checking process during debugging, which aligns with monitoring."
    },
    {
        "text": "After implementing sorting algorithms, I noticed that quicksort was more efficient than bubble sort for larger datasets.",
        "classification": "evaluating",
        "chain_of_thought": "The text evaluates the performance of sorting algorithms and reflects on their efficiency, showing evaluation."
    },
    {
        "text": "Sorting algorithms are widely used in various applications such as databases and operating systems.",
        "classification": "na",
        "chain_of_thought": "The text discusses sorting algorithms in general without involving metacognitive skills, so it is classified as 'na'."
    },
    # Topic 3: Recursion
    {
        "text": "I will allocate one hour today to reviewing recursion basics and another hour to solving related problems on LeetCode.",
        "classification": "planning",
        "chain_of_thought": "The text specifies a time allocation and tasks, indicating a structured plan, which is planning."
    },
    {
        "text": "While solving recursive problems, I consistently checked whether my base case was defined correctly.",
        "classification": "monitor",
        "chain_of_thought": "The text mentions a self-checking process during problem-solving, which is a hallmark of monitoring."
    },
    {
        "text": "After finishing several recursive problems, I realized I need to practice more with tail recursion to understand its efficiency.",
        "classification": "evaluating",
        "chain_of_thought": "The text reflects on completed tasks and identifies a specific area for improvement, which is evaluation."
    },
    {
        "text": "Recursion is an essential concept for solving divide-and-conquer problems.",
        "classification": "na",
        "chain_of_thought": "The text provides a general description of recursion without demonstrating metacognitive skills, so it is classified as 'na'."
    },
    # Topic 4: Graph Algorithms
    {
        "text": "I will start with depth-first search today and focus on breadth-first search tomorrow.",
        "classification": "planning",
        "chain_of_thought": "The text outlines a sequential plan to study DFS and BFS, showing planning."
    },
    {
        "text": "While implementing DFS, I verified that all nodes were visited correctly by tracking visited nodes.",
        "classification": "monitor",
        "chain_of_thought": "The text describes tracking progress during DFS implementation, which is monitoring."
    },
    {
        "text": "After completing graph traversal problems, I found that I need more practice on cycle detection.",
        "classification": "evaluating",
        "chain_of_thought": "The text reflects on completed tasks and identifies an area for improvement, which demonstrates evaluation."
    },
    {
        "text": "Graph algorithms are fundamental for network analysis.",
        "classification": "na",
        "chain_of_thought": "The text provides general information about graph algorithms without demonstrating metacognitive skills, so it is classified as 'na'."
    },
    # Topic 5: Dynamic Programming
    {
        "text": "I will review the knapsack problem today and practice related problems on dynamic programming tomorrow.",
        "classification": "planning",
        "chain_of_thought": "The text specifies a clear plan for studying the knapsack problem and practicing, demonstrating planning."
    },
    {
        "text": "While solving dynamic programming problems, I checked if the values in my memoization table were updated correctly.",
        "classification": "monitor",
        "chain_of_thought": "The text discusses self-checking during problem-solving, aligning with monitoring."
    },
    {
        "text": "After practicing dynamic programming, I realized I need to focus on understanding state transitions better.",
        "classification": "evaluating",
        "chain_of_thought": "The text reflects on practice outcomes and identifies areas for improvement, which is evaluation."
    },
    {
        "text": "Dynamic programming is used to solve optimization problems efficiently.",
        "classification": "na",
        "chain_of_thought": "The text provides general information about dynamic programming without demonstrating metacognitive skills, so it is classified as 'na'."
    }
    ]