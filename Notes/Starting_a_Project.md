# Starting a new programming project

Learning how to start an independent project is one of the most challenging aspects of learning to program. You will have a blank canvas where you are expected to build a finished product. This guide will show you the general steps involved in starting a new programming project. By the end you will have the kick start needed to begin any programming project.


## Write down your project idea

Writing down all of your project ideas is a great first step to any project. Not only does this prevent you from forgetting what your idea was, but it helps lock down the idea to a predefined scope.

One of the biggest risks in programming is [*feature creep*](https://en.wikipedia.org/wiki/Feature_creep). This is when you keep adding new features and functionality to a project, while never calling the program complete. Feature creep is a big issue when trying to provide a time line for when the project will be finished.

When starting out, try to keep you projects feasible. **Be ambitious, but not too ambitious.** It's very important to finish projects and build your confidence as quickly as possible.

### Google your idea to see if anybody else has already built it

Before you get too far along with your project's development, you should search Google for existing projects similar to your own. The goal here is three fold:

1. If you are in a hurry, you can implement somebody else's **open source** project for your own needs
2. You can get further ideas on how to make this project better
3. You might determine that this project is a can of worms, and you should try it when you have more time and/or are more experienced

More than likely, somebody has already tried to do the project you are thinking of, so try to find it.


## Break your project down into multiple small steps

When you have your idea nailed down, break it into small steps. Write each small step as a comment in your main program file. This will help you structure the code.

The goal is to make each step into its own function. A side benefit of this is that you will be able to reuse functions for similar tasks.

For example, if you want to download an HTML table from a website to a CSV file, you could break this into three steps:

1. Download the HTML
2. Process the table out of the HTML code
3. Save the table to a CSV file

Each of these steps would be its own function, however, hen linked together this would be a finished program. 

### Pseudocode

And extension of breaking out each step is to write *pseudocode* for the entire program. [Pseudocode](http://www.unf.edu/~broggio/cop2221/2221pseu.htm) is an informal language used to help develop programs. Think of it as a mix between english (or any language) and code.

You don't run your program with pseudocode. You just use it to help you plan your code.

## Start at the beginning and work your way down

Now you get to start programming. Use the pseudocode you wrote above as a guide for what code you should write.

When you have issues, go to Google and start searching for possible answers to your question. This can often require multiple Google searches until you find the right question to ask.

If you still can't find what you want, go back to the drawing board and try to solve this issue from another direction. There are always multiple ways to accomplish the same thing.

Don't forget that you can use the Python interpreter to try out potential code.

### Get the code working before optimizations

An important mantra with programming is to *"make it run, make it right, make it fast"*. What this means is that you should get your program running before you try to make it beautiful and efficient.

You want to determine if your program is going to be useful before spending a lot of time optimizing it. There is nothing worse than spending days optimizing your code only to realize that the code doesn't solve the problem you need it to.

However, you should try to keep your code structure clean and well documented as your write it. Often times you won't come back to the code for many weeks or months, thus it can be difficult to figure out why you wrote what you did.

To make consistent looking Python programs, you should be following the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines. These guidelines ensure that other programmers will be able to easily understand what your code is doing. 

### Continually test each new function

As you write more and more code, make sure that you keep testing each part. You want to make sure that everything is doing exactly what you think it is.

The easiest way to test your code is to print out important variables, ensuring that the output is what you expect.

You can even build automated tests with [unit tests](https://en.wikipedia.org/wiki/Unit_testing).

## Iterate the code to add new features

Now that you have finished your program (or at least version 1 of your project), you can iterate on it. This can include adding new features and optimizing it.

When adding new features, you can follow all the steps in this guide again.

If you are going to use this program on a reoccurring basis, it will be useful to optimize the code. Optimizing the code involves making it faster and more fault tolerant.

Another key task is to check over all items in the program to make sure they are acting the way you think it should. It is very easy for bugs to hide in the code, altering how data is flowing through the process.

It is important to remember that programs are living beasts. Any time you are using data from a third party, your program will break if the provider changes anything with their data. Check on your code from time to time.


#### Good luck building your program!