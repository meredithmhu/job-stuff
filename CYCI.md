# Crush Your Coding Interview by Meta - 10-02-24
[ Allison Slattery - Recruiter ] presenting 

Objective : demonstrate a live technical interview 

Engineers: Batya Zamansky, Salil Desai 

## How do you prepare for an interview?
PRACTICE, PRACTICE, PRACTICE!! 
Whiteboard interviews are nervewracking. The only thing you can control for is how prepared you are! 

## Goals of a coding interview
Interviewers want to know:
- how you think and tackle hard problems!
- how you consider engineering trade-offs (memory vs. time)
- how you communicate in English about technical problems
- don't feel bad if you get the question wrong.

## Format of the interview
Pt. 1: quick introduction - interviewer introduces themselves, you introduce yourself
Pt. 2: coding. they can stop some questions or ask follow ups. be prepared to test code, discuss how it works, analyze performance
Pt. 3: Q&A! You can ask the interviewer questions. 

## Steps to a successful coding interview.
1. repeat the question, at least like make sure in some way that you get what you're being asked.

## Content of the interview
- data structures and algorithms, trade-offs, complexity
- common library functions are fair game - like math, string manipulation 
- specific questions about concepts are rare. They don't ask specific things

Nice ones to know:
- 3D approaches
- Tries
- Heaps

DS's give you a common vocabulary to communicate with your interviewer about. 

# Example of an interview.
## Example question: Given a tree, determine if it is a binary search tree. 
Traverse the tree and see if any node has more than two children. 
I would go up until I get to a root (no more parents), then I would use recursive DFS walk to see if nodes have more than two children

You should ask things:
- clarify what a binary search tree
- how is the tree structure represented?
- are you allowed to use recursion
- ask about the edge cases
- how much memory are you given? how about time

Here's how you start:
- think about the base case

The interviewer is gonna make you code in Python maybe. 

Wow. I can understand the code, but it's not practiced, so I'm not fast enough at all. 

You gotta test the code after this, so you should be able to quickly come up with lots of valid test cases. 
- empty tree
- single node tree
- tree with only right subtrees
- BST
- Tree of all 1's

Last question: explain the runtime of the algorithm in big O notation. O(n) 
Time complexity is pretty important !! 
Also explain the memory in terms of stack frames that are added. 

## Second example question: Add two string numbers and return a string 
Tons of things to consider when clarifying!! 
- do the strings represent integers? 
- will the strings fit in an integer. not necessarily, these could be big numbers
- can i use the BigNumber library? No, that would be way too easy
- will the numbers be negative? no, assume they are positive
- should i handle the case where the number is not well-formatted? No!

It gets complicated if you need to do it manually.
1. how would i do this without a computer? add them one digit at a time.
2. does it matter which direction you add it in? yes, you will have a carry bit
3. where do you store the extra, if it doesn't fit in an integer? probably a linked list/

You will be asked to identify bugs in buggy code! 
(insert the picture that identifies the bugs) 

Test cases: 
- wanna test a long number + 1 to see if your carry works
- add a negative in case negatives are allowed
- add a number to an empty string

Can you assume preconditions are met?
- if the interviewer says they are met, then you don't have to. but if they are not, you'll have to enforce them

Optimization tweaks: 
- like the really small things 
- probably unnecessary, some people will ask and some people won't 

Main takeaways:
1. think out loud
2. ask lots of questions
3. write good code
4. test your code
5. iterate on your solution
6. be yourself!

Final tips:
1. practice on an IDE and time yourself. do Leetcode or Hackerrank! 
2. for virtual interviews, go somewhere quiet with a good internet connection.
3. do mock interviews. get a friend to do a mock interview and then swap.
4. continue practicing coding questions.

# Recruiter questions!
No preference between the years for internships but you have to be a returning student 

Undergrads and grads compete in the same pool 

Research scientists and software engineer generalist new grads have different interview processes
you can ask shirley, who is outside, about research scientist recruiters. 

what to focus on for online assessments: they recommend leetcode, but honestly, pair up and do mock interviews. 

what do you normally interview in? there isn't a preferred language. 

resume tips and fitting the resume to the 
- include your contact details: number, email
- relevant coursework
- academic background: grad year and such
- proficiency in coding languages
- work experience
- don't try to match

Doesn't matter if you've applied to FB before, you can apply again. They hire on a rolling basis. However, you should probably just apply to one role since they do a kind of "Generalist admissions" process.
Timeline - 4 to 8 weeks is when the process starts and ends. Their process is fast, they wanna make offers. 

what is onboarding like?
- everyone goes through new hire orientation
- then you have engineering bootcamp which you learn internal tools in
- you also have to get used to and meet your team
- referrals definitely help!

if you've seen the problem before, you can let the guy know, but it honestly doesn't make much of a difference 

what's the best way to get on a recruiter's radar?
- people will reach out to you on linkedin

system design questions? No

estimated time to hear back: 2 weeks
do you call to reject: they send emails for this, and don't give specific feedback 

if you have an offer on the table and need Meta to expedite, just let us know. 

they like seeing school related or personal projects. but they like to see milestones in projects and an executable or deliverable that they've hit. they are looking for AI/ML people. 
they like seeing specific projects in specific areas. this is for team matching. 
team matching happens for our new grad roles. you work really closely with your recruiter in that timeframe. 

The coding questions aren't really lifted from leetcode - they make their own 
