# SuffixTree: Build A Trie For Exact Matching

__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/specializations/data-structures-algorithms. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Assignment Description:__
<br/>
Problem Introduction: 
Reads will form a collection of strings Patterns that we wish to match against a reference genome Text. For
each string in Patterns, we will first find all its exact matches as a substring of Text (or conclude that it
does not appear in Text). When hunting for the cause of a genetic disorder, we can immediately eliminate
from consideration areas of the reference genome where exact matches occur.
<br/>
<br/>
Multiple Pattern Matching Problem: Find all occurrences of a collection of patterns in a text.
<br/>
<br/>
Input: A string Text and a collection Patterns containing (shorter) strings.
<br/>
<br/>
Output: All starting positions in Text where a string from Patterns appears as a substring.
<br/>
<br/>
To solve this problem, we will consolidate Patterns into a directed tree called a trie (pronounced “try”),
which is written Trie(Patterns) and has the following properties.
∙ The trie has a single root node with indegree 0, denoted root.
∙ Each edge of Trie(Patterns) is labeled with a letter of the alphabet.
∙ Edges leading out of a given node have distinct labels.
∙ Every string in Patterns is spelled out by concatenating the letters along some path from the root
downward.
∙ Every path from the root to a leaf, or node with outdegree 0, spells a string from Patterns.<br/>
<br/>
<br/>
Task: Construct a trie from a collection of patterns.
<br/>
<br/>
Input Format: An integer 𝑛 and a collection of strings Patterns = {𝑝1, . . . , 𝑝𝑛} (each string is given on a
separate line).
<br/>
<br/>
Constraints: 1 ≤ 𝑛 ≤ 100; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; 𝑝𝑖’s contain only symbols A, C, G, T; no 𝑝𝑖 is
a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.
<br/>
<br/>
Output Format: The adjacency list corresponding to Trie(Patterns), in the following format. If
Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the
integers 1 through 𝑛−1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be
encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and
terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling
the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.Task. Construct a trie from a collection of patterns.
<br/>
<br/>
Input Format: An integer 𝑛 and a collection of strings Patterns = {𝑝1, . . . , 𝑝𝑛} (each string is given on a
separate line).
<br/>
<br/>
Constraints: 1 ≤ 𝑛 ≤ 100; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; 𝑝𝑖’s contain only symbols A, C, G, T; no 𝑝𝑖 is
a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.
<br/>
<br/>
Output Format: The adjacency list corresponding to Trie(Patterns), in the following format. If
Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the
integers 1 through 𝑛−1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be
encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and
terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling
the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)"
