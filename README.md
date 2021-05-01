# IS597DS - Finals_Spr2021

Each project from this semester is a public fork linked from this repository.  This is just one of the many assignments students worked on for the course, but this is the *only* one they are permitted to publish openly.

## Final Project Expectations:

You have considerable flexibility about specifics and you will publish your project openly (as a fork from here) to allow making it part of your portfolio if you choose.  You may work alone or in a team of two students. 

Regardless of topic, it must involve notable amounts of original work of your own, though it can of course use existing libraries or be inspired by or adapted from some other published work(s). 

PLAGIARISM IS NOT TOLERATED. From the first commit through all production of documentation and code, it must be crystal clear which, if any, parts of the project were based on or duplicated from any other source(s) all of which must be cited.  This should be so specific that any evaluator can tell which lines of code are original work and which aren't.  Same for all documentation including images, significant algorithms, etc.

## Project Types you may choose:

(Making original variations of puzzles and games isn't as difficult as it may seem -- we'll discuss this in class. _Though admittedly, making *good* game variations -- that are well-balanced, strategically interesting, with good replay value_ can take expertise or luck and play-testing with revisions.  Such balanced elegance isn't required, given the short time you have.)

1. Devise your own new _original_ type of logic puzzle or an _original variation_ of existing puzzle type. Like with previous homework, your program should be able to randomly generate many puzzles of your type and to verify that all puzzles generated comply with the standard meta-rule that only one valid solution exists. It needs to output the unsolved puzzles in a way that a human can print or view them conveniently to try solving them and to somehow output (to file?) or display the solution for each puzzle when requested, so as not to spoil the challenge. An interactive UI to "play" the puzzles interactively is *not* required.

2. OR develop an AI game player for an _original variation_ of some existing strategy game.  If you do this, it needs to be set up so it can either play computer-vs-computer and/or against human players with a reasonable text or graphical UI. 2B. If two teams want to independently develop AI players for the same type of game variant as each other (but using different algorithms, strategies, and/or data structures) so they can compete, that is okay.

3. OR Computationally 'Solve' a game.  _Background: Some strategic games, especially those of perfect information are known to be "solved". See https://en.wikipedia.org/wiki/Solved_game, which we discussed in class._  Sometimes these proofs are done through mathematical analysis, other times through exhaustive computational verification. If you choose this option, you can either write your own code or modify some existing code that plays a game, to exhaustively analyze a game to attempt to prove if it is "solved" in this way for certain configurations. Changes to rules or conditions of a known solved game can alter this outcome and require reanalysis.


## Deliverables and other Requirements:

* Have some fun!
* In your own fork, please replace this README.md file's contents with a good introduction to your own project. 
* Targeted Algorithm Analysis:  Regardless of which option you choose, you need to _describe the performance characteristics of at least one critical part of your program and explain why you chose the data structures and core algorithm(s) you did_. So for example, if you chose Type #1, what's the Big-O, Big-Theta, or Big-Omega run-time complexity of your puzzle solver? Or the puzzle generator? If you're doing Type #2, what's the complexity of your heuristic evaluation function used for pruning?
* If your team has more than one student, take efforts to see that everyone makes git commits. In addition, your README documentation should include a summary of how you shared the work.
* Live in-class presentation of your work.




## option1
### modify soduku
* Disjoint subset  
  a digit can never appear twice in the same cell within different 3x3 boxes

* Thermo rule  
  digits increase along the thermos from bulbs to the end, and in my implementation, I only created thermos of lengh 3, without turning, and the bulbs are always at the known cells in the puzzle.

  ![IMG_1261](https://tva1.sinaimg.cn/large/008i3skNly1gq24igxfzxj30p00p6tah.jpg)



## Analysis of Puzzle Generator

#### Performance characteristics

* Say 9 is n, which is the board width/height.

* For the first row, I use random.shuffle() to shuffle numbers from 1 to 9, the time complexity is O(n), referring to [https://softwareengineering.stackexchange.com/a/215780](https://softwareengineering.stackexchange.com/a/215780)

* For other rows, I will get an intersection of 3 sets which are the remaining numbers in a row, coloumn, or subgrid, to get one set, the time complexity is O(n), to get 3, is still O(n), and to get the intersection, it is still O(n). For such process, I will go over all other cells which is O(n^2). So overall, it is O(n^3)

* And after populate one grid, I will check if this is a disjoint soduku, and I will just check every cell in the first grid, and compare one by one in it compared to other 8 sub grids, time complexity should be O(n^2)
* In sum, time complexity is O(n^3)
* TODO: include the solver first